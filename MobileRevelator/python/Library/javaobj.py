#!/usr/bin/python
# -- Content-Encoding: UTF-8 --
"""
Provides functions for reading and writing (writing is WIP currently) Java
objects serialized or will be deserialized by ObjectOutputStream. This form of
object representation is a standard data interchange format in Java world.

javaobj module exposes an API familiar to users of the standard library
marshal, pickle and json modules.

See:
http://download.oracle.com/javase/6/docs/platform/serialization/spec/protocol.html

:authors: Volodymyr Buell, Thomas Calmant
:license: Apache License 2.0
:version: 0.2.4
:status: Alpha

..

    Copyright 2016 Thomas Calmant

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

# Standard library
import collections
import logging
import os
import struct
import sys

try:
    # Python 3+
    from io import BytesIO
except ImportError:
    # Python 2
    from StringIO import StringIO as BytesIO

try:
    import ftfy.bad_codecs
    javacodec = "utf-8-var"
except ImportError:
    javacodec = "utf-8"

# ------------------------------------------------------------------------------

# Module version
__version_info__ = (0, 2, 4)
__version__ = ".".join(str(x) for x in __version_info__)

# Documentation strings format
__docformat__ = "restructuredtext en"

# ------------------------------------------------------------------------------

# Setup the logger
_log = logging.getLogger(__name__)


def log_debug(message, ident=0):
    """
    Logs a message at debug level

    :param message: Message to log
    :param ident: Number of indentation spaces
    """
    #_log.debug(" " * (ident * 2) + str(message))


def log_error(message, ident=0):
    """
    Logs a message at error level

    :param message: Message to log
    :param ident: Number of indentation spaces
    """
    #_log.error(" " * (ident * 2) + str(message))

# ------------------------------------------------------------------------------


if sys.version_info[0] >= 3:
    # Python 3 interpreter : bytes & str
    def to_bytes(data, encoding="UTF-8"):
        """
        Converts the given string to an array of bytes.
        Returns the first parameter if it is already an array of bytes.

        :param data: A unicode string
        :param encoding: The encoding of data
        :return: The corresponding array of bytes
        """
        if type(data) is bytes:
            # Nothing to do
            return data
        return data.encode(encoding)

    def to_str(data, encoding="UTF-8"):
        """
        Converts the given parameter to a string.
        Returns the first parameter if it is already an instance of ``str``.

        :param data: A string
        :param encoding: The encoding of data
        :return: The corresponding string
        """
        if type(data) is str:
            # Nothing to do
            return data
        return str(data, encoding)

    def read_to_str(data):
        """
        Concats all bytes into a string
        """
        return ''.join(chr(char) for char in data)

else:
    # Python 2 interpreter : str & unicode
    def to_str(data, encoding="UTF-8"):
        """
        Converts the given parameter to a string.
        Returns the first parameter if it is already an instance of ``str``.

        :param data: A string
        :param encoding: The encoding of data
        :return: The corresponding string
        """
        if type(data) is str:
            # Nothing to do
            return data
        return data.encode(encoding)

    # Same operation
    to_bytes = to_str

    def read_to_str(data):
        """
        Nothing to do in Python 2
        """
        return data

# ------------------------------------------------------------------------------


def load(file_object, *transformers, **kwargs):
    """
    Deserializes Java primitive data and objects serialized using
    ObjectOutputStream from a file-like object.

    :param file_object: A file-like object
    :param transformers: Custom transformers to use
    :param ignore_remaining_data: If True, don't log an error when unused
                                  trailing bytes are remaining
    :return: The deserialized object
    """
    # Read keyword argument
    ignore_remaining_data = kwargs.get('ignore_remaining_data', False)

    marshaller = JavaObjectUnmarshaller(
        file_object, kwargs.get('use_numpy_arrays', False))

    # Add custom transformers first
    for transformer in transformers:
        marshaller.add_transformer(transformer)
    marshaller.add_transformer(DefaultObjectTransformer())

    # Read the file object
    return marshaller.readObject(ignore_remaining_data=ignore_remaining_data)


def loads(string, *transformers, **kwargs):
    """
    Deserializes Java objects and primitive data serialized using
    ObjectOutputStream from a string.

    :param string: A Java data string
    :param transformers: Custom transformers to use
    :param ignore_remaining_data: If True, don't log an error when unused
                                  trailing bytes are remaining
    :return: The deserialized object
    """
    # Read keyword argument
    ignore_remaining_data = kwargs.get('ignore_remaining_data', False)

    # Reuse the load method (avoid code duplication)
    return load(BytesIO(string), *transformers,
                ignore_remaining_data=ignore_remaining_data)


def dumps(obj, *transformers):
    """
    Serializes Java primitive data and objects unmarshaled by load(s) before
    into string.

    :param obj: A Python primitive object, or one loaded using load(s)
    :param transformers: Custom transformers to use
    :return: The serialized data as a string
    """
    marshaller = JavaObjectMarshaller()
    # Add custom transformers
    for transformer in transformers:
        marshaller.add_transformer(transformer)

    return marshaller.dump(obj)

# ------------------------------------------------------------------------------


class JavaClass(object):
    """
    Represents a class in the Java world
    """
    def __init__(self):
        """
        Sets up members
        """
        self.name = None
        self.serialVersionUID = None
        self.flags = None
        self.fields_names = []
        self.fields_types = []
        self.superclass = None

    def __str__(self):
        """
        String representation of the Java class
        """
        return self.__repr__()

    def __repr__(self):
        """
        String representation of the Java class
        """
        return "[{0:s}:0x{1:X}]".format(self.name, self.serialVersionUID)

    def __eq__(self, other):
        """
        Equality test between two Java classes

        :param other: Other JavaClass to test
        :return: True if both classes share the same fields and name
        """
        if not isinstance(other, type(self)):
            return False

        return (self.name == other.name and
                self.serialVersionUID == other.serialVersionUID and
                self.flags == other.flags and
                self.fields_names == other.fields_names and
                self.fields_types == other.fields_types and
                self.superclass == other.superclass)


class JavaObject(object):
    """
    Represents a deserialized non-primitive Java object
    """
    def __init__(self):
        """
        Sets up members
        """
        self.classdesc = None
        self.annotations = []

    def get_class(self):
        """
        Returns the JavaClass that defines the type of this object
        """
        return self.classdesc

    def __str__(self):
        """
        String representation
        """
        return self.__repr__()

    def __repr__(self):
        """
        String representation
        """
        name = "UNKNOWN"
        if self.classdesc:
            name = self.classdesc.name
        return "<javaobj:{0}>".format(name)

    def __eq__(self, other):
        """
        Equality test between two Java classes

        :param other: Other JavaClass to test
        :return: True if both classes share the same fields and name
        """
        if not isinstance(other, type(self)):
            return False

        res = (self.classdesc == other.classdesc and
               self.annotations == other.annotations)
        if not res:
            return False

        for name in self.classdesc.fields_names:
            if not getattr(self, name) == getattr(other, name):
                return False
        return True


class JavaString(str):
    """
    Represents a Java String
    """
    def __hash__(self):
        return str.__hash__(self)

    def __eq__(self, other):
        if not isinstance(other, str):
            return False
        return str.__eq__(self, other)


class JavaEnum(JavaObject):
    """
    Represents a Java enumeration
    """
    def __init__(self, constant=None):
        super(JavaEnum, self).__init__()
        self.constant = constant


class JavaArray(list, JavaObject):
    """
    Represents a Java Array
    """
    def __init__(self, classdesc=None):
        list.__init__(self)
        JavaObject.__init__(self)
        self.classdesc = classdesc


class JavaByteArray(JavaObject):
    """
    Represents the special case of Java Array which contains bytes
    """
    def __init__(self, data, classdesc=None):
        JavaObject.__init__(self)
        self._data = struct.unpack("b" * len(data), data)
        self.classdesc = classdesc

    def __str__(self):
        return "JavaByteArray({0})".format(self._data)

    def __getitem__(self, item):
        return self._data[item]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

# ------------------------------------------------------------------------------


class JavaObjectConstants(object):
    """
    Defines the constants of the Java serialization format
    """
    STREAM_MAGIC = 0xaced
    STREAM_VERSION = 0x05

    TC_NULL = 0x70
    TC_REFERENCE = 0x71
    TC_CLASSDESC = 0x72
    TC_OBJECT = 0x73
    TC_STRING = 0x74
    TC_ARRAY = 0x75
    TC_CLASS = 0x76
    TC_BLOCKDATA = 0x77
    TC_ENDBLOCKDATA = 0x78
    TC_RESET = 0x79
    TC_BLOCKDATALONG = 0x7A
    TC_EXCEPTION = 0x7B
    TC_LONGSTRING = 0x7C
    TC_PROXYCLASSDESC = 0x7D
    TC_ENUM = 0x7E
    # Ignore TC_MAX: we don't use it and it messes with TC_ENUM
    # TC_MAX = 0x7E

    # classDescFlags
    SC_WRITE_METHOD = 0x01  # if SC_SERIALIZABLE
    SC_BLOCK_DATA = 0x08    # if SC_EXTERNALIZABLE
    SC_SERIALIZABLE = 0x02
    SC_EXTERNALIZABLE = 0x04
    SC_ENUM = 0x10

    # type definition chars (typecode)
    TYPE_BYTE = 'B'     # 0x42
    TYPE_CHAR = 'C'     # 0x43
    TYPE_DOUBLE = 'D'   # 0x44
    TYPE_FLOAT = 'F'    # 0x46
    TYPE_INTEGER = 'I'  # 0x49
    TYPE_LONG = 'J'     # 0x4A
    TYPE_SHORT = 'S'    # 0x53
    TYPE_BOOLEAN = 'Z'  # 0x5A
    TYPE_OBJECT = 'L'   # 0x4C
    TYPE_ARRAY = '['    # 0x5B

    # list of supported typecodes listed above
    TYPECODES_LIST = [
        # primitive types
        TYPE_BYTE,
        TYPE_CHAR,
        TYPE_DOUBLE,
        TYPE_FLOAT,
        TYPE_INTEGER,
        TYPE_LONG,
        TYPE_SHORT,
        TYPE_BOOLEAN,
        # object types
        TYPE_OBJECT,
        TYPE_ARRAY]

    BASE_REFERENCE_IDX = 0x7E0000

    NUMPY_TYPE_MAP = {
        TYPE_BYTE: 'B',
        TYPE_CHAR: 'b',
        TYPE_DOUBLE: '>d',
        TYPE_FLOAT: '>f',
        TYPE_INTEGER: '>i',
        TYPE_LONG: '>l',
        TYPE_SHORT: '>h',
        TYPE_BOOLEAN: '>B'
    }


class OpCodeDebug(object):
    """
    OP Codes definition and utility methods
    """
    # Type codes
    OP_CODE = dict((getattr(JavaObjectConstants, key), key)
                   for key in dir(JavaObjectConstants)
                   if key.startswith("TC_"))

    TYPE = dict((getattr(JavaObjectConstants, key), key)
                for key in dir(JavaObjectConstants)
                if key.startswith("TYPE_"))

    STREAM_CONSTANT = dict((getattr(JavaObjectConstants, key), key)
                           for key in dir(JavaObjectConstants)
                           if key.startswith("SC_"))

    @staticmethod
    def op_id(op_id):
        """
        Returns the name of the given OP Code
        :param op_id: OP Code
        :return: Name of the OP Code
        """
        return OpCodeDebug.OP_CODE.get(
            op_id, "<unknown OP:{0}>".format(op_id))

    @staticmethod
    def type_code(type_id):
        """
        Returns the name of the given Type Code
        :param type_id: Type code
        :return: Name of the type code
        """
        return OpCodeDebug.TYPE.get(
            type_id, "<unknown Type:{0}>".format(type_id))

    @staticmethod
    def flags(flags):
        """
        Returns the names of the class description flags found in the given
        integer

        :param flags: A class description flag entry
        :return: The flags names as a single string
        """
        names = sorted(
            descr for key, descr in OpCodeDebug.STREAM_CONSTANT.items()
            if key & flags)
        return ', '.join(names)

# ------------------------------------------------------------------------------


class JavaObjectUnmarshaller(JavaObjectConstants):
    """
    Deserializes a Java serialization stream
    """
    def __init__(self, stream, use_numpy_arrays=False):
        """
        Sets up members

        :param stream: An input stream (opened in binary/bytes mode)
        :raise IOError: Invalid input stream
        """
        self.use_numpy_arrays = use_numpy_arrays

        # Check stream
        if stream is None:
            raise IOError("No input stream given")

        # Prepare the association Terminal Symbol -> Reading method
        self.opmap = {
            self.TC_NULL: self.do_null,
            self.TC_CLASSDESC: self.do_classdesc,
            self.TC_OBJECT: self.do_object,
            self.TC_STRING: self.do_string,
            self.TC_LONGSTRING: self.do_string_long,
            self.TC_ARRAY: self.do_array,
            self.TC_CLASS: self.do_class,
            self.TC_BLOCKDATA: self.do_blockdata,
            self.TC_BLOCKDATALONG: self.do_blockdata_long,
            self.TC_REFERENCE: self.do_reference,
            self.TC_ENUM: self.do_enum,
            # note that we are reusing do_null:
            self.TC_ENDBLOCKDATA: self.do_null,
        }

        # Set up members
        self.current_object = None
        self.reference_counter = 0
        self.references = []
        self.object_transformers = []
        self.object_stream = stream

        # Read the stream header (magic & version)
        self._readStreamHeader()

    def readObject(self, ignore_remaining_data=False):
        """
        Reads an object from the input stream

        :param ignore_remaining_data: If True, don't log an error when
                                      unused trailing bytes are remaining
        :return: The unmarshalled object
        :raise Exception: Any exception that occurred during unmarshalling
        """
        try:
            arry=[]
            _, res = self._read_and_exec_opcode(ident=0)
            arry.append(res)
            position_bak = self.object_stream.tell()
            the_rest = self.object_stream.read()
            if not ignore_remaining_data and len(the_rest):
                while len(the_rest):
                    self.object_stream.seek(position_bak)
                    _, res = self._read_and_exec_opcode(ident=0)
                    arry.append(res)
                    position_bak = self.object_stream.tell()
                    the_rest = self.object_stream.read()
            else:
                log_debug("Java Object unmarshalled successfully!")

            self.object_stream.seek(position_bak)
            return arry
        except Exception:
            self._oops_dump_state(ignore_remaining_data)
            raise

    def add_transformer(self, transformer):
        """
        Appends an object transformer to the deserialization process

        :param transformer: An object with a transform(obj) method
        """
        self.object_transformers.append(transformer)

    def _readStreamHeader(self):
        """
        Reads the magic header of a Java serialization stream

        :raise IOError: Invalid magic header (not a Java stream)
        """
        (magic, version) = self._readStruct(">HH")
        if magic != self.STREAM_MAGIC or version != self.STREAM_VERSION:
            raise IOError("The stream is not java serialized object. "
                          "Invalid stream header: {0:04X}{1:04X}"
                          .format(magic, version))

    def _read_and_exec_opcode(self, ident=0, expect=None):
        """
        Reads the next opcode, and executes its handler

        :param ident: Log identation level
        :param expect: A list of expected opcodes
        :return: A tuple: (opcode, result of the handler)
        :raise IOError: Read opcode is not one of the expected ones
        :raise RuntimeError: Unknown opcode
        """
        position = self.object_stream.tell()
        (opid,) = self._readStruct(">B")
        log_debug("OpCode: 0x{0:X} -- {1} (at offset 0x{2:X})"
                  .format(opid, OpCodeDebug.op_id(opid), position), ident)

        if expect and opid not in expect:
            raise IOError(
                "Unexpected opcode 0x{0:X} -- {1} (at offset 0x{2:X})"
                .format(opid, OpCodeDebug.op_id(opid), position))

        try:
            handler = self.opmap[opid]
        except KeyError:
            raise RuntimeError(
                "Unknown OpCode in the stream: 0x{0:X} (at offset 0x{1:X})"
                .format(opid, position))
        else:
            return opid, handler(ident=ident)

    def _readStruct(self, unpack):
        """
        Reads from the input stream, using struct

        :param unpack: An unpack format string
        :return: The result of struct.unpack (tuple)
        :raise RuntimeError: End of stream reached during unpacking
        """
        length = struct.calcsize(unpack)
        ba = self.object_stream.read(length)

        if len(ba) != length:
            raise RuntimeError("Stream has been ended unexpectedly while "
                               "unmarshaling.")

        return struct.unpack(unpack, ba)

    def _readString(self, length_fmt="H"):
        """
        Reads a serialized string

        :param length_fmt: Structure format of the string length (H or Q)
        :return: The deserialized string
        :raise RuntimeError: Unexpected end of stream
        """
        (length,) = self._readStruct(">{0}".format(length_fmt))
        ba = self.object_stream.read(length)
        return to_str(ba.decode(javacodec))

    def do_classdesc(self, parent=None, ident=0):
        """
        Handles a TC_CLASSDESC opcode

        :param parent:
        :param ident: Log indentation level
        :return: A JavaClass object
        """
        # TC_CLASSDESC className serialVersionUID newHandle classDescInfo
        # classDescInfo:
        #   classDescFlags fields classAnnotation superClassDesc
        # classDescFlags:
        #   (byte)                 // Defined in Terminal Symbols and Constants
        # fields:
        #   (short)<count>  fieldDesc[count]

        # fieldDesc:
        #   primitiveDesc
        #   objectDesc
        # primitiveDesc:
        #   prim_typecode fieldName
        # objectDesc:
        #   obj_typecode fieldName className1
        clazz = JavaClass()
        log_debug("[classdesc]", ident)
        class_name = self._readString()
        clazz.name = class_name
        log_debug("Class name: %s" % class_name, ident)

        # serialVersionUID is a Java (signed) long => 8 bytes
        serialVersionUID, classDescFlags = self._readStruct(">qB")
        clazz.serialVersionUID = serialVersionUID
        clazz.flags = classDescFlags

        self._add_reference(clazz, ident)

        log_debug("Serial: 0x{0:X} / {0:d} - classDescFlags: 0x{1:X} {2}"
                  .format(serialVersionUID, classDescFlags,
                          OpCodeDebug.flags(classDescFlags)), ident)
        (length,) = self._readStruct(">H")
        log_debug("Fields num: 0x{0:X}".format(length), ident)

        clazz.fields_names = []
        clazz.fields_types = []
        for fieldId in range(length):
            (typecode,) = self._readStruct(">B")
            field_name = self._readString()
            field_type = self._convert_char_to_type(typecode)

            log_debug("> Reading field {0}".format(field_name), ident)

            if field_type == self.TYPE_ARRAY:
                _, field_type = self._read_and_exec_opcode(
                    ident=ident + 1,
                    expect=(self.TC_STRING, self.TC_REFERENCE))

                if type(field_type) is not JavaString:
                    raise AssertionError("Field type must be a JavaString, "
                                         "not {0}".format(type(field_type)))

            elif field_type == self.TYPE_OBJECT:
                _, field_type = self._read_and_exec_opcode(
                    ident=ident + 1,
                    expect=(self.TC_STRING, self.TC_REFERENCE))

                if type(field_type) is JavaClass:
                    # FIXME: ugly trick
                    field_type = JavaString(field_type.name)

                if type(field_type) is not JavaString:
                    raise AssertionError("Field type must be a JavaString, "
                                         "not {0}".format(type(field_type)))

            log_debug("< FieldName: 0x{0:X} Name:{1} Type:{2} ID:{3}"
                      .format(typecode, field_name, field_type, fieldId),
                      ident)
            assert field_name is not None
            assert field_type is not None

            clazz.fields_names.append(field_name)
            clazz.fields_types.append(field_type)

        if parent:
            parent.__fields = clazz.fields_names
            parent.__types = clazz.fields_types

        # classAnnotation
        (opid,) = self._readStruct(">B")
        log_debug("OpCode: 0x{0:X} -- {1} (classAnnotation)"
                  .format(opid, OpCodeDebug.op_id(opid)), ident)
        if opid != self.TC_ENDBLOCKDATA:
            raise NotImplementedError("classAnnotation isn't implemented yet")

        # superClassDesc
        log_debug("Reading Super Class of {0}".format(clazz.name), ident)
        _, superclassdesc = self._read_and_exec_opcode(
            ident=ident + 1,
            expect=(self.TC_CLASSDESC, self.TC_NULL, self.TC_REFERENCE))
        log_debug("Super Class for {0}: {1}"
                  .format(clazz.name, str(superclassdesc)), ident)
        clazz.superclass = superclassdesc
        # j8spencer (Google, LLC) 2018-01-16: OR in superclass flags to catch
        # any SC_WRITE_METHODs needed for objects.
        if superclassdesc and hasattr(superclassdesc, "flags"):
            clazz.flags |= superclassdesc.flags

        return clazz

    def do_blockdata(self, parent=None, ident=0):
        """
        Handles TC_BLOCKDATA opcode

        :param parent:
        :param ident: Log indentation level
        :return: A string containing the block data
        """
        # TC_BLOCKDATA (unsigned byte)<size> (byte)[size]
        log_debug("[blockdata]", ident)
        (length,) = self._readStruct(">B")
        ba = self.object_stream.read(length)

        # Ensure we have an str
        return read_to_str(ba)

    def do_blockdata_long(self, parent=None, ident=0):
        """
        Handles TC_BLOCKDATALONG opcode

        :param parent:
        :param ident: Log indentation level
        :return: A string containing the block data
        """
        # TC_BLOCKDATALONG (int)<size> (byte)[size]
        log_debug("[blockdatalong]", ident)
        (length,) = self._readStruct(">I")
        ba = self.object_stream.read(length)

        # Ensure we have an str
        return read_to_str(ba)

    def do_class(self, parent=None, ident=0):
        """
        Handles TC_CLASS opcode

        :param parent:
        :param ident: Log indentation level
        :return: A JavaClass object
        """
        # TC_CLASS classDesc newHandle
        log_debug("[class]", ident)

        # TODO: what to do with "(ClassDesc)prevObject".
        # (see 3rd line for classDesc:)
        _, classdesc = self._read_and_exec_opcode(
            ident=ident + 1,
            expect=(self.TC_CLASSDESC, self.TC_PROXYCLASSDESC,
                    self.TC_NULL, self.TC_REFERENCE))
        log_debug("Classdesc: {0}".format(classdesc), ident)
        self._add_reference(classdesc, ident)
        return classdesc

    def do_object(self, parent=None, ident=0):
        """
        Handles a TC_OBJECT opcode

        :param parent:
        :param ident: Log indentation level
        :return: A JavaClass object
        """
        # TC_OBJECT classDesc newHandle classdata[]  // data for each class
        java_object = JavaObject()
        log_debug("[object]", ident)
        log_debug("java_object.annotations just after instantiation: {0}"
                  .format(java_object.annotations), ident)

        # TODO: what to do with "(ClassDesc)prevObject".
        # (see 3rd line for classDesc:)
        opcode, classdesc = self._read_and_exec_opcode(
            ident=ident + 1,
            expect=(self.TC_CLASSDESC, self.TC_PROXYCLASSDESC,
                    self.TC_NULL, self.TC_REFERENCE))
        # self.TC_REFERENCE hasn't shown in spec, but actually is here

        # Create object
        for transformer in self.object_transformers:
            java_object = transformer.create(classdesc)
            if java_object:
                break

        # Store classdesc of this object
        java_object.classdesc = classdesc

        # Store the reference
        self._add_reference(java_object, ident)

        # classdata[]

        if classdesc.flags & self.SC_EXTERNALIZABLE \
                and not classdesc.flags & self.SC_BLOCK_DATA:
            # TODO:
            raise NotImplementedError("externalContents isn't implemented yet")

        if classdesc.flags & self.SC_SERIALIZABLE:
            # TODO: look at ObjectInputStream.readSerialData()
            # FIXME: Handle the SC_WRITE_METHOD flag

            # create megalist
            tempclass = classdesc
            megalist = []
            megatypes = []
            log_debug("Constructing class...", ident)
            while tempclass:
                log_debug("Class: {0}".format(tempclass.name), ident + 1)
                class_fields_str = ' - '.join(
                    ' '.join((field_type, field_name))
                    for field_type, field_name
                    in zip(tempclass.fields_types, tempclass.fields_names))
                if class_fields_str:
                    log_debug(class_fields_str, ident + 2)

                fieldscopy = tempclass.fields_names[:]
                fieldscopy.extend(megalist)
                megalist = fieldscopy

                fieldscopy = tempclass.fields_types[:]
                fieldscopy.extend(megatypes)
                megatypes = fieldscopy

                tempclass = tempclass.superclass

            log_debug("Values count: {0}".format(len(megalist)), ident)
            log_debug("Prepared list of values: {0}".format(megalist), ident)
            log_debug("Prepared list of types: {0}".format(megatypes), ident)

            for field_name, field_type in zip(megalist, megatypes):
                log_debug("Reading field: {0} - {1}"
                          .format(field_type, field_name))
                res = self._read_value(field_type, ident, name=field_name)
                java_object.__setattr__(field_name, res)

        if classdesc.flags & self.SC_SERIALIZABLE \
                and classdesc.flags & self.SC_WRITE_METHOD \
                or classdesc.flags & self.SC_EXTERNALIZABLE \
                and classdesc.flags & self.SC_BLOCK_DATA:
            # objectAnnotation
            log_debug("java_object.annotations before: {0}"
                      .format(java_object.annotations), ident)

            while opcode != self.TC_ENDBLOCKDATA:
                opcode, obj = self._read_and_exec_opcode(ident=ident + 1)
                # , expect=[self.TC_ENDBLOCKDATA, self.TC_BLOCKDATA,
                # self.TC_OBJECT, self.TC_NULL, self.TC_REFERENCE])
                if opcode != self.TC_ENDBLOCKDATA:
                    java_object.annotations.append(obj)

                log_debug("objectAnnotation value: {0}".format(obj), ident)

            log_debug("java_object.annotations after: {0}"
                      .format(java_object.annotations), ident)

        log_debug(">>> java_object: {0}".format(java_object), ident)
        return java_object

    def do_string(self, parent=None, ident=0):
        """
        Handles a TC_STRING opcode

        :param parent:
        :param ident: Log indentation level
        :return: A string
        """
        log_debug("[string]", ident)
        ba = JavaString(self._readString())
        self._add_reference(ba, ident)
        return ba

    def do_string_long(self, parent=None, ident=0):
        """
        Handles a TC_LONGSTRING opcode

        :param parent:
        :param ident: Log indentation level
        :return: A string
        """
        log_debug("[long string]", ident)
        ba = JavaString(self._readString("Q"))
        self._add_reference(ba, ident)
        return ba

    def do_array(self, parent=None, ident=0):
        """
        Handles a TC_ARRAY opcode

        :param parent:
        :param ident: Log indentation level
        :return: A list of deserialized objects
        """
        # TC_ARRAY classDesc newHandle (int)<size> values[size]
        log_debug("[array]", ident)
        _, classdesc = self._read_and_exec_opcode(
            ident=ident + 1,
            expect=(self.TC_CLASSDESC, self.TC_PROXYCLASSDESC,
                    self.TC_NULL, self.TC_REFERENCE))

        array = JavaArray(classdesc)

        self._add_reference(array, ident)

        (size,) = self._readStruct(">i")
        log_debug("size: {0}".format(size), ident)

        type_char = classdesc.name[0]
        assert type_char == self.TYPE_ARRAY
        type_char = classdesc.name[1]

        if type_char == self.TYPE_OBJECT or type_char == self.TYPE_ARRAY:
            for _ in range(size):
                _, res = self._read_and_exec_opcode(ident=ident + 1)
                log_debug("Object value: {0}".format(res), ident)
                array.append(res)
        elif type_char == self.TYPE_BYTE:
            array = JavaByteArray(self.object_stream.read(size), classdesc)
        elif self.use_numpy_arrays:
            import numpy
            array = numpy.fromfile(
                self.object_stream,
                dtype=JavaObjectConstants.NUMPY_TYPE_MAP[type_char],
                count=size)
        else:
            for _ in range(size):
                res = self._read_value(type_char, ident)
                log_debug("Native value: {0}".format(res), ident)
                array.append(res)

        return array

    def do_reference(self, parent=None, ident=0):
        """
        Handles a TC_REFERENCE opcode

        :param parent:
        :param ident: Log indentation level
        :return: The referenced object
        """
        (handle,) = self._readStruct(">L")
        log_debug("## Reference handle: 0x{0:X}".format(handle), ident)
        ref = self.references[handle - self.BASE_REFERENCE_IDX]
        log_debug("###-> Type: {0} - Value: {1}".format(type(ref), ref), ident)
        return ref

    @staticmethod
    def do_null(parent=None, ident=0):
        """
        Handles a TC_NULL opcode

        :param parent:
        :param ident: Log indentation level
        :return: Always None
        """
        return None

    def do_enum(self, parent=None, ident=0):
        """
        Handles a TC_ENUM opcode

        :param parent:
        :param ident: Log indentation level
        :return: A JavaEnum object
        """
        # TC_ENUM classDesc newHandle enumConstantName
        enum = JavaEnum()
        _, classdesc = self._read_and_exec_opcode(
            ident=ident + 1,
            expect=(self.TC_CLASSDESC, self.TC_PROXYCLASSDESC,
                    self.TC_NULL, self.TC_REFERENCE))
        enum.classdesc = classdesc
        self._add_reference(enum, ident)
        _, enumConstantName = self._read_and_exec_opcode(
            ident=ident + 1, expect=(self.TC_STRING, self.TC_REFERENCE))
        enum.constant = enumConstantName
        return enum

    @staticmethod
    def _create_hexdump(src, start_offset=0, length=16):
        """
        Prepares an hexadecimal dump string

        :param src: A string containing binary data
        :param start_offset: The start offset of the source
        :param length: Length of a dump line
        :return: A dump string
        """
        FILTER = ''.join((len(repr(chr(x))) == 3) and chr(x) or '.'
                         for x in range(256))
        pattern = "{{0:04X}}   {{1:<{0}}}  {{2}}\n".format(length * 3)

        # Convert raw data to str (Python 3 compatibility)
        src = to_str(src, 'latin-1')

        result = []
        for i in range(0, len(src), length):
            s = src[i:i + length]
            hexa = ' '.join("{0:02X}".format(ord(x)) for x in s)
            printable = s.translate(FILTER)
            result.append(pattern.format(i + start_offset, hexa, printable))

        return ''.join(result)

    def _read_value(self, field_type, ident, name=""):
        """
        Reads the next value, of the given type

        :param field_type: A serialization typecode
        :param ident: Log indentation
        :param name: Field name (for logs)
        :return: The read value
        :raise RuntimeError: Unknown field type
        """
        if len(field_type) > 1:
            # We don't need details for arrays and objects
            field_type = field_type[0]

        if field_type == self.TYPE_BOOLEAN:
            (val,) = self._readStruct(">B")
            res = bool(val)
        elif field_type == self.TYPE_BYTE:
            (res,) = self._readStruct(">b")
        elif field_type == self.TYPE_CHAR:
            # TYPE_CHAR is defined by the serialization specification
            # but not used in the implementation, so this is
            # a hypothetical code
            res = bytes(self._readStruct(">bb")).decode("utf-16-be")
        elif field_type == self.TYPE_SHORT:
            (res,) = self._readStruct(">h")
        elif field_type == self.TYPE_INTEGER:
            (res,) = self._readStruct(">i")
        elif field_type == self.TYPE_LONG:
            (res,) = self._readStruct(">q")
        elif field_type == self.TYPE_FLOAT:
            (res,) = self._readStruct(">f")
        elif field_type == self.TYPE_DOUBLE:
            (res,) = self._readStruct(">d")
        elif field_type == self.TYPE_OBJECT or field_type == self.TYPE_ARRAY:
            _, res = self._read_and_exec_opcode(ident=ident + 1)
        else:
            raise RuntimeError("Unknown typecode: {0}".format(field_type))

        log_debug("* {0} {1}: {2}".format(field_type, name, res), ident)
        return res

    def _convert_char_to_type(self, type_char):
        """
        Ensures a read character is a typecode.

        :param type_char: Read typecode
        :return: The typecode as a string (using chr)
        :raise RuntimeError: Unknown typecode
        """
        typecode = type_char
        if type(type_char) is int:
            typecode = chr(type_char)

        if typecode in self.TYPECODES_LIST:
            return typecode
        else:
            raise RuntimeError("Typecode {0} ({1}) isn't supported."
                               .format(type_char, typecode))

    def _add_reference(self, obj, ident=0):
        """
        Adds a read reference to the marshaler storage

        :param obj: Reference to add
        :param ident: Log indentation level
        """
        log_debug("## New reference handle 0x{0:X}: {1} -> {2}"
                  .format(len(self.references) + self.BASE_REFERENCE_IDX,
                          type(obj).__name__, obj), ident)
        self.references.append(obj)

    def _oops_dump_state(self, ignore_remaining_data=False):
        """
        Log a deserialization error

        :param ignore_remaining_data: If True, don't log an error when
                                      unused trailing bytes are remaining
        """
        log_error("==Oops state dump" + "=" * (30 - 17))
        log_error("References: {0}".format(self.references))
        log_error("Stream seeking back at -16 byte (2nd line is an actual "
                  "position!):")

        # Do not use a keyword argument
        self.object_stream.seek(-16, os.SEEK_CUR)
        position = self.object_stream.tell()
        the_rest = self.object_stream.read()

        if not ignore_remaining_data and len(the_rest):
            log_error("Warning!!!!: Stream still has {0} bytes left."
                      .format(len(the_rest)))
            log_error(self._create_hexdump(the_rest, position))

        log_error("=" * 30)

# ------------------------------------------------------------------------------


class JavaObjectMarshaller(JavaObjectConstants):
    """
    Serializes objects into Java serialization format
    """
    def __init__(self, stream=None):
        """
        Sets up members

        :param stream: An output stream
        """
        self.object_stream = stream
        self.object_obj = None
        self.object_transformers = []
        self.references = []

    def add_transformer(self, transformer):
        """
        Appends an object transformer to the serialization process

        :param transformer: An object with a transform(obj) method
        """
        self.object_transformers.append(transformer)

    def dump(self, obj):
        """
        Dumps the given object in the Java serialization format
        """
        self.references = []
        self.object_obj = obj
        self.object_stream = BytesIO()
        self._writeStreamHeader()
        self.writeObject(obj)
        return self.object_stream.getvalue()

    def _writeStreamHeader(self):
        """
        Writes the Java serialization magic header in the serialization stream
        """
        self._writeStruct(">HH", 4, (self.STREAM_MAGIC, self.STREAM_VERSION))

    def writeObject(self, obj):
        """
        Appends an object to the serialization stream

        :param obj: A string or a deserialized Java object
        :raise RuntimeError: Unsupported type
        """
        log_debug("Writing object of type {0}".format(type(obj).__name__))
        if isinstance(obj, JavaArray):
            # Deserialized Java array
            self.write_array(obj)
        elif isinstance(obj, JavaEnum):
            # Deserialized Java Enum
            self.write_enum(obj)
        elif isinstance(obj, JavaObject):
            # Deserialized Java object
            self.write_object(obj)
        elif isinstance(obj, JavaString):
            # Deserialized String
            self.write_string(obj)
        elif isinstance(obj, JavaClass):
            # Java class
            self.write_class(obj)
        elif obj is None:
            # Null
            self.write_null()
        elif type(obj) is str:
            # String value
            self.write_blockdata(obj)
        else:
            # Unhandled type
            raise RuntimeError("Object serialization of type {0} is not "
                               "supported.".format(type(obj)))

    def _writeStruct(self, unpack, length, args):
        """
        Appends data to the serialization stream

        :param unpack: Struct format string
        :param length: Unused
        :param args: Struct arguments
        """
        ba = struct.pack(unpack, *args)
        self.object_stream.write(ba)

    def _writeString(self, obj, use_reference=True):
        """
        Appends a string to the serialization stream

        :param obj: String to serialize
        :param use_reference: If True, allow writing a reference
        """
        # TODO: Convert to "modified UTF-8"
        # http://docs.oracle.com/javase/7/docs/api/java/io/DataInput.html#modified-utf-8
        string = to_bytes(obj, "utf-8")

        if use_reference and isinstance(obj, JavaString):
            try:
                idx = self.references.index(obj)
            except ValueError:
                # First appearance of the string
                self.references.append(obj)
                logging.debug(
                    "*** Adding ref 0x%X for string: %s",
                    len(self.references) - 1 + self.BASE_REFERENCE_IDX, obj)

                self._writeStruct(">H", 2, (len(string),))
                self.object_stream.write(string)
            else:
                # Write a reference to the previous type
                logging.debug("*** Reusing ref 0x%X for string: %s",
                              idx + self.BASE_REFERENCE_IDX, obj)
                self.write_reference(idx)
        else:
            self._writeStruct(">H", 2, (len(string),))
            self.object_stream.write(string)

    def write_string(self, obj, use_reference=True):
        """
        Writes a Java string with the TC_STRING type marker

        :param obj: The string to print
        :param use_reference: If True, allow writing a reference
        """
        if use_reference and isinstance(obj, JavaString):
            try:
                idx = self.references.index(obj)
            except ValueError:
                # String is not referenced: let _writeString store it
                self._writeStruct(">B", 1, (self.TC_STRING,))
                self._writeString(obj, use_reference)
            else:
                # Reuse the referenced string
                logging.debug("*** Reusing ref 0x%X for String: %s",
                              idx + self.BASE_REFERENCE_IDX, obj)
                self.write_reference(idx)
        else:
            # Don't use references
            self._writeStruct(">B", 1, (self.TC_STRING,))
            self._writeString(obj, use_reference)

    def write_enum(self, obj):
        """
        Writes an Enum value

        :param obj: A JavaEnum object
        """
        # FIXME: the output doesn't have the same references as the real
        # serializable form
        self._writeStruct(">B", 1, (self.TC_ENUM,))

        try:
            idx = self.references.index(obj)
        except ValueError:
            # New reference
            self.references.append(obj)
            logging.debug(
                "*** Adding ref 0x%X for enum: %s",
                len(self.references) - 1 + self.BASE_REFERENCE_IDX, obj)

            self.write_classdesc(obj.get_class())
        else:
            self.write_reference(idx)

        self.write_string(obj.constant)

    def write_blockdata(self, obj, parent=None):
        """
        Appends a block of data to the serialization stream

        :param obj: String form of the data block
        """
        if type(obj) is str:
            # Latin-1: keep bytes as is
            obj = to_bytes(obj, "latin-1")

        length = len(obj)
        if length <= 256:
            # Small block data
            # TC_BLOCKDATA (unsigned byte)<size> (byte)[size]
            self._writeStruct(">B", 1, (self.TC_BLOCKDATA,))
            self._writeStruct(">B", 1, (length,))
        else:
            # Large block data
            # TC_BLOCKDATALONG (unsigned int)<size> (byte)[size]
            self._writeStruct(">B", 1, (self.TC_BLOCKDATALONG,))
            self._writeStruct(">I", 1, (length,))

        self.object_stream.write(obj)

    def write_null(self):
        """
        Writes a "null" value
        """
        self._writeStruct(">B", 1, (self.TC_NULL,))

    def write_object(self, obj, parent=None):
        """
        Writes an object header to the serialization stream

        :param obj: Not yet used
        :param parent: Not yet used
        """
        # Transform object
        for transformer in self.object_transformers:
            tmp_object = transformer.transform(obj)
            if tmp_object is not obj:
                obj = tmp_object
                break

        self._writeStruct(">B", 1, (self.TC_OBJECT,))
        cls = obj.get_class()
        self.write_classdesc(cls)

        # Add reference
        self.references.append([])
        logging.debug(
            "*** Adding ref 0x%X for object %s",
            len(self.references) - 1 + self.BASE_REFERENCE_IDX, obj)

        all_names = collections.deque()
        all_types = collections.deque()
        tmpcls = cls
        while tmpcls:
            all_names.extendleft(reversed(tmpcls.fields_names))
            all_types.extendleft(reversed(tmpcls.fields_types))
            tmpcls = tmpcls.superclass
        del tmpcls

        logging.debug("<=> Field names: %s", all_names)
        logging.debug("<=> Field types: %s", all_types)

        for field_name, field_type in zip(all_names, all_types):
            try:
                logging.debug("Writing field %s (%s): %s",
                              field_name, field_type, getattr(obj, field_name))
                self._write_value(field_type, getattr(obj, field_name))
            except AttributeError as ex:
                log_error("No attribute {0} for object {1}\nDir: {2}"
                          .format(ex, repr(obj), dir(obj)))
                raise
        del all_names, all_types

        if cls.flags & self.SC_SERIALIZABLE \
                and cls.flags & self.SC_WRITE_METHOD \
                or cls.flags & self.SC_EXTERNALIZABLE \
                and cls.flags & self.SC_BLOCK_DATA:
            for annotation in obj.annotations:
                log_debug("Write annotation {0} for {1}"
                          .format(repr(annotation), repr(obj)))
                if annotation is None:
                    self.write_null()
                else:
                    self.writeObject(annotation)
            self._writeStruct('>B', 1, (self.TC_ENDBLOCKDATA,))

    def write_class(self, obj, parent=None):
        """
        Writes a class to the stream

        :param obj: A JavaClass object
        :param parent:
        """
        self._writeStruct(">B", 1, (self.TC_CLASS,))
        self.write_classdesc(obj)

    def write_classdesc(self, obj, parent=None):
        """
        Writes a class description

        :param obj: Class description to write
        :param parent:
        """
        if obj not in self.references:
            # Add reference
            self.references.append(obj)
            logging.debug(
                "*** Adding ref 0x%X for classdesc %s",
                len(self.references) - 1 + self.BASE_REFERENCE_IDX, obj.name)

            self._writeStruct(">B", 1, (self.TC_CLASSDESC,))
            self._writeString(obj.name)
            self._writeStruct(">qB", 1, (obj.serialVersionUID, obj.flags))
            self._writeStruct(">H", 1, (len(obj.fields_names),))

            for field_name, field_type \
                    in zip(obj.fields_names, obj.fields_types):
                self._writeStruct(
                    ">B", 1, (self._convert_type_to_char(field_type),))
                self._writeString(field_name)
                if field_type[0] in (self.TYPE_OBJECT, self.TYPE_ARRAY):
                    try:
                        idx = self.references.index(field_type)
                    except ValueError:
                        # First appearance of the type
                        self.references.append(field_type)
                        logging.debug(
                            "*** Adding ref 0x%X for field type %s",
                            len(self.references) - 1 + self.BASE_REFERENCE_IDX,
                            field_type)

                        self.write_string(field_type, False)
                    else:
                        # Write a reference to the previous type
                        logging.debug("*** Reusing ref 0x%X for %s (%s)",
                                      idx + self.BASE_REFERENCE_IDX,
                                      field_type, field_name)
                        self.write_reference(idx)

            self._writeStruct(">B", 1, (self.TC_ENDBLOCKDATA,))
            if obj.superclass:
                self.write_classdesc(obj.superclass)
            else:
                self.write_null()
        else:
            # Use reference
            self.write_reference(self.references.index(obj))

    def write_reference(self, ref_index):
        """
        Writes a reference
        :param ref_index: Local index (0-based) to the reference
        """
        self._writeStruct(
            ">BL", 1, (self.TC_REFERENCE, ref_index + self.BASE_REFERENCE_IDX))

    def write_array(self, obj):
        """
        Writes a JavaArray

        :param obj: A JavaArray object
        """
        classdesc = obj.get_class()
        self._writeStruct(">B", 1, (self.TC_ARRAY,))
        self.write_classdesc(classdesc)
        self._writeStruct(">i", 1, (len(obj),))

        # Add reference
        self.references.append(obj)
        logging.debug(
            "*** Adding ref 0x%X for array []",
            len(self.references) - 1 + self.BASE_REFERENCE_IDX)

        type_char = classdesc.name[0]
        assert type_char == self.TYPE_ARRAY
        type_char = classdesc.name[1]

        if type_char == self.TYPE_OBJECT:
            for o in obj:
                self._write_value(classdesc.name[1:], o)
        elif type_char == self.TYPE_ARRAY:
            for a in obj:
                self.write_array(a)
        else:
            log_debug("Write array of type %s" % type_char)
            for v in obj:
                log_debug("Writing: %s" % v)
                self._write_value(type_char, v)

    def _write_value(self, field_type, value):
        """
        Writes an item of an array

        :param field_type: Value type
        :param value: The value itself
        """
        if len(field_type) > 1:
            # We don't need details for arrays and objects
            field_type = field_type[0]

        if field_type == self.TYPE_BOOLEAN:
            self._writeStruct(">B", 1, (1 if value else 0,))
        elif field_type == self.TYPE_BYTE:
            self._writeStruct(">b", 1, (value,))
        elif field_type == self.TYPE_SHORT:
            self._writeStruct(">h", 1, (value,))
        elif field_type == self.TYPE_INTEGER:
            self._writeStruct(">i", 1, (value,))
        elif field_type == self.TYPE_LONG:
            self._writeStruct(">q", 1, (value,))
        elif field_type == self.TYPE_FLOAT:
            self._writeStruct(">f", 1, (value,))
        elif field_type == self.TYPE_DOUBLE:
            self._writeStruct(">d", 1, (value,))
        elif field_type == self.TYPE_OBJECT or field_type == self.TYPE_ARRAY:
            if value is None:
                self.write_null()
            elif isinstance(value, JavaEnum):
                self.write_enum(value)
            elif isinstance(value, (JavaArray, JavaByteArray)):
                self.write_array(value)
            elif isinstance(value, JavaObject):
                self.write_object(value)
            elif isinstance(value, JavaString):
                self.write_string(value)
            elif isinstance(value, str):
                self.write_blockdata(value)
            else:
                raise RuntimeError("Unknown typecode: {0}".format(field_type))
        else:
            raise RuntimeError("Unknown typecode: {0}".format(field_type))

    def _convert_type_to_char(self, type_char):
        """
        Converts the given type code to an int

        :param type_char: A type code character
        """
        typecode = type_char
        if type(type_char) is int:
            typecode = chr(type_char)

        if typecode in self.TYPECODES_LIST:
            return ord(typecode)
        elif len(typecode) > 1:
            if typecode[0] == 'L':
                return ord(self.TYPE_OBJECT)
            elif typecode[0] == '[':
                return ord(self.TYPE_ARRAY)

        raise RuntimeError("Typecode {0} ({1}) isn't supported."
                           .format(type_char, typecode))

# ------------------------------------------------------------------------------


class DefaultObjectTransformer(object):
    """
    Default transformer for the deserialized objects.
    Converts JavaObject objects to Python types (maps, lists, ...)
    """
    class JavaList(list, JavaObject):
        """
        Python-Java list bridge type
        """
        def __init__(self, *args, **kwargs):
            list.__init__(self, *args, **kwargs)
            JavaObject.__init__(self)

    class JavaMap(dict, JavaObject):
        """
        Python-Java dictionary/map bridge type
        """
        def __init__(self, *args, **kwargs):
            dict.__init__(self, *args, **kwargs)
            JavaObject.__init__(self)

    TYPE_MAPPER = {
        "java.util.ArrayList": JavaList,
        "java.util.LinkedList": JavaList,
        "java.util.HashMap": JavaMap,
        "java.util.LinkedHashMap": JavaMap,
        "java.util.TreeMap": JavaMap,
    }

    def create(self, classdesc):
        """
        Transforms a deserialized Java object into a Python object

        :param classdesc: The description of a Java class
        :return: The Python form of the object, or the original JavaObject
        """
        try:
            mapped_type = self.TYPE_MAPPER[classdesc.name]
        except KeyError:
            # Return a JavaObject by default
            return JavaObject()
        else:
            log_debug("---")
            log_debug(classdesc.name)
            log_debug("---")

            java_object = mapped_type()

            log_debug(">>> java_object: {0}".format(java_object))
            return java_object
