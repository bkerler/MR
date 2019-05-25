#!/usr/bin/python3

import sys, re, os, string, sqlite3, glob, base64, subprocess, io, shutil, gzip, zlib, collections
from pathlib import PurePath, Path
from xml.dom import minidom
from whatsapp_decrypt import decryptwhatsapp
from Library import javaobj
from Library.htmlreport import HTMLReportMessaging

class WhatsApp:
    PRODUCT = "WAPAF - WhatsApp Parser for Android Forensics" 
    VERSION = "v0.5 Alpha (2019-05-24)"

    """
    This class opens and parses an android whatsapp database and related files.
        
        WAPAF - WhatsApp Parser for Android Forensics
        (c) 2019 by Björn Knorr

        Released under MIT licence
        
        Decryption of msgstore.db is supported via whatsapp_decrypt.py.

        The class will find and use media und other files. It's possible 
        to run the class by suppling just the msgstore.db. Decryption is in 
        this case supported if the "key" file lies next to the msgstore.db.
        However you will not get any media files linked to chats etc. Embedded
        thumbnails from msgstore.db will be extracted.

        It's recommended to supply the class with a full dump of the
        "/data/com.whatsapp" and "/media/.../WhatsApp" (SD card) directory,
        wich looks exacly like this:

        report
        │
        ├── com.whatsapp                    <- folder from /data
        │   ├── databases
        │   │   ├── msgstore.db             <- main database
        │   │   └── wa.db                   <- contact database
        │   ├── files
        │   │   ├── Avatars                 <- Avatar images
        │   │   │   └── ...
        │   │   └── key                     <- decryption key
        │   └── shared_prefs
        │       └── com.whatsapp_preferences.xml    <- prefs file
        └── WhatsApp                        <- folder from SD card or /media/0
            ├── Databases                   <- msgstore.db backup(s)
            │   └── msgstore.db.crypt12
            └── Media                       <- sent & received files
                └── ...

        If you parse some modded WhatsApp version like YoWhatsApp2, you must
        rename the folders and file names like described above.

        Now the class can be called:

            whatsapp = WhatsApp("/<path>/com.whatsapp/databases/msgstore.db")

            or

            whatsapp = WhatsApp("/<path>/WhatsApp/Databases/msgstore.db.crypt12")
    """

    # default pathes and file names in app directory
    path_root =             None
    path_data_root =        Path("com.whatsapp")
    path_data_databases =   path_data_root / "databases"
    path_data_files =       path_data_root / "files"
    path_data_cache =       path_data_root / "cache"
    path_data_sharedprefs = path_data_root / "shared_prefs"

    path_data_avatars =     path_data_files / "Avatars"
    path_data_avatars_big = path_data_cache / "Profile Pictures"

    # default pathes and file names in whatsapp directory
    path_wa_root =          Path("WhatsApp")
    path_wa_databases =     path_wa_root / "Databases"
    path_wa_media =         path_wa_root / "Media"

    # default file and dirnames
    filename_preferences =  "com.whatsapp_preferences.xml"
    filename_key =          "key"
    filename_wadb =         "wa.db"
    dirname_thumbnail=      "thumbnails"

    # default extensions for users and groups
    JID_EXT_S = "@s.whatsapp.net"
    JID_EXT_G = "@g.us"

    # mapping status id to content
    MESSAGES_STATUS_MSG = 6

    # mapping media_type id to content
    MESSAGES_MEDIA_TYPE = collections.OrderedDict()
    MESSAGES_MEDIA_TYPE.update({
        "TEXT":         (0, ""), 
        "IMAGE":        (1, ""), 
        "VOICE":        (2, ""), 
        "VIDEO":        (3, ""), 
        "CONTACT":      (4, ""),
        "GEO":          (5, ""),
        "ID6":          (6, "-not implemented- media_type:6"),
        "ID7":          (7, "-not implemented- media_type:7"), 
        "CALL_MISSED":  (8, "📱 Call"), 
        "ID9":          (9, "-not implemented- media_type:9"), 
        "CALL_MISSED_SYSTEM": (10, ""), 
        "ID11":         (11, "-not implemented- media_type:11"), 
        "ID12":         (12, "-not implemented- media_type:12"), 
        "GIF":          (13, ""),
        "ID14":         (14, "-not implemented- media_type:14"),
        "DELETED":      (15, "Message deleted by user."),
        "ID16":         (16, "-not implemented- media_type:16"), 
        "ID17":         (17, "-not implemented- media_type:17"), 
        "ID18":         (18, "-not implemented- media_type:18"), 
        "ID19":         (19, "-not implemented- media_type:19"),  
        "STICKER":      (20, "")
    })

    MT_ID2MSG = list(MESSAGES_MEDIA_TYPE.values())
    MT_ID2SC = list(MESSAGES_MEDIA_TYPE.keys())
    MT_SC2ID = MESSAGES_MEDIA_TYPE

    # mapping media_size id to messages
    MESSAGES_EN = collections.OrderedDict()
    MESSAGES_EN.update({
        "ID0":            (0,"-not implemented- media_size:0 {}"),
        "ID1":            (1,"-not implemented- media_size:1 {}"),
        "ID2":            (2,"-not implemented- media_size:2 {}"),
        "ID3":            (3,"-not implemented- media_size:3 {}"),
        "GROUP_JOIN":     (4,"User {} joins the group."),
        "GROUP_LEFT":     (5,"User {} has left the group."),
        "GROUP_PIC":      (6,"User {} has changed the group picture."),
        "ID7":            (7,"-not implemented- media_size:7 {}"),
        "ID8":            (8,"-not implemented- media_size:8 {}"),
        "ID9":            (9,"-not implemented- media_size:9 {}"),
        "GROUP_?":        (10,"-not implemented- media_size:10 {}"),
        "GROUP_CREATE":   (11,"Chat-Group was created or changed from User {}"),
        "GROUP_ADD":      (12,"User {} joins the group. Initiated by {}"),
        "ID13":           (13,"-not implemented- media_size:13 {}"),
        "GROUP_REMOVE":   (14,"User {} was removed from group. Initiated by {}"),
        "ID15":           (15,"-not implemented- media_size:15"),
        "ID16":           (16,"-not implemented- media_size:16 {}"),
        "ID17":           (17,"-not implemented- media_size:17 {}"),
        "ID18":           (18,"-not implemented- media_size:18 {}"),
        "CHAT_NEW":       (19,"🔒 Messages you send to this chat and calls are now secured with end-to-end encryption. Tap for more info."), #19
        "GROUP_JOIN2":    (20,"User {} joined group via invitaion link."),
        "ID21":           (21, "-not implemented- media_size:21 {}"),
        "ID22":           (22, "-not implemented- media_size:22 {}")
    })

    # default is english
    MS_ID2MSG = list(MESSAGES_EN.values())
    MS_SC2ID = MESSAGES_EN
    MS_ID2SC = list(MESSAGES_EN.keys())

    def __init__(self, file_msgstore_db):
        """
        Check and open whatsapp database and other files.

            Opens, decrypts and checks msgstore.db. The returned object will
            have following attribues:

            - owner: a Contact object with the details of the owner
            - contacts: a list of the contacts
            - contact_objects: a dict of Contact objects

            :param file_msgstore_db: path to msgstore.db file
        """
        self.info_output("WhatsApp Class {0}".format(WhatsApp.VERSION), 3)
        self.info_output("Initiasisation ...", 3)

        # default values
        self.owner_jid = "N/A"
        self.owner_name = "Owner"
        self.current = 0

        # set all fileplaces to current directory of msgstore.db by default
        self.file_msgstore_db = Path(file_msgstore_db)
        self.file_wa_db = self.file_msgstore_db.parent / WhatsApp.filename_wadb
        self.file_prefs = self.file_msgstore_db.parent / WhatsApp.filename_preferences
        self.file_key = self.file_msgstore_db.parent / WhatsApp.filename_key

        # search for complete directory structure
        try:
            tmp_parrent = self.file_msgstore_db.parent.parent
            # is msgstore.db in com.whatsapp/databases/ or in WhatsApp/Databases/ ?
            if tmp_parrent.name == WhatsApp.path_data_root.name or tmp_parrent.name == WhatsApp.path_wa_root.name:
                WhatsApp.path_root = tmp_parrent.parent 
                self.file_prefs = WhatsApp.path_root / WhatsApp.path_data_sharedprefs / WhatsApp.filename_preferences
                self.file_key = WhatsApp.path_root / WhatsApp.path_data_files / WhatsApp.filename_key
                self.file_wa_db = WhatsApp.path_root / WhatsApp.path_data_databases / WhatsApp.filename_wadb
            else:
                WhatsApp.path_root = self.file_msgstore_db.parent
                raise RuntimeError('Database not in a sub directory path called "{0}"!'.format(WhatsApp.path_data_databases))
        except Exception as error:
            self.info_output('Searching all needed files in current directory. {0}'.format(error), 1)
    
        # we need at least a valid database
        try:
            self.check_sqlite(self.file_msgstore_db)
        except sqlite3.DatabaseError as error:
            # maybe it's just encrypted, let's try to decrypt it *fingers crossed*
            self.info_output('Can\'t open database file "{0}" Maybe it\'s encryted. {1}'.format(self.file_msgstore_db ,str(error)), 1)
            try:
                # write decrypted file to same location as the encrypted file
                decryptedfile = self.file_msgstore_db.parent / str(self.file_msgstore_db.stem + ".decrypted.db")
                decodedfile = decryptwhatsapp(self.file_msgstore_db, decryptedfile, self.file_key)
                self.check_sqlite(decodedfile)
            except:
                raise
            else:
                self.file_msgstore_db = decodedfile
                self.info_output("Decrypted file: '{0}'".format(self.file_msgstore_db))
        except:
            raise

        # open db connection
        self.db_msgstore = sqlite3.connect(os.fspath(self.file_msgstore_db))
        self.db_msgstore.row_factory = sqlite3.Row
        self.db_msgstore.text_factory = lambda x: str(x.decode('utf_8_sig'))
        
        # check if we have a wa.db and open db
        try:
            self.check_sqlite(self.file_wa_db)
            self.db_wa = sqlite3.connect(os.fspath(self.file_wa_db))
            self.db_wa.row_factory = sqlite3.Row
            self.db_wa.text_factory = lambda x: str(x.decode('utf_8_sig'))
        except:
            self.info_output('No wa.db file in "{0}". This means we have no contact names and status.'.format(self.file_wa_db), 1)
            self.file_wa_db = None
            self.db_wa = None

        # get owner information from prefs
        try:
            self.prefs = self.parse_prefs(self.file_prefs)
        except Exception as error:
            self.info_output("No preference file. This means we have owner name or information. {0}".format(error), 1)
            self.prefs = None
            # fallback: try to get jid from msgstore.db
            tmp_jid = self.find_own_id(self.file_msgstore_db)
            if tmp_jid:
                self.owner_jid = tmp_jid
        else:
            tmp_jid = self.prefs.get("registration_jid")
            if not tmp_jid:
                try:
                    tmp_jid = self.prefs.get("cc") + self.prefs.get("ph")
                    self.owner_jid = tmp_jid + WhatsApp.JID_EXT_S
                except:
                    tmp_jid = self.find_own_id(self.file_msgstore_db)

                if not tmp_jid:
                    tmp_jid = "unkown"
            else:
                self.owner_jid = tmp_jid + WhatsApp.JID_EXT_S
            self.owner_name = self.prefs.get("push_name", "") + " (Owner)"

        # preinit owner, and lists of contacts
        self.init_contacts()
        self.owner = self.Contact(platform_id=self.owner_jid, name=self.owner_name, owner=True)
        self.contact_objects.append(self.owner)

        # we are done
        self.info_output("... finished.", 3)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.contacts[self.current]
        except IndexError:
            self.current = 0
            raise StopIteration()
        self.current += 1
        return item
    
    def check_sqlite(self, database_file):
        """Check SQLite database for integrity."""

        # prevent creation of new SQLite dabases by "opening"
        if not database_file.exists():
            raise FileNotFoundError('[Error:] There is no file "{0}"'.format(database_file))

        try:
            db = sqlite3.connect(os.fspath(database_file))
            db_c = db.cursor()
            # Get the integrity status. 'ok' means we're good
            integrity_status = db_c.execute("PRAGMA integrity_check;").fetchone()[0]
            db_c.close()
        except:
            raise
        else:
            if integrity_status != "ok":
                raise RuntimeError('File "{0}" has integrity issues.'.format(database_file))

    def find_own_id(self, file_msgstore_db=None):
        jid = None

        # let's use the db file from our object
        if not file_msgstore_db:
            file_msgstore_db = self.file_msgstore_db

        try:
            msgstore = sqlite3.connect(os.fspath(file_msgstore_db))
            msgstore.row_factory = sqlite3.Row
            msgstore.text_factory = lambda x: str(x.decode('utf_8_sig'))
            msg_cursor = msgstore.cursor()

            # own id is stored in remote_resource if owner joins group chat
            msg_cursor.execute(
                "SELECT remote_resource as jid FROM messages WHERE "
                "key_from_me=1 AND status={0} AND media_size={1}".format(
                    WhatsApp.MESSAGES_STATUS_MSG, 
                    WhatsApp.MS_SC2ID["GROUP_JOIN"][0]))
            msg = msg_cursor.fetchone()
            if msg:
                jid = msg["jid"]
                if jid:
                    return jid
                self.info_output(
                    'Found owner_id in "messages" table: "{0}"'.format(jid))

        except Exception as error:
            self.info_output(
                'Failure at fetching own user id from "messages" table in '
                '"{0}": {1}'.format(file_msgstore_db, str(error)))

        try:
            # table messages stores own id in thumb_image if you where added to a group chat
            msg_cursor.execute(
                "SELECT thumb_image FROM messages WHERE key_from_me=1 "
                "AND status={0} AND media_size={1}"
                " AND media_duration=1".format(
                    WhatsApp.MESSAGES_STATUS_MSG, 
                    WhatsApp.MS_SC2ID["GROUP_ADD"][0]))

            msg = msg_cursor.fetchone()
            if msg:
                jid = self.jid_from_thumb_image(msg["thumb_image"])
                self.info_output('Found owner_id in "messages" table: "{0}"'.format(jid))
                return jid
        except Exception as error:
            self.info_output('Failure at fetching own user id from "messages" table in "{0}": {1}'.format(file_msgstore_db, str(error)))
        return None

    def parse_prefs(self, path_to_prefs_file):
        """Parses xml preference files (whatsapp_preferences.xml)"""
        preferences = {}
        xmldoc = minidom.parse(os.fspath(path_to_prefs_file))
        cNodes = xmldoc.childNodes
        for node in cNodes:
            eList = node.getElementsByTagName("*")
            for counter, e in enumerate(eList):
                if e.hasAttribute("name"):
                    preferences[e.getAttribute("name")] = " ".join(t.nodeValue for t in e.childNodes if t.nodeType == t.TEXT_NODE)
        self.info_output('Getting preferences from "{0}"'.format(path_to_prefs_file))
        self.info_output('    Found {0} preference(s).'.format(counter+1))
        return preferences
 
    def init_contacts(self):
        """
        Parse wa.db (if available) or as fallback msgstore.db for a contact list
        
            :return: list of WhatsApp IDs
        """

        # default values
        self.contact_objects = []
        contacts_set = set()

        # connect to wa.db if available
        if self.db_wa:
            try:
                wa_cursor = self.db_wa.cursor()
                self.info_output('Getting contacts from "{0}".'.format(self.file_wa_db))

                # table wa_contacts stores all contacts
                wa_cursor.execute("SELECT * FROM wa_contacts WHERE is_whatsapp_user=1 "
                    "ORDER BY wa_name")
                wa = wa_cursor.fetchall()
                source = str(self.file_wa_db.name)  + ' - Table "wa_contacts"'
    
                # loop over contacts
                for counter, w in enumerate(wa):
                    # skip if key_remote_jid is -1
                    if w["jid"] == "-1":
                        continue

                    # build Contact
                    cleartext_name = ""
                    if w["wa_name"]:
                        if w["display_name"]:
                            cleartext_name = w["display_name"] + " (" + w["wa_name"] +")"
                        else:
                            cleartext_name = w["wa_name"]
                    else:
                        if w["display_name"]:
                            cleartext_name = w["display_name"]

                    contacts_set.add(w["jid"])
                    self.contact_objects.append(self.Contact(platform_id=w["jid"], name=cleartext_name, status=w["status"], source=source , source_id=w["_id"]))

                self.info_output("    Found {0} contact(s).".format(counter+1))

            except Exception as error:
                self.info_output('Failure at fetching data from "wa_contacts" table in "{0}": '.format(self.file_wa_db) + str(error))
        
        else:
            #fallback: use msgstore as contact source
            try:
                contacts = []
                msg_cursor = self.db_msgstore.cursor()
                self.info_output('Getting contacts from "{0}".'.format(self.file_msgstore_db))

                # get jid from messages table
                msg_cursor.execute("SELECT key_remote_jid as jid FROM messages GROUP BY key_remote_jid")
                msg = msg_cursor.fetchall()
                for c in msg:
                    contacts.append(c["jid"])
            except Exception as error:
                self.info_output('Failure at fetching contacts from "messages" table in "{0}": '.format(self.file_msgstore_db) + str(error))
                # we have no contacts - this a serious error
                raise

            try:    
                # table "jid" stores some more contacts - let's add them
                msg_cursor.execute("SELECT raw_string as jid FROM jid")
                msg = msg_cursor.fetchall()
                for c in msg:
                    contacts.append(c["jid"])

                # table group_participants stores contacts from groups - let's add them too
                msg_cursor.execute("SELECT jid FROM group_participants GROUP by jid")
                msg = msg_cursor.fetchall()
                for c in msg:
                    contacts.append(c["jid"])
            except Exception as error:
                self.info_output('Failure at fetching additional contacts from "messages" table in "{0}": '.format(self.file_msgstore_db) + str(error))
                
            for counter, jid in enumerate(contacts):
                # skip if key_remote_jid is -1
                if jid == "-1"  or jid == "0@s.whatsapp.net":
                    continue
            
                # build Contact
                contacts_set.add(jid)
                self.contact_objects.append(self.Contact(platform_id=jid, source=str(self.file_msgstore_db.name)))

            self.info_output("    Found {0} contact(s).".format(counter+1))
        self.contacts = list(contacts_set)

    def get_contact(self, platform_id):
        """
        Get details for a given platform_id as {dict}. If platform_id is unknown
        you will get the requestet id back. This is by intention, so you can call this
        function from reports etc. without worring.

            :param self: 
            :param platform_id:
            :returns: found or empty Contact object
        """
        for c in self.contact_objects:
            if c.platform_id == platform_id:
                return c
        return self.Contact(platform_id)

    def get_chat(self, platform_id):
        """
        Parse msgstore.db for a chat of platform_id.

            :param platform_id: WhatsApp ID
            :return: a Chat object
        """

        # connect to msgstore.db
        try:
            msg_cursor = self.db_msgstore.cursor()
            msg_cursor.execute(
                "SELECT count(_id) as count_msg, "
                "min(timestamp) as timestamp_start, "
                "max(timestamp) as timestamp_end "
                "FROM messages WHERE key_remote_jid='{0}'".format(platform_id))
            data = [dict(row) for row in msg_cursor.fetchall()][0]
            self.info_output(
                'Get chat for {0}.'.format(
                    platform_id))
        except Exception as error:
            self.info_output(
                'Failure at fetching data from "messages" table in "{0}": '
                .format(self.file_msgstore_db) + str(error))
            # this is a serious error
            raise
    
        try:
            # get attachment count
            msg_cursor.execute(
                "SELECT count(_id) as count_attach FROM messages WHERE "
                "key_remote_jid='{0}' AND media_mime_type NOT NULL"
                .format(platform_id))
            m2 = msg_cursor.fetchone()
            data.update(m2)

        except Exception as error:
            self.info_output(
                'Failure at fetching some details from "messages" table '
                'in "{0}": '.format(file_msgstore_db) + str(error))

        try:
            # get id of last read message, subject & timstamp (groups)
            msg_cursor.execute(
                "SELECT last_read_message_table_id as last_read_id, "
                "last_message_table_id as last_id, subject, creation "
                "as timestamp_creation "
                "FROM chat_list WHERE key_remote_jid='{0}'"
                .format(platform_id))
            m2 = msg_cursor.fetchone()
            if m2:
                data.update(m2)

        except Exception as error:
            self.info_output(
                'Failure at fetching some details from "chat_list" table '
                'in "{0}": '.format(self.file_msgstore_db) + str(error))

        # generate member_count and adminlist for groupchats
        if WhatsApp.JID_EXT_G in platform_id:
            list_admins = set()

            # table group_participants stores contacts & admins of groups
            try:
                msg_cursor.execute(
                    "SELECT jid, admin FROM group_participants WHERE "
                    "gjid='{0}'".format(platform_id))
                m = msg_cursor.fetchall()
                for count, c in enumerate(m):
                    # TODO: check for admins if no 2 is correct
                    if c["admin"] == 2:
                        list_admins.add(c["jid"])
                # +1 for count starting from 0, +1 for owner of device
                data.update(count_users = count + 2)
            except Exception as error:
                self.info_output(
                    'Failure at fetching some details from '
                    '"group_participants" table in "{0}": '
                    .format(self.file_msgstore_db) + str(error))
            data.update(list_admins = list_admins)
            data.update(memberlist = self.get_members(platform_id))
        else:
            data.update(memberlist = None)

        # add extra data
        data.update(source = str(self.file_msgstore_db.name) + 
            ' - tables "messages", "chat_list and "group_participants"')
        data.update(platform_id = platform_id)
        data.update(contact = self.get_contact(platform_id))

        # add message generator
        if data["count_msg"]:
            data.update(messages = self.get_messages(platform_id))
        else:
            data.update(messages = None)


        self.info_output("    Found {0} message(s).".format(data["count_msg"]))
        return self.Chat(**data)

    def get_messages(self, platform_id):
        """
        Parses msgstore.db and returns a list of Message objects for a givne
        platform_id.
        
        :param platform_id: WhatsApp ID
        :return: generator object which gives back the messages
        """

        # connect to msgstore.db
        try:
            msg_cursor = self.db_msgstore.cursor()
            msg_cursor.execute(
                "SELECT * FROM messages "
                "WHERE key_remote_jid='{0}' "
                "ORDER BY timestamp ASC".format(platform_id))
            for counter, m in enumerate(msg_cursor):
                self.info_output("    getting message: {0}".format(counter) ,2, end="\r")
                yield self.Message(
                    source = self.file_msgstore_db.name,
                    source_id=m["_id"],
                    owner_jid=self.owner.platform_id,
                    key_from_me=m["key_from_me"],
                    key_remote_jid=m["key_remote_jid"],
                    media_wa_type=m["media_wa_type"],
                    data=m["data"],
                    thumb_image=m["thumb_image"],
                    remote_resource= m["remote_resource"],
                    timestamp=m["timestamp"],
                    received_timestamp=m["received_timestamp"],
                    send_timestamp=m["send_timestamp"],
                    status=m["status"],
                    media_size=m["media_size"],
                    media_name=m["media_name"], 
                    media_caption=m["media_caption"],
                    media_hash=m["media_hash"],
                    media_url=m["media_url"],
                    media_duration=m["media_duration"],
                    latitude=m["latitude"],
                    longitude=m["longitude"],
                    media_enc_hash=m["media_enc_hash"],
                    thumbnail=m["key_id"]
                    )
        except Exception as error:
            self.info_output(
                'Failure at fetching messages from "messages" table in "{0}":'
                ' '.format(self.file_msgstore_db) + str(error))
            # this is a serious error
            raise

    def get_members(self, platform_id):
        """
        Parse msgstore.db for a memberlist in a chat of platform_id.

            :param platform_id: WhatsApp ID
            :param file_msgstore_db: whatsapp database file
            :return: a MessageList object

            notice:
            - affected user id is in field thumb_image
            - the action (user removed, user added, ... ) is in the field media_size

            obviously someone at whatsapp smoked pot...
        """

        # connect to msgstore.db
        try:
            msg_cursor = self.db_msgstore.cursor()

        except Exception as error:
            self.info_output(
                'Failure at fetching data from "messages" table in "{0}": '
                .format(self.file_msgstore_db) + str(error))
            # this is a serious error
            return None
            
        # generate memberlists 
        group_contacts = set()
        try:
            msg_cursor.execute(
                "SELECT jid FROM group_participants WHERE "
                "gjid='{0}'".format(platform_id))
            m = msg_cursor.fetchall()
            for c in m:
                group_contacts.add(c["jid"])

            msg_cursor.execute(
                "SELECT max(timestamp) as timestamp_end "
                "FROM messages WHERE key_remote_jid='{0}'".format(platform_id))
            m = msg_cursor.fetchone()
            timestamp_end = m["timestamp_end"]
            
        except Exception as error:
            self.info_output(
                'Failure at fetching some memberlists from '
                '"group_participants" table in "{0}": '
                .format(self.file_msgstore_db) + str(error))
            return None

        # populate MemberList
        memberlist = self.MemberList(platform_id)
        try:
            # initialise list with latest state from group_participants
            #memberlist.add(timestamp_end, group_contacts)

            # fetch user changes from messages table
            msg_cursor.execute(
                "SELECT _id, media_size, timestamp, media_size, thumb_image, "
                "remote_resource FROM messages WHERE status='{0}' "
                "AND key_remote_jid='{1}' "
                "ORDER BY timestamp DESC".format(
                    WhatsApp.MESSAGES_STATUS_MSG, platform_id))

            # loop over messages in reverse order to find member changes backwards
            for m2 in msg_cursor:
                ms = m2["media_size"]
                # add user on remove (we are coming timeline reverse order upwards)
                if ms == WhatsApp.MS_SC2ID["GROUP_REMOVE"][0] \
                    or ms == WhatsApp.MS_SC2ID["GROUP_LEFT"][0]:
                    if ms == WhatsApp.MS_SC2ID["GROUP_REMOVE"][0]:
                        user = self.jid_from_thumb_image(m2["thumb_image"])
                    else:
                        user = m2["remote_resource"]
                    if user in group_contacts:
                        self.info_output(
                            'Tried to add user "{0}" which is already'
                            ' in the chat "{1}". ID {2} in message table.'.format(
                            error, platform_id, m2["_id"]))
                    memberlist.add(m2["timestamp"], group_contacts)
                    group_contacts.add(user)

                #remove user
                if ms == WhatsApp.MS_SC2ID["GROUP_ADD"][0] \
                    or ms == WhatsApp.MS_SC2ID["GROUP_JOIN"][0] \
                    or ms == WhatsApp.MS_SC2ID["GROUP_JOIN2"][0]:
                    try:
                        user = self.jid_from_thumb_image(m2["thumb_image"])
                        if user:
                            memberlist.add(m2["timestamp"], group_contacts)
                            group_contacts.remove(user)
                    except KeyError:
                        self.info_output(
                            'Tried to remove user "{0}" which is not'
                            ' in the chat "{1}". ID {2} in message table.'.format(
                            user, platform_id, m2["_id"]))
                        memberlist.add_backwards(m2["timestamp"], user)

        except Exception as error:
            self.info_output('Creation of member list for "{0}" failed.'
                ' List may be incomplete. {1}'.format(platform_id, error))
        
        return memberlist

    
    def dump_tumbnails(self):
        self.info_output("Dumping thumbnails from database to filesystem ...", 3)
        output_dir = WhatsApp.path_root / self.dirname_thumbnail
        if output_dir.exists():
            self.info_output('Output directory "{0}" exists. Skipping thumbnail dump.'.format(output_dir))
            self.info_output("... finished.", 3)
            return

        output_dir.mkdir(parents=True, exist_ok=True)

        # connect to msgstore.db
        try:
            msg_cursor = self.db_msgstore.cursor()
            msg_cursor.execute(
                "SELECT thumbnail, key_id FROM message_thumbnails")
        except Exception as error:
            self.info_output(
                'Failure at fetching thumbnails from "messages_thumbnails" table in "{0}": {1}'
                ' '.format(self.file_msgstore_db, str(error)))

        for count, msg in enumerate(msg_cursor):
            try:
                output_file = output_dir / str(msg["key_id"])
                output_file.write_bytes(msg["thumbnail"])
                self.info_output('Thumbnail {0}: "{1}"    '.format(count,msg["key_id"]), 2, "\r")
            except Exception as error:
                self.info_output(
                    'Failure at writing thumbnail "{0}": {1}'
                    ' '.format(msg["key_id"], str(error)))
        self.info_output("", 2)
        self.info_output("... finished.", 3)

    @classmethod
    def jid_from_thumb_image(cls, blob):
        """
        Get jid from an Java Array Object
        
        """
        if blob:
            try:
                data = javaobj.loads(blob)[0].annotations[1]
            except:
                data = ""
            return data

    def info_output(self, message, level=2, end="\n"):
        levels = ["Error", "Warning", "Info"]
        if level < 3:
            print("    " + levels[level] + (7-len(levels[level]))*" "+ ": " + str(message), end=end)
        else:
            print("**** " + str(message) + " ****", end=end)


    class Contact:
        """Contact object to store contact information"""
        
        def __init__(self, platform_id, name=None, status=None, source=None, source_id=None, owner=None):
            """
            Create a new Contact object.

                :param platform_id: WhatsApp-ID
                :param name=None: name of contact
                :param status=None: user status
                :param source=None: source of data (database, etc.)
                :param source_id=None: source id of data (id of entry in database)
            """
            self.platform_id = platform_id
            self.name = name
            self.status = status
            self.source = source
            self.source_id = source_id
            self.file_avatar_thumb = self.find_avatar(platform_id, "thumb")
            self.file_avatar = self.find_avatar(platform_id)

            # find owners avatars
            if owner:
                self.file_avatar_thumb = self.find_avatar("me", "thumb")
                file_avatar = WhatsApp.path_root / WhatsApp.path_data_files / "me.jpg"
                if file_avatar.exists()  and file_avatar.stat().st_size:
                    self.file_avatar = file_avatar
                else:
                    self.file_avatar = None

        def find_avatar(self, platform_id, size=None):
            """
            Scans kown places for avatar images.

                :param platform_id: WhatsApp-ID
                :param size=None: size none means full image, "thumb" means thumbnail
                :return: path to image file or None
            """
            if size == "thumb":
                test_pic = WhatsApp.path_root / WhatsApp.path_data_avatars / (str(platform_id) + ".j")
            else:
                id_no, *_ = str(platform_id).split('@')
                test_pic = WhatsApp.path_root / WhatsApp.path_data_avatars_big / (str(id_no) + ".jpg")

            if test_pic.exists() and test_pic.stat().st_size:
                path_avatar = test_pic
                return path_avatar
            else:
                return None


    class Chat:
        """Chat object stores information for a chat session."""

        def __init__(self, platform_id, count_msg=None, last_read_id=None,
            last_id=None, timestamp_start=None, memberlist=None,
            timestamp_end=None, count_attach=None, count_users=None,
            list_admins=None, subject=None, messages=None,
            timestamp_creation=None, source=None, contact=None):

            """
            Create a new Chat object.

            :param platform_id: WhatsApp ID
            :param msg_count=None: number of messages in this chat
            :param subject=None: group name (groups)
            :param last_read_message_id=None: id of last read message 
            :param timestamp_creation: timestamp of chat creation (groups)
            :param timestamp_start: timestamp of first message in chat
            :param timestamp_end: timestamp of last message in chat
            :param attach_count=None: number of attachments in this chat
            :param user_count=None: number of users in this chat
            :param admin_list: [list] of admin platform_ids (groups)
            :param source: source of data (database, etc.)
            """
            
            self.platform_id = platform_id
            self.contact_id = platform_id
            if WhatsApp.JID_EXT_G in platform_id:
                self.chat_type = "group"
            else:
                self.chat_type = "dialog"
            self.count_msg = count_msg
            self.subject = subject
            self.last_read_id = last_read_id
            self.timestamp_creation = timestamp_creation
            self.timestamp_start = timestamp_start
            self.timestamp_end = timestamp_end 
            self.count_attach = count_attach
            if count_users == None:
                self.count_users = 2
            else:
                self.count_users = count_users
            self.list_admins = list_admins
            self.source = source
            self.messages = messages
            self.memberlist = memberlist
            self.contact = contact


    class Message:
        """
        Stores a single message entry from msgstore.db -> messages
        """
        def __init__(self, source_id, owner_jid, key_from_me, key_remote_jid,
            data, thumb_image, remote_resource, timestamp, received_timestamp, 
            send_timestamp, status, media_wa_type, media_size, media_name, 
            media_caption, media_hash, media_duration, latitude,
            longitude, media_enc_hash, thumbnail, source, media_url):

            self.platform_id = key_remote_jid
            self.source_id = source_id
            self.source = source
            self.message_type = None

            # generate status message
            if status == WhatsApp.MESSAGES_STATUS_MSG:
                self.message_type = "status"

                # group messages
                try:
                    sc = WhatsApp.MS_ID2SC[int(media_size)]
                except IndexError:
                    sc = "ID" + str(media_size)
                    WhatsApp.info_output("Error unkown media_size field found, value: {0}", media_size)

                if sc.startswith("GROUP"):   
                    # set media type to text         
                    self.sender_id = key_remote_jid
                    self.receiver_id = owner_jid

                    try:
                        if thumb_image:
                            affected_jid = WhatsApp.jid_from_thumb_image(thumb_image)
                            data = WhatsApp.MS_ID2MSG[media_size][1].format(
                                affected_jid, remote_resource)
                        else:
                            data = WhatsApp.MS_ID2MSG[media_size][1].format(remote_resource)
                    except:
                            data = ""

                    media_size = None
                
                # calls
                elif WhatsApp.MT_ID2SC[int(media_wa_type)].startswith("CALL"):
                    data = WhatsApp.MT_ID2MSG[int(media_wa_type)][1]
                else:
                    try:
                        data = WhatsApp.MS_ID2MSG[int(media_size)][1]
                    except IndexError:
                        data = None
            
            # set sender and receiver
            if key_from_me == 0:
                if WhatsApp.JID_EXT_G in key_remote_jid:
                    self.sender_id = remote_resource
                else:
                    self.sender_id = key_remote_jid
                self.receiver_id = owner_jid
                self.message_type = "incoming" if not self.message_type else self.message_type
            else:
                self.sender_id = owner_jid
                self.receiver_id = key_remote_jid
                self.message_type = "outgoing" if not self.message_type else self.message_type

            # timestamps
            self.timestamp_message = timestamp
            if received_timestamp >0:
                self.timestamp_received = received_timestamp
            if send_timestamp >0:
                self.timestamp_sent = send_timestamp

            # create MessageContent
            self.content_message = WhatsApp.MessageContent(
                media_wa_type=media_wa_type, data=data, media_size=media_size,
                media_name=media_name, media_caption=media_caption,
                media_hash=media_hash, media_duration=media_duration,
                latitude=latitude, longitude=longitude, media_url=media_url,
                media_enc_hash=media_enc_hash, thumbnail=thumbnail,
                thumb_image=thumb_image)


    class MessageContent:
        def __init__(self, media_wa_type, data, media_size, media_name, 
                media_caption, media_hash, media_duration, latitude,
                longitude, media_enc_hash, thumbnail, thumb_image,
                media_url):
            
            self.media_type = WhatsApp.MT_ID2SC[int(media_wa_type)]
            self.size = media_size
            self.caption = media_caption
            self.name = media_name
            self.url = media_url
            self.file_thumbnail = self.find_thumbnail(thumbnail)
            self.file_media = self.find_file(thumb_image)
            self.data = data
            self.duration = media_duration
            self.latitude = latitude
            self.longitude = longitude

        def find_file(self, thumb_image):
            try:
                if thumb_image:
                    media_file_name = javaobj.loads(thumb_image)[0].file.path
                    file_path = WhatsApp.path_root / WhatsApp.path_wa_root / media_file_name
                    if file_path.exists() and file_path.stat().st_size:
                        return file_path
                else:
                    return None
            except:
                return None

        def find_thumbnail(self, thumbnail):
            if thumbnail:
                file_path = WhatsApp.path_root / WhatsApp.dirname_thumbnail / thumbnail
                if file_path.exists() and file_path.stat().st_size:
                    return file_path
            else:
                return None


    class MemberList:
        """
        Stores a list of whatsapp ids of a group chat for a given timestamp
        """

        def __init__(self, platform_id):
            self.timestamp_list = []
            self.contact_list = []
            self.platform_id = platform_id
            self.current = 0

        def __iter__(self):
            return self

        def __next__(self):
            try:
                item = ( self.timestamp_list[self.current], self.contact_list[self.current])
            except IndexError:
                self.current = 0
                raise StopIteration()
            self.current += 1
            return item

        def add(self, timestamp, contactlist):
            """
            Add list of Contacts for a timestamp

            :param timestamp: timestamp of list
            :param contactlist: list of Contact objects
            """
            if timestamp and contactlist:
                self.timestamp_list.append(timestamp)
                self.contact_list.append(contactlist.copy())

        def add_backwards(self, timestamp, platform_id):
            for counter, ts in enumerate(self.timestamp_list):
                if ts >= timestamp:
                    cl = list(self.contact_list[counter].copy())
                    cl.append(platform_id)
                    self.contact_list[counter] = set(cl)

        def get_state(self, timestamp=None):
            """
            Find the last state of MemberList for a given timestamp)

            :param timestamp: timestamp (if empty get latest state)
            :return: a list of jids
            """

            # get latest state
            if not timestamp:
                if self.contact_list:
                    return sorted(self.contact_list[0])
                else:
                    return None

            current_timelist = None
            for counter, entry in enumerate(self.timestamp_list):
                if counter == 0 and timestamp > entry:
                    # timestamp is higher as the highest entry
                    WhatsApp.info_output(self, 
                        "Requested timestamp is higher then the highest in list.", 2)
                    return None
                if timestamp == entry:
                    return sorted(self.contact_list[counter])
                elif timestamp < entry:
                    current_timelist = self.contact_list[counter]
                    continue
                else:
                    return current_timelist
            WhatsApp.info_output(self,
                "Requested timestamp is lower then the lowest in list.", 2)
            return None
        
        def get_allmembers(self):
            """
            Generates a sorted list with all jids which where ever in group

            :return: a set with all jids
            """
            if self.contact_list:
                return sorted(set.union(*self.contact_list))
            else:
                return None

# main function
def main(argv):
    """
    Function for running whatsapp.py class as standalone

        :param argv: params supplied by command line
    """

    from argparse import ArgumentParser

    # argument parser for options
    parser = ArgumentParser(description=
        'Converts WhatsApp database and files into a HTML report.')
    parser.add_argument(dest='infile', help="input 'msgstore.db' or "
        "'msgstore.db.cryptXX' file to scan",nargs='?',
        default='./report/com.whatsapp/databases/msgstore.db')
    parser.add_argument('-o', '--outdir',  dest='outdir', 
        help="optionally choose name of output directory",default='.')
    options = parser.parse_args()

    # create WhatsApp object
    whatsapp = WhatsApp(options.infile)

    # we need to dump the thumbnails
    whatsapp.dump_tumbnails()


    print('\nWhatsApp Account: {0} ({1})'.format(whatsapp.owner.name,
        whatsapp.owner.platform_id))

    output_dir = Path(options.outdir) / "wa-{0}".format(
        whatsapp.file_msgstore_db.name)

    HTMLReportMessaging(output_dir, whatsapp)

# run
if __name__ == '__main__':
    main(sys.argv[1:])