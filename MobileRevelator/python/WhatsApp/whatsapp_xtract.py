# -*- coding: utf-8 -*-
XTRACT_VERSION = "2.6.6"
XTRACT_DATE = "Jan 12, 2017"

'''
WhatsApp Xtract v2.66
- WhatsApp Backup Messages Extractor for Android and iPhone

Released on December 10th, 2011
Last Update on June 1th, 2015

Tested with Whatsapp (Android) 2.16.105
Tested with Whatsapp (iPhone)  2.12.14
---

Changelog:
v2.66 (integrated by B.Kerler -  Jan 12, 2017)
- fixed crypt5-crypt12 support


v2.65 (integrated by B.Kerler -  June 01, 2016)
- add crypt10-crypt12 support
- minor fixes

v2.64 (integrated by B.Kerler -  Mai 22, 2016)
- add support for different report directory
- Python 3 fixes
- Added decryption of crypt,crypt6-10

v2.63 (integrated by dg1mlr -  Mai 12, 2016)
- Bugfix
(Android Version)
- new analysis of File "me" for DB-Ownwer Phone No / jid - Mai 23, 2016
(Iphone Version)
- new Database Version

v2.62 (integrated by dg1mlr -  Apr 01, 2016)
- Group Analysis (List of Senders and added/deleted users from status)
(Android Version)
- analysis of File "me" for DB-Ownwer Phone No / jid
- analysis of File "com.whatsapp_preferences.xml" for DB-Ownwer Name
- new File-Struckture (App)

v2.61 (integrated by dg1mlr -  Nov 09, 2015)
- detect NEWhatsApp (Kira WhatsApp) - 09.11.2015

v2.60 (integrated by dg1mlr -  Oct 07, 2015)
- Combined output A + B - 07.10.2015

v2.58 (integrated by dg1mlr -  Jul 14, 2015)
- Bugfix Check incomplete wa.db  - 14.07.2015
- Bugfix Check incomplete wa.db  - 02.07.2015
- Bugfix Time Filter - 10.06.2015
- Bugfix Broadcast - 10.06.2015
- Bugfix width old Databases - 08.06.2015

v2.58 (modified by B. Kerler - Mai 19, 2015)
- added Python 3 support

v2.58 (integrated by dg1mlr -  Mai 12, 2015)
- wa.db ignored if the table 'wa_contacts' is empty or incomplete

v2.58 (integrated by dg1mlr -  Mai 6, 2015)
- (updated by Ruediger Fischaleck - April 21, 2015)
  Added Android Calls

v2.57 (updated by dg1mlr - March 2, 2015)
- (Feb 27, 2015)
  (Android Version) Media, more Information (What is it and MediaPathFilename) in the report
  (IMAGE, VOICE NOTES, AUDIOS, VIDEOS) in Report Version A and B
  Report A Media Overview in addition the Messege-Number (PK)
- (Mar 2, 2015)
  (Iphone Version) Bugfix GroupInformation,
  Media, more Information (What is it and MediaPathFilename) in the report
  (IMAGE, VOICE NOTES, AUDIOS, VIDEOS) in Report Version A and B
  Report A Media Overview in addition the Messege-Number (PK)
- (Mar 3, 2015)
  (Android Version) better way for location Mediafiles
- (Mar 4, 2015 - Android and Iphone Version)
  add Media Caption
  Bugfix
- (Mar 5, 2015 - Android and Iphone Version)
  add more Information on GPS-Location in the report

Changelog:
v2.56 (updated by dg1mlr - Jul 7, 2014)
- allow to filter by time (switch: -f Y) for activate
  FROM DateTime / first message --- TO DateTime / last message
- Bugfix
- Bugfix width wa.db (Jul 30, 2014)
- Bugfix Time-Filter (Jan 13, 2015)

Changelog:
v2.55 (updated by dg1mlr - Jun 04, 2014)
- (Android Version) wa.db (sqlite 3.7 up) used WAL for juornaling, setting it to legacy
- (Android Version) added more Group-Information in messages
- (Iphone Version) !!! geplant !!! added more Group-Information in messages

- Bugfix
- output filename unify - on manually entcrypted .crypt5 Databses (Apr 08, 2014)
- add broadcast Information  (Apr 10, 2014)
- Bugfix - Repair Database (Mai 30, 2014)

Changelog:
v2.54 (updated by dg1mlr - Feb 11, 2014)
- new FindFile Functions, search now in every Subfolders
- emotion for Column Nick-Name
- Media - use HTML5 Tag Video
- add Info for Chat-Groups (Group Admin and Group Creation Time)
- add Output as on File, like Version 2.2 - switchable width Option -t
  A = one HTML-File per Chat - Standard
  B = one HTML-File


Changelog:
v2.53A (updated by dg1mlr - Feb 05, 2014)
- corrected linking of offline files
- for each chat session, add "contact ID" only when not equil
- added "Time Duration" for Audio and Video [Message] if available
- replace ".plain." in "." for Outputfiles [Android]
- (Iphone version)  new Database Schema - implemet workaround
- (Android Version) now supports Medias in "Voice Notes"
- (Android Version) now supports Medias in Subfolder "Sent"

v2.52 (updated by suloku - Mar 15, 2013)
- Corrected typo causing error.
- (Iphone version): "from" cell in group chats now shows the ZCONTACTNAME of the sender instead of the group's name.
- (Iphone version): added a "whatsapp nick" column to chats (useful when you don't have the contact).

v2.51 (updated by Alon Diamant - Mar 15, 2013)
- v2.5 was now tested with Python 3 as well. :S

v2.5 (updated by Alon Diamant - Mar 14, 2013)
- Improved encrypted Android database detection and decryption code
- Can now repair malformed Android databases (depends on availability of sqlite3 executable)

v2.4 (updated by Alon Diamant - Mar 06, 2013)
- Generates media index file - but crappily, we should set this up better..

v2.3 (updated by Alon Diamant - Mar 05, 2013)
- now generates separate file for each contact
- fixed file search to search for image files in days prior to date given (to fix a bug where because of timezone differences the image file exists but is not found)
- fixed message counts for contacts
- does not list contacts with 0 messages
- now writes version number in generated files
- (Android Version) displays WhatsApp name (server based) if no display name is found for a contact
- (Android Version) Supports Python 2.6

v2.2 (updated by Martina Weidner - Nov 17, 2012)
- now supports new emoji smileys
- (Android Version) hotfix for TypeError in b64encode
- (Android Version) decoded file won't be deleted even if it can't be opened

v2.1 (updated by Fabio Sangiacomo and Martina Weidner - May 7, 2012)
- improved install pyCrypto.bat
- added easy drag and drop possibility with whatsapp_xtract_drag'n'drop_database(s)_here.bat
- (Android Version) added support to fix corrupted android whatsapp database (needs sqlite3, for windows sqlite3.exe is contained in the archive)
- (Android Version) removed wrong extraction of owner in android version
- (Iphone Version) information from Z_METADATA table will be printed to shell
- (Iphone Version) fixed bug in support of older Iphone whatsapp databases

V2.0 (updated by Fabio Sangiacomo and Martina Weidner - Apr 26, 2012)
- supports WhatsApp DBs coming from both Android and iPhone platforms
- (Android Version) wa.db is optional
- (Android Version) now also crypted msgstore.db from the SD card can be imported
- chat list is sorted by the last sent message
- fixed bug that the script didn't work with python 3

V1.3 (updated by Martina Weidner - Apr 17, 2012)
- corrected linking of offline files (now linking according to media file size)

V1.2 (updated by Martina Weidner - Apr 5, 2012)
- media files also linked to offline files
- corrected hyperlinks

V1.1 (updated by Martina Weidner - Apr 5, 2012)
- changed database structure, Android only
- show contact names
- show smileys
- show images
- link / popup for images, video, audio, gps
- clickable links

V1.0 (created by Fabio Sangiacomo - Dec 10, 2011)
- first release, iPhone only:
  it takes in input the file "ChatStorage.sqlite",
  extracts chat sessions and the bare text
- sortable js allows table sorting to make chat sessions easily readable

TODO:

- Add an option for an output directory
- Add an option to split chat file to pages in case that generated file is over certain size
- Add an option to show found image thumbnail instead of base64 thumbnail (to save file size and make loading it faster)

Usage:

For Android DB:
> python whatsapp_xtract.py msgstore.db -w wa.db
OR (if wa.db is unavailable)
> python whatsapp_xtract.py msgstore.db
OR (for crypted db)
> python whatsapp_xtract.py msgstore.db.crypt

For iPhone DB: (-w option is ignored)
> python whatsapp_xtract.py ChatStorage.sqlite

(C)opyright 2012 Fabio Sangiacomo <fabio.sangiacomo@digital-forensics.it>
(C)opyright 2012 Martina Weidner  <martina.weidner@freenet.ch>
(C)opyright 2012 Alon Diamant     <diamant.alon@gmail.com>

Released under MIT licence

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

'''

import sys, re, os, string, datetime, time, sqlite3, glob, webbrowser, base64, subprocess, io
from argparse import ArgumentParser
from os.path import join, getsize
from xml.dom import minidom
import shutil
 
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Warning: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Warning: %s' % e)

def GetBase(input):
    try:
        if (input.rindex('/')>0):
            return input[input.rindex('/') + 1:]
    except:
        return input[input.rindex('\\') + 1:]

def GetPath(input):
    try:
        if (input.rindex('/')>0):
            return input[0:input.rindex('/')]
    except:
            return input[0:input.rindex('\\')]


def PKCS5PaddingLength(data):
  length = data[len(data)-1]
  if ((length > 0) and (length < 16)):
    for i in range (0,length):
      if length != data[len(data)-i-1]:
        return 0
  else:
    return 0
  return length

def decryptwhatsapp(infile,outdir):
    try:
        print("Trying to decrypt Android database...")
        filename, file_extension = os.path.splitext(infile)
        from Crypto.Cipher import AES
        import gzip
        import zlib
        decryptedfile = outdir+"/WhatsApp/Databases/"+infile[infile.find("msgstore"):infile.find(".db.crypt")] + ".db"
        keypath=outdir+"/com.whatsapp/"+FilePathF+"key"
        version=int(file_extension[6:])
        decrypted=b''
        if (version==0):
            key = "346a23652a46392b4d73257c67317e352e3372482177652c"
            if PYTHON_VERSION == 2:
                key = key.decode('hex')
            elif PYTHON_VERSION == 3:
                key = bytes.fromhex(key)
            cipher = AES.new(key,AES.MODE_ECB)
            decrypted = cipher.decrypt(open(infile,"rb").read())
        elif (version>=6) and (version<9):
            if os.path.isfile(keypath):
                with (open(keypath,'rb')) as keyf:
                    keycontent = keyf.read()
                    key = keycontent[126:126+32]
                    with (open(infile,"rb")) as inputf:
                        inputf.seek(51)
                        iv=inputf.read(16)
                        cipher = AES.new(key, AES.MODE_CBC, iv)
                        compressed = cipher.decrypt(open(infile,"rb").read()[51+16:])
                        padlen=PKCS5PaddingLength(compressed)
                        compressed=compressed[0:len(compressed)-padlen]
                        decrypted=gzip.decompress(compressed)
            else:
                print("Couldn't find key in path: "+keypath)
                return
        elif (version>=9) and (version<12):
            if os.path.isfile(keypath):
                with (open(keypath,'rb')) as keyf:
                    keycontent = keyf.read()
                    key = keycontent[126:126+32]
                    with (open(infile,"rb")) as inputf:
                        inputf.seek(51)
                        iv=inputf.read(16)
                        cipher = AES.new(key, AES.MODE_GCM, iv)
                        compressed = cipher.decrypt(open(infile,"rb").read()[51+16:])
                        padlen=PKCS5PaddingLength(compressed)
                        compressed=compressed[0:len(compressed)-padlen]
                        decrypted=gzip.decompress(compressed)
            else:
                print("Couldn't find key in path: "+keypath)
                return
        elif (version==12):
            if os.path.isfile(keypath):
                with (open(keypath,'rb')) as keyf:
                    keycontent = keyf.read()
                    key = keycontent[126:126+32]
                    with (open(infile,"rb")) as inputf:
                        inputf.seek(51)
                        iv=inputf.read(16)
                        cipher = AES.new(key, AES.MODE_GCM, iv)
                        compressed = cipher.decrypt(open(infile,"rb").read()[51+16:])
                        padlen=PKCS5PaddingLength(compressed)
                        decrypted=compressed[0:len(compressed)-padlen]
                        decrypted=zlib.decompress(compressed,32)
            else:
                print("Couldn't find key in path: "+keypath)
                return ""
        else:
                print("Unknown crypt version")
                return ""
        if not os.path.exists(outdir+"/WhatsApp/Databases"):
            os.makedirs(outdir+"/WhatsApp/Databases")
        with open(decryptedfile, "wb") as output:
            output.write(decrypted)
            return decryptedfile
    except:
        print("Error on decryption")
        raise

def asciifunc(dt):
    if (sys.version < '3'):
        if isinstance(dt, unicode) or isinstance(dt, str):
            return True
        else:
            return False
    else:
        if isinstance(dt, str) or isinstance(dt, bytes):
            return True
        else:
            return False

################################################################################
# Chatsession obj definition
class Chatsession:

    # init
    def __init__(self,pkcs,contactname,wa_name,contactid,
                 contactmsgcount,contactunread,contactstatus,lastmessagedate, is_wa_user):

        # if invalid params are passed, sets attributes to invalid values
        # primary key
        if pkcs == "" or pkcs is None:
            self.pk_cs = -1
        else:
            self.pk_cs = pkcs

        # contactname
        if contactname == "" or contactname is None:
            self.contact_name = "N/A"
        else:
            self.contact_name = contactname

        # whatsapp name (on server) used for NICK
        if wa_name == "" or wa_name is None:
            self.wa_name = "N/A"
        else:
            self.wa_name = wa_name

        # contact id
        if contactid == "" or contactid is None:
            self.contact_id = "N/A"
        else:
            self.contact_id = contactid

        # contact msg counter
        if contactmsgcount == "" or contactmsgcount is None:
            self.contact_msg_count = "N/A"
        else:
            self.contact_msg_count = contactmsgcount

        # contact unread msg
        if contactunread == "" or contactunread is None:
            self.contact_unread_msg = "N/A"
        else:
            self.contact_unread_msg = contactunread

        # contact status
        if contactstatus == "" or contactstatus is None:
            self.contact_status = "N/A"
        else:
            self.contact_status = contactstatus

        # contact last message date
        if lastmessagedate == "" or lastmessagedate is None or lastmessagedate == 0:
            self.last_message_date = " N/A" #space is necessary for that the empty chats are placed at the end on sorting
        else:
            try:
                if mode == IPHONE:
                    lastmessagedate = str(lastmessagedate)
                    if lastmessagedate.find(".") > -1: #if timestamp is not like "304966548", but like "306350664.792749", then just use the numbers in front of the "."
                        lastmessagedate = lastmessagedate[:lastmessagedate.find(".")]
                    self.last_message_date = datetime.datetime.fromtimestamp(int(lastmessagedate)+11323*60*1440)
                elif mode == ANDROID:
                    msgdate = str(lastmessagedate)
                    # cut last 3 digits (microseconds)
                    msgdate = msgdate[:-3]
                    self.last_message_date = datetime.datetime.fromtimestamp(int(msgdate))
                self.last_message_date = str( self.last_message_date )
            except (TypeError, ValueError) as msg:
                print('Error while reading chat #{0}: {1}'.format(self.pk_cs,msg))
                self.last_message_date = " N/A error"


        # is_wa_user
        if is_wa_user == "" or is_wa_user is None:
            self.is_wa_user = "N/A"
        else:
            self.is_wa_user = is_wa_user

        # chat session messages
        self.msg_list = []

        # chat session is Group
        # if contact_id.find("@g.us") >0:

        # chat # Group Members
        self.members = " N/A"

        # chat session Groupmebers found
        self.gms_list = []

    # comparison operator
    def __cmp__(self, other):
        if self.pk_cs == other.pk_cs:
                return 0
        return 1

################################################################################
# Message obj definition
class Message:

    # init
    def __init__(self,pkmsg,fromme,msgdate,text,contactfrom,wa_name,msgstatus,localurl,mediaurl,mediacaption,mediathumb,mediathumblocalurl,mediawatype,mediasize,mediaduration,latitude,longitude,vcardname,vcardstring,groupeventtype,groupmemberjid):

        # if invalid params are passed, sets attributes to invalid values
        # primary key
        if pkmsg == "" or pkmsg is None:
            self.pk_msg = -1
        else:
            self.pk_msg = pkmsg

        # "from me" flag
        if fromme == "" or fromme is None:
            self.from_me = -1
        else:
            self.from_me = fromme

        # message timestamp
        if msgdate == "" or msgdate is None or msgdate == 0:
            self.msg_date = "N/A"
        else:
            try:
                if mode == IPHONE:
                    msgdate = str(msgdate)
                    if msgdate.find(".") > -1: #if timestamp is not like "304966548", but like "306350664.792749", then just use the numbers in front of the "."
                        msgdate = msgdate[:msgdate.find(".")]
                    self.msg_date = datetime.datetime.fromtimestamp(int(msgdate)+11323*60*1440)
                elif mode == ANDROID:
                    msgdate = str(msgdate)
                    # cut last 3 digits (microseconds)
                    msgdate = msgdate[:-3]
                    self.msg_date = datetime.datetime.fromtimestamp(int(msgdate))
            except (TypeError, ValueError) as msg:
                print('Error while reading message #{0}: {1}'.format(self.pk_msg,msg))
                self.msg_date = "N/A error"

        # message text
        if text == "" or text is None:
            self.msg_text = "N/A"
        if mediawatype == "8" and contactfrom == "me":
                if mediaduration != 0:
                    self.msg_text = "<img src='data/img/call.png'  style='width:20px;height:20px;vertical-align:middle'> Outgoing call. Duration: "  + timeperiod(mediaduration) + ""
                else:
                    self.msg_text = "<img src='data/img/call.png'  style='width:20px;height:20px;vertical-align:middle'> Outgoing call. Not accepted call."
        elif mediawatype == "8" and contactfrom != "me":
                if mediaduration != 0:
                    self.msg_text = "<img src='data/img/call.png' style='width:20px;height:20px;vertical-align:middle'> Incoming call. Duration: " + timeperiod(mediaduration) + ""
                else:
                    self.msg_text = "<img src='data/img/call.png'  style='width:20px;height:20px;vertical-align:middle'> Missed call."
        else:
            self.msg_text = text
        # contact from
        if contactfrom == "" or contactfrom is None:
            self.contact_from = "N/A"
        else:
            self.contact_from = contactfrom
        # whatsapp name (on server) (used for NICK)
        if wa_name == "" or wa_name is None:
            self.wa_name = "N/A"
        else:
            self.wa_name = wa_name

        # media
        if localurl == "" or localurl is None:
            self.local_url = ""
        else:
            self.local_url = localurl
        if mediaurl == "" or mediaurl is None:
            self.media_url = ""
        else:
            self.media_url = mediaurl
        mediacaption
        if mediacaption == "" or mediacaption is None:
            self.media_caption = ""
        else:
            self.media_caption = mediacaption
        if mediathumb == "" or mediathumb is None:
            self.media_thumb = ""
        else:
            self.media_thumb = mediathumb
        if mediathumblocalurl == "" or mediathumblocalurl is None:
            self.media_thumb_local_url = ""
        else:
            self.media_thumb_local_url = mediathumblocalurl
        if mediawatype == "" or mediawatype is None:
            self.media_wa_type = ""
        else:
            self.media_wa_type = mediawatype
        if mediasize == "" or mediasize is None:
            self.media_size = ""
        else:
            self.media_size = mediasize
        if mediaduration == "" or mediaduration is None:
            self.media_duration = ""
        else:
            self.media_duration = mediaduration

        #status
        if msgstatus == "" or msgstatus is None:
            self.status = "N/A"
        else:
            self.status = msgstatus

        #GPS
        if latitude == "" or latitude is None:
            self.latitude = ""
        else:
            self.latitude = latitude
        if longitude == "" or longitude is None:
            self.longitude = ""
        else:
            self.longitude = longitude

        #VCARD
        if vcardname == "" or vcardname is None:
            self.vcard_name = ""
        else:
            self.vcard_name = vcardname
        if vcardstring == "" or vcardstring is None:
            self.vcard_string = ""
        else:
            self.vcard_string = vcardstring

        #Groupeventtype
        if groupeventtype == "" or groupeventtype is None:
            self.group_event_type = "N/A"
        else:
            self.group_event_type = groupeventtype

        #Groupmemberjid - contactfrom
        if groupmemberjid == "" or groupmemberjid is None:
            self.group_member_jid = "N/A"
        else:
            self.group_member_jid = groupmemberjid

    # comparison operator
    def __cmp__(self, other):
        if self.pk_msg == other.pk_msg:
                return 0
        return 1

class GMembers:

    # init
    def __init__(self,groupmemberjid,display_name,wa_name,has_send,has_changed_Group,has_changed_GroupPicture,is_added,is_deleted):

        # if invalid params are passed, sets attributes to invalid values

        # primary key
        #Groupmemberjid - contactfrom
        if groupmemberjid == "" or groupmemberjid is None:
            self.group_member_jid = "N/A"
        else:
            self.group_member_jid = str(groupmemberjid)

        # display_name
        if display_name == "" or display_name is None:
            self.display_name = "N/A"
        else:
            self.display_name = str(display_name)

        # whatsapp name (on server) (used for NICK)
        if wa_name == "" or wa_name is None:
            self.wa_name = "N/A"
        else:
            self.wa_name = str(wa_name)

        #Groupeventtypes

        if has_send == "" or has_send is None:
            self.has_send = 0
        else:
            self.has_send = has_send

        if has_changed_GroupPicture == "" or has_changed_GroupPicture is None:
            self.has_changed_GroupPicture = 0
        else:
            self.has_changed_GroupPicture = has_changed_GroupPicture

        if has_changed_Group == "" or has_changed_Group is None:
            self.has_changed_Group = 0
        else:
            self.has_changed_Group = has_changed_Group

        if is_added == "" or is_added is None:
            self.is_added = 0
        else:
            self.is_added = is_added

        if is_deleted == "" or is_deleted is None:
            self.is_deleted = 0
        else:
            self.is_deleted = is_deleted


    # comparison operator
    def __cmp__(self, other):
        if self.groupmemberjid == other.groupmemberjid:
                return 0
        return 1


################################################################################
# Smileys conversion function
def convertsmileys_python3 (text):
    newtext = str(text)

    # new emojis
    newtext = newtext.replace('\U0001F0CF', '<img src="data/emoji_new/1F0CF.png" alt=""/>')
    newtext = newtext.replace('\U0001F191', '<img src="data/emoji_new/1F191.png" alt=""/>')
    newtext = newtext.replace('\U0001F193', '<img src="data/emoji_new/1F193.png" alt=""/>')
    newtext = newtext.replace('\U0001F196', '<img src="data/emoji_new/1F196.png" alt=""/>')
    newtext = newtext.replace('\U0001F198', '<img src="data/emoji_new/1F198.png" alt=""/>')
    newtext = newtext.replace('\U0001F232', '<img src="data/emoji_new/1F232.png" alt=""/>')
    newtext = newtext.replace('\U0001F234', '<img src="data/emoji_new/1F234.png" alt=""/>')
    newtext = newtext.replace('\U0001F251', '<img src="data/emoji_new/1F251.png" alt=""/>')
    newtext = newtext.replace('\U0001F301', '<img src="data/emoji_new/1F301.png" alt=""/>')
    newtext = newtext.replace('\U0001F309', '<img src="data/emoji_new/1F309.png" alt=""/>')
    newtext = newtext.replace('\U0001F30B', '<img src="data/emoji_new/1F30B.png" alt=""/>')
    newtext = newtext.replace('\U0001F30C', '<img src="data/emoji_new/1F30C.png" alt=""/>')
    newtext = newtext.replace('\U0001F30D', '<img src="data/emoji_new/1F30D.png" alt=""/>')
    newtext = newtext.replace('\U0001F30E', '<img src="data/emoji_new/1F30E.png" alt=""/>')
    newtext = newtext.replace('\U0001F30F', '<img src="data/emoji_new/1F30F.png" alt=""/>')
    newtext = newtext.replace('\U0001F310', '<img src="data/emoji_new/1F310.png" alt=""/>')
    newtext = newtext.replace('\U0001F311', '<img src="data/emoji_new/1F311.png" alt=""/>')
    newtext = newtext.replace('\U0001F312', '<img src="data/emoji_new/1F312.png" alt=""/>')
    newtext = newtext.replace('\U0001F313', '<img src="data/emoji_new/1F313.png" alt=""/>')
    newtext = newtext.replace('\U0001F314', '<img src="data/emoji_new/1F314.png" alt=""/>')
    newtext = newtext.replace('\U0001F315', '<img src="data/emoji_new/1F315.png" alt=""/>')
    newtext = newtext.replace('\U0001F316', '<img src="data/emoji_new/1F316.png" alt=""/>')
    newtext = newtext.replace('\U0001F317', '<img src="data/emoji_new/1F317.png" alt=""/>')
    newtext = newtext.replace('\U0001F318', '<img src="data/emoji_new/1F318.png" alt=""/>')
    newtext = newtext.replace('\U0001F31A', '<img src="data/emoji_new/1F31A.png" alt=""/>')
    newtext = newtext.replace('\U0001F31B', '<img src="data/emoji_new/1F31B.png" alt=""/>')
    newtext = newtext.replace('\U0001F31C', '<img src="data/emoji_new/1F31C.png" alt=""/>')
    newtext = newtext.replace('\U0001F31D', '<img src="data/emoji_new/1F31D.png" alt=""/>')
    newtext = newtext.replace('\U0001F31E', '<img src="data/emoji_new/1F31E.png" alt=""/>')
    newtext = newtext.replace('\U0001F320', '<img src="data/emoji_new/1F320.png" alt=""/>')
    newtext = newtext.replace('\U0001F330', '<img src="data/emoji_new/1F330.png" alt=""/>')
    newtext = newtext.replace('\U0001F331', '<img src="data/emoji_new/1F331.png" alt=""/>')
    newtext = newtext.replace('\U0001F332', '<img src="data/emoji_new/1F332.png" alt=""/>')
    newtext = newtext.replace('\U0001F333', '<img src="data/emoji_new/1F333.png" alt=""/>')
    newtext = newtext.replace('\U0001F33C', '<img src="data/emoji_new/1F33C.png" alt=""/>')
    newtext = newtext.replace('\U0001F33D', '<img src="data/emoji_new/1F33D.png" alt=""/>')
    newtext = newtext.replace('\U0001F33F', '<img src="data/emoji_new/1F33F.png" alt=""/>')
    newtext = newtext.replace('\U0001F344', '<img src="data/emoji_new/1F344.png" alt=""/>')
    newtext = newtext.replace('\U0001F347', '<img src="data/emoji_new/1F347.png" alt=""/>')
    newtext = newtext.replace('\U0001F348', '<img src="data/emoji_new/1F348.png" alt=""/>')
    newtext = newtext.replace('\U0001F34B', '<img src="data/emoji_new/1F34B.png" alt=""/>')
    newtext = newtext.replace('\U0001F34C', '<img src="data/emoji_new/1F34C.png" alt=""/>')
    newtext = newtext.replace('\U0001F34D', '<img src="data/emoji_new/1F34D.png" alt=""/>')
    newtext = newtext.replace('\U0001F34F', '<img src="data/emoji_new/1F34F.png" alt=""/>')
    newtext = newtext.replace('\U0001F350', '<img src="data/emoji_new/1F350.png" alt=""/>')
    newtext = newtext.replace('\U0001F351', '<img src="data/emoji_new/1F351.png" alt=""/>')
    newtext = newtext.replace('\U0001F352', '<img src="data/emoji_new/1F352.png" alt=""/>')
    newtext = newtext.replace('\U0001F355', '<img src="data/emoji_new/1F355.png" alt=""/>')
    newtext = newtext.replace('\U0001F356', '<img src="data/emoji_new/1F356.png" alt=""/>')
    newtext = newtext.replace('\U0001F357', '<img src="data/emoji_new/1F357.png" alt=""/>')
    newtext = newtext.replace('\U0001F360', '<img src="data/emoji_new/1F360.png" alt=""/>')
    newtext = newtext.replace('\U0001F364', '<img src="data/emoji_new/1F364.png" alt=""/>')
    newtext = newtext.replace('\U0001F365', '<img src="data/emoji_new/1F365.png" alt=""/>')
    newtext = newtext.replace('\U0001F368', '<img src="data/emoji_new/1F368.png" alt=""/>')
    newtext = newtext.replace('\U0001F369', '<img src="data/emoji_new/1F369.png" alt=""/>')
    newtext = newtext.replace('\U0001F36A', '<img src="data/emoji_new/1F36A.png" alt=""/>')
    newtext = newtext.replace('\U0001F36B', '<img src="data/emoji_new/1F36B.png" alt=""/>')
    newtext = newtext.replace('\U0001F36C', '<img src="data/emoji_new/1F36C.png" alt=""/>')
    newtext = newtext.replace('\U0001F36D', '<img src="data/emoji_new/1F36D.png" alt=""/>')
    newtext = newtext.replace('\U0001F36E', '<img src="data/emoji_new/1F36E.png" alt=""/>')
    newtext = newtext.replace('\U0001F36F', '<img src="data/emoji_new/1F36F.png" alt=""/>')
    newtext = newtext.replace('\U0001F377', '<img src="data/emoji_new/1F377.png" alt=""/>')
    newtext = newtext.replace('\U0001F379', '<img src="data/emoji_new/1F379.png" alt=""/>')
    newtext = newtext.replace('\U0001F37C', '<img src="data/emoji_new/1F37C.png" alt=""/>')
    newtext = newtext.replace('\U0001F38A', '<img src="data/emoji_new/1F38A.png" alt=""/>')
    newtext = newtext.replace('\U0001F38B', '<img src="data/emoji_new/1F38B.png" alt=""/>')
    newtext = newtext.replace('\U0001F3A0', '<img src="data/emoji_new/1F3A0.png" alt=""/>')
    newtext = newtext.replace('\U0001F3A3', '<img src="data/emoji_new/1F3A3.png" alt=""/>')
    newtext = newtext.replace('\U0001F3AA', '<img src="data/emoji_new/1F3AA.png" alt=""/>')
    newtext = newtext.replace('\U0001F3AD', '<img src="data/emoji_new/1F3AD.png" alt=""/>')
    newtext = newtext.replace('\U0001F3AE', '<img src="data/emoji_new/1F3AE.png" alt=""/>')
    newtext = newtext.replace('\U0001F3B2', '<img src="data/emoji_new/1F3B2.png" alt=""/>')
    newtext = newtext.replace('\U0001F3B3', '<img src="data/emoji_new/1F3B3.png" alt=""/>')
    newtext = newtext.replace('\U0001F3B4', '<img src="data/emoji_new/1F3B4.png" alt=""/>')
    newtext = newtext.replace('\U0001F3B9', '<img src="data/emoji_new/1F3B9.png" alt=""/>')
    newtext = newtext.replace('\U0001F3BB', '<img src="data/emoji_new/1F3BB.png" alt=""/>')
    newtext = newtext.replace('\U0001F3BC', '<img src="data/emoji_new/1F3BC.png" alt=""/>')
    newtext = newtext.replace('\U0001F3BD', '<img src="data/emoji_new/1F3BD.png" alt=""/>')
    newtext = newtext.replace('\U0001F3C2', '<img src="data/emoji_new/1F3C2.png" alt=""/>')
    newtext = newtext.replace('\U0001F3C7', '<img src="data/emoji_new/1F3C7.png" alt=""/>')
    newtext = newtext.replace('\U0001F3C9', '<img src="data/emoji_new/1F3C9.png" alt=""/>')
    newtext = newtext.replace('\U0001F3E1', '<img src="data/emoji_new/1F3E1.png" alt=""/>')
    newtext = newtext.replace('\U0001F3E4', '<img src="data/emoji_new/1F3E4.png" alt=""/>')
    newtext = newtext.replace('\U0001F3EE', '<img src="data/emoji_new/1F3EE.png" alt=""/>')
    newtext = newtext.replace('\U0001F400', '<img src="data/emoji_new/1F400.png" alt=""/>')
    newtext = newtext.replace('\U0001F401', '<img src="data/emoji_new/1F401.png" alt=""/>')
    newtext = newtext.replace('\U0001F402', '<img src="data/emoji_new/1F402.png" alt=""/>')
    newtext = newtext.replace('\U0001F403', '<img src="data/emoji_new/1F403.png" alt=""/>')
    newtext = newtext.replace('\U0001F404', '<img src="data/emoji_new/1F404.png" alt=""/>')
    newtext = newtext.replace('\U0001F405', '<img src="data/emoji_new/1F405.png" alt=""/>')
    newtext = newtext.replace('\U0001F406', '<img src="data/emoji_new/1F406.png" alt=""/>')
    newtext = newtext.replace('\U0001F407', '<img src="data/emoji_new/1F407.png" alt=""/>')
    newtext = newtext.replace('\U0001F408', '<img src="data/emoji_new/1F408.png" alt=""/>')
    newtext = newtext.replace('\U0001F409', '<img src="data/emoji_new/1F409.png" alt=""/>')
    newtext = newtext.replace('\U0001F40A', '<img src="data/emoji_new/1F40A.png" alt=""/>')
    newtext = newtext.replace('\U0001F40B', '<img src="data/emoji_new/1F40B.png" alt=""/>')
    newtext = newtext.replace('\U0001F40C', '<img src="data/emoji_new/1F40C.png" alt=""/>')
    newtext = newtext.replace('\U0001F40F', '<img src="data/emoji_new/1F40F.png" alt=""/>')
    newtext = newtext.replace('\U0001F410', '<img src="data/emoji_new/1F410.png" alt=""/>')
    newtext = newtext.replace('\U0001F413', '<img src="data/emoji_new/1F413.png" alt=""/>')
    newtext = newtext.replace('\U0001F415', '<img src="data/emoji_new/1F415.png" alt=""/>')
    newtext = newtext.replace('\U0001F416', '<img src="data/emoji_new/1F416.png" alt=""/>')
    newtext = newtext.replace('\U0001F41C', '<img src="data/emoji_new/1F41C.png" alt=""/>')
    newtext = newtext.replace('\U0001F41D', '<img src="data/emoji_new/1F41D.png" alt=""/>')
    newtext = newtext.replace('\U0001F41E', '<img src="data/emoji_new/1F41E.png" alt=""/>')
    newtext = newtext.replace('\U0001F421', '<img src="data/emoji_new/1F421.png" alt=""/>')
    newtext = newtext.replace('\U0001F422', '<img src="data/emoji_new/1F422.png" alt=""/>')
    newtext = newtext.replace('\U0001F423', '<img src="data/emoji_new/1F423.png" alt=""/>')
    newtext = newtext.replace('\U0001F425', '<img src="data/emoji_new/1F425.png" alt=""/>')
    newtext = newtext.replace('\U0001F429', '<img src="data/emoji_new/1F429.png" alt=""/>')
    newtext = newtext.replace('\U0001F42A', '<img src="data/emoji_new/1F42A.png" alt=""/>')
    newtext = newtext.replace('\U0001F432', '<img src="data/emoji_new/1F432.png" alt=""/>')
    newtext = newtext.replace('\U0001F43C', '<img src="data/emoji_new/1F43C.png" alt=""/>')
    newtext = newtext.replace('\U0001F43D', '<img src="data/emoji_new/1F43D.png" alt=""/>')
    newtext = newtext.replace('\U0001F43E', '<img src="data/emoji_new/1F43E.png" alt=""/>')
    newtext = newtext.replace('\U0001F445', '<img src="data/emoji_new/1F445.png" alt=""/>')
    newtext = newtext.replace('\U0001F453', '<img src="data/emoji_new/1F453.png" alt=""/>')
    newtext = newtext.replace('\U0001F456', '<img src="data/emoji_new/1F456.png" alt=""/>')
    newtext = newtext.replace('\U0001F45A', '<img src="data/emoji_new/1F45A.png" alt=""/>')
    newtext = newtext.replace('\U0001F45B', '<img src="data/emoji_new/1F45B.png" alt=""/>')
    newtext = newtext.replace('\U0001F45D', '<img src="data/emoji_new/1F45D.png" alt=""/>')
    newtext = newtext.replace('\U0001F45E', '<img src="data/emoji_new/1F45E.png" alt=""/>')
    newtext = newtext.replace('\U0001F464', '<img src="data/emoji_new/1F464.png" alt=""/>')
    newtext = newtext.replace('\U0001F465', '<img src="data/emoji_new/1F465.png" alt=""/>')
    newtext = newtext.replace('\U0001F46A', '<img src="data/emoji_new/1F46A.png" alt=""/>')
    newtext = newtext.replace('\U0001F46C', '<img src="data/emoji_new/1F46C.png" alt=""/>')
    newtext = newtext.replace('\U0001F46D', '<img src="data/emoji_new/1F46D.png" alt=""/>')
    newtext = newtext.replace('\U0001F470', '<img src="data/emoji_new/1F470.png" alt=""/>')
    newtext = newtext.replace('\U0001F479', '<img src="data/emoji_new/1F479.png" alt=""/>')
    newtext = newtext.replace('\U0001F47A', '<img src="data/emoji_new/1F47A.png" alt=""/>')
    newtext = newtext.replace('\U0001F48C', '<img src="data/emoji_new/1F48C.png" alt=""/>')
    newtext = newtext.replace('\U0001F495', '<img src="data/emoji_new/1F495.png" alt=""/>')
    newtext = newtext.replace('\U0001F496', '<img src="data/emoji_new/1F496.png" alt=""/>')
    newtext = newtext.replace('\U0001F49E', '<img src="data/emoji_new/1F49E.png" alt=""/>')
    newtext = newtext.replace('\U0001F4A0', '<img src="data/emoji_new/1F4A0.png" alt=""/>')
    newtext = newtext.replace('\U0001F4A5', '<img src="data/emoji_new/1F4A5.png" alt=""/>')
    newtext = newtext.replace('\U0001F4A7', '<img src="data/emoji_new/1F4A7.png" alt=""/>')
    newtext = newtext.replace('\U0001F4AB', '<img src="data/emoji_new/1F4AB.png" alt=""/>')
    newtext = newtext.replace('\U0001F4AC', '<img src="data/emoji_new/1F4AC.png" alt=""/>')
    newtext = newtext.replace('\U0001F4AD', '<img src="data/emoji_new/1F4AD.png" alt=""/>')
    newtext = newtext.replace('\U0001F4AE', '<img src="data/emoji_new/1F4AE.png" alt=""/>')
    newtext = newtext.replace('\U0001F4AF', '<img src="data/emoji_new/1F4AF.png" alt=""/>')
    newtext = newtext.replace('\U0001F4B2', '<img src="data/emoji_new/1F4B2.png" alt=""/>')
    newtext = newtext.replace('\U0001F4B3', '<img src="data/emoji_new/1F4B3.png" alt=""/>')
    newtext = newtext.replace('\U0001F4B4', '<img src="data/emoji_new/1F4B4.png" alt=""/>')
    newtext = newtext.replace('\U0001F4B5', '<img src="data/emoji_new/1F4B5.png" alt=""/>')
    newtext = newtext.replace('\U0001F4B6', '<img src="data/emoji_new/1F4B6.png" alt=""/>')
    newtext = newtext.replace('\U0001F4B7', '<img src="data/emoji_new/1F4B7.png" alt=""/>')
    newtext = newtext.replace('\U0001F4B8', '<img src="data/emoji_new/1F4B8.png" alt=""/>')
    newtext = newtext.replace('\U0001F4BE', '<img src="data/emoji_new/1F4BE.png" alt=""/>')
    newtext = newtext.replace('\U0001F4C1', '<img src="data/emoji_new/1F4C1.png" alt=""/>')
    newtext = newtext.replace('\U0001F4C2', '<img src="data/emoji_new/1F4C2.png" alt=""/>')
    newtext = newtext.replace('\U0001F4C3', '<img src="data/emoji_new/1F4C3.png" alt=""/>')
    newtext = newtext.replace('\U0001F4C4', '<img src="data/emoji_new/1F4C4.png" alt=""/>')
    newtext = newtext.replace('\U0001F4C5', '<img src="data/emoji_new/1F4C5.png" alt=""/>')
    newtext = newtext.replace('\U0001F4C6', '<img src="data/emoji_new/1F4C6.png" alt=""/>')
    newtext = newtext.replace('\U0001F4C7', '<img src="data/emoji_new/1F4C7.png" alt=""/>')
    newtext = newtext.replace('\U0001F4C8', '<img src="data/emoji_new/1F4C8.png" alt=""/>')
    newtext = newtext.replace('\U0001F4C9', '<img src="data/emoji_new/1F4C9.png" alt=""/>')
    newtext = newtext.replace('\U0001F4CA', '<img src="data/emoji_new/1F4CA.png" alt=""/>')
    newtext = newtext.replace('\U0001F4CB', '<img src="data/emoji_new/1F4CB.png" alt=""/>')
    newtext = newtext.replace('\U0001F4CC', '<img src="data/emoji_new/1F4CC.png" alt=""/>')
    newtext = newtext.replace('\U0001F4CD', '<img src="data/emoji_new/1F4CD.png" alt=""/>')
    newtext = newtext.replace('\U0001F4CE', '<img src="data/emoji_new/1F4CE.png" alt=""/>')
    newtext = newtext.replace('\U0001F4CF', '<img src="data/emoji_new/1F4CF.png" alt=""/>')
    newtext = newtext.replace('\U0001F4D0', '<img src="data/emoji_new/1F4D0.png" alt=""/>')
    newtext = newtext.replace('\U0001F4D1', '<img src="data/emoji_new/1F4D1.png" alt=""/>')
    newtext = newtext.replace('\U0001F4D2', '<img src="data/emoji_new/1F4D2.png" alt=""/>')
    newtext = newtext.replace('\U0001F4D3', '<img src="data/emoji_new/1F4D3.png" alt=""/>')
    newtext = newtext.replace('\U0001F4D4', '<img src="data/emoji_new/1F4D4.png" alt=""/>')
    newtext = newtext.replace('\U0001F4D5', '<img src="data/emoji_new/1F4D5.png" alt=""/>')
    newtext = newtext.replace('\U0001F4D7', '<img src="data/emoji_new/1F4D7.png" alt=""/>')
    newtext = newtext.replace('\U0001F4D8', '<img src="data/emoji_new/1F4D8.png" alt=""/>')
    newtext = newtext.replace('\U0001F4D9', '<img src="data/emoji_new/1F4D9.png" alt=""/>')
    newtext = newtext.replace('\U0001F4DA', '<img src="data/emoji_new/1F4DA.png" alt=""/>')
    newtext = newtext.replace('\U0001F4DB', '<img src="data/emoji_new/1F4DB.png" alt=""/>')
    newtext = newtext.replace('\U0001F4DC', '<img src="data/emoji_new/1F4DC.png" alt=""/>')
    newtext = newtext.replace('\U0001F4DE', '<img src="data/emoji_new/1F4DE.png" alt=""/>')
    newtext = newtext.replace('\U0001F4DF', '<img src="data/emoji_new/1F4DF.png" alt=""/>')
    newtext = newtext.replace('\U0001F4E4', '<img src="data/emoji_new/1F4E4.png" alt=""/>')
    newtext = newtext.replace('\U0001F4E5', '<img src="data/emoji_new/1F4E5.png" alt=""/>')
    newtext = newtext.replace('\U0001F4E6', '<img src="data/emoji_new/1F4E6.png" alt=""/>')
    newtext = newtext.replace('\U0001F4E7', '<img src="data/emoji_new/1F4E7.png" alt=""/>')
    newtext = newtext.replace('\U0001F4E8', '<img src="data/emoji_new/1F4E8.png" alt=""/>')
    newtext = newtext.replace('\U0001F4EA', '<img src="data/emoji_new/1F4EA.png" alt=""/>')
    newtext = newtext.replace('\U0001F4EC', '<img src="data/emoji_new/1F4EC.png" alt=""/>')
    newtext = newtext.replace('\U0001F4ED', '<img src="data/emoji_new/1F4ED.png" alt=""/>')
    newtext = newtext.replace('\U0001F4EF', '<img src="data/emoji_new/1F4EF.png" alt=""/>')
    newtext = newtext.replace('\U0001F4F0', '<img src="data/emoji_new/1F4F0.png" alt=""/>')
    newtext = newtext.replace('\U0001F4F5', '<img src="data/emoji_new/1F4F5.png" alt=""/>')
    newtext = newtext.replace('\U0001F4F9', '<img src="data/emoji_new/1F4F9.png" alt=""/>')
    newtext = newtext.replace('\U0001F500', '<img src="data/emoji_new/1F500.png" alt=""/>')
    newtext = newtext.replace('\U0001F501', '<img src="data/emoji_new/1F501.png" alt=""/>')
    newtext = newtext.replace('\U0001F502', '<img src="data/emoji_new/1F502.png" alt=""/>')
    newtext = newtext.replace('\U0001F503', '<img src="data/emoji_new/1F503.png" alt=""/>')
    newtext = newtext.replace('\U0001F504', '<img src="data/emoji_new/1F504.png" alt=""/>')
    newtext = newtext.replace('\U0001F505', '<img src="data/emoji_new/1F505.png" alt=""/>')
    newtext = newtext.replace('\U0001F506', '<img src="data/emoji_new/1F506.png" alt=""/>')
    newtext = newtext.replace('\U0001F507', '<img src="data/emoji_new/1F507.png" alt=""/>')
    newtext = newtext.replace('\U0001F508', '<img src="data/emoji_new/1F508.png" alt=""/>')
    newtext = newtext.replace('\U0001F509', '<img src="data/emoji_new/1F509.png" alt=""/>')
    newtext = newtext.replace('\U0001F50B', '<img src="data/emoji_new/1F50B.png" alt=""/>')
    newtext = newtext.replace('\U0001F50C', '<img src="data/emoji_new/1F50C.png" alt=""/>')
    newtext = newtext.replace('\U0001F50E', '<img src="data/emoji_new/1F50E.png" alt=""/>')
    newtext = newtext.replace('\U0001F50F', '<img src="data/emoji_new/1F50F.png" alt=""/>')
    newtext = newtext.replace('\U0001F510', '<img src="data/emoji_new/1F510.png" alt=""/>')
    newtext = newtext.replace('\U0001F515', '<img src="data/emoji_new/1F515.png" alt=""/>')
    newtext = newtext.replace('\U0001F516', '<img src="data/emoji_new/1F516.png" alt=""/>')
    newtext = newtext.replace('\U0001F517', '<img src="data/emoji_new/1F517.png" alt=""/>')
    newtext = newtext.replace('\U0001F518', '<img src="data/emoji_new/1F518.png" alt=""/>')
    newtext = newtext.replace('\U0001F519', '<img src="data/emoji_new/1F519.png" alt=""/>')
    newtext = newtext.replace('\U0001F51A', '<img src="data/emoji_new/1F51A.png" alt=""/>')
    newtext = newtext.replace('\U0001F51B', '<img src="data/emoji_new/1F51B.png" alt=""/>')
    newtext = newtext.replace('\U0001F51C', '<img src="data/emoji_new/1F51C.png" alt=""/>')
    newtext = newtext.replace('\U0001F51F', '<img src="data/emoji_new/1F51F.png" alt=""/>')
    newtext = newtext.replace('\U0001F520', '<img src="data/emoji_new/1F520.png" alt=""/>')
    newtext = newtext.replace('\U0001F521', '<img src="data/emoji_new/1F521.png" alt=""/>')
    newtext = newtext.replace('\U0001F522', '<img src="data/emoji_new/1F522.png" alt=""/>')
    newtext = newtext.replace('\U0001F523', '<img src="data/emoji_new/1F523.png" alt=""/>')
    newtext = newtext.replace('\U0001F524', '<img src="data/emoji_new/1F524.png" alt=""/>')
    newtext = newtext.replace('\U0001F526', '<img src="data/emoji_new/1F526.png" alt=""/>')
    newtext = newtext.replace('\U0001F527', '<img src="data/emoji_new/1F527.png" alt=""/>')
    newtext = newtext.replace('\U0001F529', '<img src="data/emoji_new/1F529.png" alt=""/>')
    newtext = newtext.replace('\U0001F52A', '<img src="data/emoji_new/1F52A.png" alt=""/>')
    newtext = newtext.replace('\U0001F52C', '<img src="data/emoji_new/1F52C.png" alt=""/>')
    newtext = newtext.replace('\U0001F52D', '<img src="data/emoji_new/1F52D.png" alt=""/>')
    newtext = newtext.replace('\U0001F52E', '<img src="data/emoji_new/1F52E.png" alt=""/>')
    newtext = newtext.replace('\U0001F535', '<img src="data/emoji_new/1F535.png" alt=""/>')
    newtext = newtext.replace('\U0001F536', '<img src="data/emoji_new/1F536.png" alt=""/>')
    newtext = newtext.replace('\U0001F537', '<img src="data/emoji_new/1F537.png" alt=""/>')
    newtext = newtext.replace('\U0001F538', '<img src="data/emoji_new/1F538.png" alt=""/>')
    newtext = newtext.replace('\U0001F539', '<img src="data/emoji_new/1F539.png" alt=""/>')
    newtext = newtext.replace('\U0001F53A', '<img src="data/emoji_new/1F53A.png" alt=""/>')
    newtext = newtext.replace('\U0001F53B', '<img src="data/emoji_new/1F53B.png" alt=""/>')
    newtext = newtext.replace('\U0001F53C', '<img src="data/emoji_new/1F53C.png" alt=""/>')
    newtext = newtext.replace('\U0001F53D', '<img src="data/emoji_new/1F53D.png" alt=""/>')
    newtext = newtext.replace('\U0001F55C', '<img src="data/emoji_new/1F55C.png" alt=""/>')
    newtext = newtext.replace('\U0001F55D', '<img src="data/emoji_new/1F55D.png" alt=""/>')
    newtext = newtext.replace('\U0001F55E', '<img src="data/emoji_new/1F55E.png" alt=""/>')
    newtext = newtext.replace('\U0001F55F', '<img src="data/emoji_new/1F55F.png" alt=""/>')
    newtext = newtext.replace('\U0001F560', '<img src="data/emoji_new/1F560.png" alt=""/>')
    newtext = newtext.replace('\U0001F561', '<img src="data/emoji_new/1F561.png" alt=""/>')
    newtext = newtext.replace('\U0001F562', '<img src="data/emoji_new/1F562.png" alt=""/>')
    newtext = newtext.replace('\U0001F563', '<img src="data/emoji_new/1F563.png" alt=""/>')
    newtext = newtext.replace('\U0001F564', '<img src="data/emoji_new/1F564.png" alt=""/>')
    newtext = newtext.replace('\U0001F565', '<img src="data/emoji_new/1F565.png" alt=""/>')
    newtext = newtext.replace('\U0001F566', '<img src="data/emoji_new/1F566.png" alt=""/>')
    newtext = newtext.replace('\U0001F567', '<img src="data/emoji_new/1F567.png" alt=""/>')
    newtext = newtext.replace('\U0001F5FE', '<img src="data/emoji_new/1F5FE.png" alt=""/>')
    newtext = newtext.replace('\U0001F5FF', '<img src="data/emoji_new/1F5FF.png" alt=""/>')
    newtext = newtext.replace('\U0001F600', '<img src="data/emoji_new/1F600.png" alt=""/>')
    newtext = newtext.replace('\U0001F605', '<img src="data/emoji_new/1F605.png" alt=""/>')
    newtext = newtext.replace('\U0001F606', '<img src="data/emoji_new/1F606.png" alt=""/>')
    newtext = newtext.replace('\U0001F607', '<img src="data/emoji_new/1F607.png" alt=""/>')
    newtext = newtext.replace('\U0001F608', '<img src="data/emoji_new/1F608.png" alt=""/>')
    newtext = newtext.replace('\U0001F60B', '<img src="data/emoji_new/1F60B.png" alt=""/>')
    newtext = newtext.replace('\U0001F60E', '<img src="data/emoji_new/1F60E.png" alt=""/>')
    newtext = newtext.replace('\U0001F610', '<img src="data/emoji_new/1F610.png" alt=""/>')
    newtext = newtext.replace('\U0001F611', '<img src="data/emoji_new/1F611.png" alt=""/>')
    newtext = newtext.replace('\U0001F615', '<img src="data/emoji_new/1F615.png" alt=""/>')
    newtext = newtext.replace('\U0001F617', '<img src="data/emoji_new/1F617.png" alt=""/>')
    newtext = newtext.replace('\U0001F619', '<img src="data/emoji_new/1F619.png" alt=""/>')
    newtext = newtext.replace('\U0001F61B', '<img src="data/emoji_new/1F61B.png" alt=""/>')
    newtext = newtext.replace('\U0001F61F', '<img src="data/emoji_new/1F61F.png" alt=""/>')
    newtext = newtext.replace('\U0001F624', '<img src="data/emoji_new/1F624.png" alt=""/>')
    newtext = newtext.replace('\U0001F626', '<img src="data/emoji_new/1F626.png" alt=""/>')
    newtext = newtext.replace('\U0001F627', '<img src="data/emoji_new/1F627.png" alt=""/>')
    newtext = newtext.replace('\U0001F629', '<img src="data/emoji_new/1F629.png" alt=""/>')
    newtext = newtext.replace('\U0001F62B', '<img src="data/emoji_new/1F62B.png" alt=""/>')
    newtext = newtext.replace('\U0001F62C', '<img src="data/emoji_new/1F62C.png" alt=""/>')
    newtext = newtext.replace('\U0001F62E', '<img src="data/emoji_new/1F62E.png" alt=""/>')
    newtext = newtext.replace('\U0001F62F', '<img src="data/emoji_new/1F62F.png" alt=""/>')
    newtext = newtext.replace('\U0001F634', '<img src="data/emoji_new/1F634.png" alt=""/>')
    newtext = newtext.replace('\U0001F635', '<img src="data/emoji_new/1F635.png" alt=""/>')
    newtext = newtext.replace('\U0001F636', '<img src="data/emoji_new/1F636.png" alt=""/>')
    newtext = newtext.replace('\U0001F638', '<img src="data/emoji_new/1F638.png" alt=""/>')
    newtext = newtext.replace('\U0001F639', '<img src="data/emoji_new/1F639.png" alt=""/>')
    newtext = newtext.replace('\U0001F63A', '<img src="data/emoji_new/1F63A.png" alt=""/>')
    newtext = newtext.replace('\U0001F63B', '<img src="data/emoji_new/1F63B.png" alt=""/>')
    newtext = newtext.replace('\U0001F63C', '<img src="data/emoji_new/1F63C.png" alt=""/>')
    newtext = newtext.replace('\U0001F63D', '<img src="data/emoji_new/1F63D.png" alt=""/>')
    newtext = newtext.replace('\U0001F63E', '<img src="data/emoji_new/1F63E.png" alt=""/>')
    newtext = newtext.replace('\U0001F63F', '<img src="data/emoji_new/1F63F.png" alt=""/>')
    newtext = newtext.replace('\U0001F640', '<img src="data/emoji_new/1F640.png" alt=""/>')
    newtext = newtext.replace('\U0001F648', '<img src="data/emoji_new/1F648.png" alt=""/>')
    newtext = newtext.replace('\U0001F649', '<img src="data/emoji_new/1F649.png" alt=""/>')
    newtext = newtext.replace('\U0001F64A', '<img src="data/emoji_new/1F64A.png" alt=""/>')
    newtext = newtext.replace('\U0001F64B', '<img src="data/emoji_new/1F64B.png" alt=""/>')
    newtext = newtext.replace('\U0001F64D', '<img src="data/emoji_new/1F64D.png" alt=""/>')
    newtext = newtext.replace('\U0001F64E', '<img src="data/emoji_new/1F64E.png" alt=""/>')
    newtext = newtext.replace('\U0001F681', '<img src="data/emoji_new/1F681.png" alt=""/>')
    newtext = newtext.replace('\U0001F682', '<img src="data/emoji_new/1F682.png" alt=""/>')
    newtext = newtext.replace('\U0001F686', '<img src="data/emoji_new/1F686.png" alt=""/>')
    newtext = newtext.replace('\U0001F688', '<img src="data/emoji_new/1F688.png" alt=""/>')
    newtext = newtext.replace('\U0001F68A', '<img src="data/emoji_new/1F68A.png" alt=""/>')
    newtext = newtext.replace('\U0001F68B', '<img src="data/emoji_new/1F68B.png" alt=""/>')
    newtext = newtext.replace('\U0001F68D', '<img src="data/emoji_new/1F68D.png" alt=""/>')
    newtext = newtext.replace('\U0001F68E', '<img src="data/emoji_new/1F68E.png" alt=""/>')
    newtext = newtext.replace('\U0001F690', '<img src="data/emoji_new/1F690.png" alt=""/>')
    newtext = newtext.replace('\U0001F694', '<img src="data/emoji_new/1F694.png" alt=""/>')
    newtext = newtext.replace('\U0001F696', '<img src="data/emoji_new/1F696.png" alt=""/>')
    newtext = newtext.replace('\U0001F698', '<img src="data/emoji_new/1F698.png" alt=""/>')
    newtext = newtext.replace('\U0001F69B', '<img src="data/emoji_new/1F69B.png" alt=""/>')
    newtext = newtext.replace('\U0001F69C', '<img src="data/emoji_new/1F69C.png" alt=""/>')
    newtext = newtext.replace('\U0001F69D', '<img src="data/emoji_new/1F69D.png" alt=""/>')
    newtext = newtext.replace('\U0001F69E', '<img src="data/emoji_new/1F69E.png" alt=""/>')
    newtext = newtext.replace('\U0001F69F', '<img src="data/emoji_new/1F69F.png" alt=""/>')
    newtext = newtext.replace('\U0001F6A0', '<img src="data/emoji_new/1F6A0.png" alt=""/>')
    newtext = newtext.replace('\U0001F6A1', '<img src="data/emoji_new/1F6A1.png" alt=""/>')
    newtext = newtext.replace('\U0001F6A3', '<img src="data/emoji_new/1F6A3.png" alt=""/>')
    newtext = newtext.replace('\U0001F6A6', '<img src="data/emoji_new/1F6A6.png" alt=""/>')
    newtext = newtext.replace('\U0001F6A8', '<img src="data/emoji_new/1F6A8.png" alt=""/>')
    newtext = newtext.replace('\U0001F6A9', '<img src="data/emoji_new/1F6A9.png" alt=""/>')
    newtext = newtext.replace('\U0001F6AA', '<img src="data/emoji_new/1F6AA.png" alt=""/>')
    newtext = newtext.replace('\U0001F6AB', '<img src="data/emoji_new/1F6AB.png" alt=""/>')
    newtext = newtext.replace('\U0001F6AE', '<img src="data/emoji_new/1F6AE.png" alt=""/>')
    newtext = newtext.replace('\U0001F6AF', '<img src="data/emoji_new/1F6AF.png" alt=""/>')
    newtext = newtext.replace('\U0001F6B0', '<img src="data/emoji_new/1F6B0.png" alt=""/>')
    newtext = newtext.replace('\U0001F6B1', '<img src="data/emoji_new/1F6B1.png" alt=""/>')
    newtext = newtext.replace('\U0001F6B3', '<img src="data/emoji_new/1F6B3.png" alt=""/>')
    newtext = newtext.replace('\U0001F6B4', '<img src="data/emoji_new/1F6B4.png" alt=""/>')
    newtext = newtext.replace('\U0001F6B5', '<img src="data/emoji_new/1F6B5.png" alt=""/>')
    newtext = newtext.replace('\U0001F6B7', '<img src="data/emoji_new/1F6B7.png" alt=""/>')
    newtext = newtext.replace('\U0001F6B8', '<img src="data/emoji_new/1F6B8.png" alt=""/>')
    newtext = newtext.replace('\U0001F6BF', '<img src="data/emoji_new/1F6BF.png" alt=""/>')
    newtext = newtext.replace('\U0001F6C1', '<img src="data/emoji_new/1F6C1.png" alt=""/>')
    newtext = newtext.replace('\U0001F6C2', '<img src="data/emoji_new/1F6C2.png" alt=""/>')
    newtext = newtext.replace('\U0001F6C3', '<img src="data/emoji_new/1F6C3.png" alt=""/>')
    newtext = newtext.replace('\U0001F6C4', '<img src="data/emoji_new/1F6C4.png" alt=""/>')
    newtext = newtext.replace('\U0001F6C5', '<img src="data/emoji_new/1F6C5.png" alt=""/>')
    newtext = newtext.replace('\u203C', '<img src="data/emoji_new/203C.png" alt=""/>')
    newtext = newtext.replace('\u2049', '<img src="data/emoji_new/2049.png" alt=""/>')
    newtext = newtext.replace('\u2139', '<img src="data/emoji_new/2139.png" alt=""/>')
    newtext = newtext.replace('\u2194', '<img src="data/emoji_new/2194.png" alt=""/>')
    newtext = newtext.replace('\u2195', '<img src="data/emoji_new/2195.png" alt=""/>')
    newtext = newtext.replace('\u21A9', '<img src="data/emoji_new/21A9.png" alt=""/>')
    newtext = newtext.replace('\u21AA', '<img src="data/emoji_new/21AA.png" alt=""/>')
    newtext = newtext.replace('\u231A', '<img src="data/emoji_new/231A.png" alt=""/>')
    newtext = newtext.replace('\u231B', '<img src="data/emoji_new/231B.png" alt=""/>')
    newtext = newtext.replace('\u23EB', '<img src="data/emoji_new/23EB.png" alt=""/>')
    newtext = newtext.replace('\u23EC', '<img src="data/emoji_new/23EC.png" alt=""/>')
    newtext = newtext.replace('\u23F0', '<img src="data/emoji_new/23F0.png" alt=""/>')
    newtext = newtext.replace('\u23F3', '<img src="data/emoji_new/23F3.png" alt=""/>')
    newtext = newtext.replace('\u24C2', '<img src="data/emoji_new/24C2.png" alt=""/>')
    newtext = newtext.replace('\u25AA', '<img src="data/emoji_new/25AA.png" alt=""/>')
    newtext = newtext.replace('\u25AB', '<img src="data/emoji_new/25AB.png" alt=""/>')
    newtext = newtext.replace('\u25FB', '<img src="data/emoji_new/25FB.png" alt=""/>')
    newtext = newtext.replace('\u25FC', '<img src="data/emoji_new/25FC.png" alt=""/>')
    newtext = newtext.replace('\u25FD', '<img src="data/emoji_new/25FD.png" alt=""/>')
    newtext = newtext.replace('\u25FE', '<img src="data/emoji_new/25FE.png" alt=""/>')
    newtext = newtext.replace('\u2611', '<img src="data/emoji_new/2611.png" alt=""/>')
    newtext = newtext.replace('\u267B', '<img src="data/emoji_new/267B.png" alt=""/>')
    newtext = newtext.replace('\u2693', '<img src="data/emoji_new/2693.png" alt=""/>')
    newtext = newtext.replace('\u26AA', '<img src="data/emoji_new/26AA.png" alt=""/>')
    newtext = newtext.replace('\u26AB', '<img src="data/emoji_new/26AB.png" alt=""/>')
    newtext = newtext.replace('\u26C5', '<img src="data/emoji_new/26C5.png" alt=""/>')
    newtext = newtext.replace('\u26D4', '<img src="data/emoji_new/26D4.png" alt=""/>')
    newtext = newtext.replace('\u2705', '<img src="data/emoji_new/2705.png" alt=""/>')
    newtext = newtext.replace('\u2709', '<img src="data/emoji_new/2709.png" alt=""/>')
    newtext = newtext.replace('\u270F', '<img src="data/emoji_new/270F.png" alt=""/>')
    newtext = newtext.replace('\u2712', '<img src="data/emoji_new/2712.png" alt=""/>')
    newtext = newtext.replace('\u2714', '<img src="data/emoji_new/2714.png" alt=""/>')
    newtext = newtext.replace('\u2716', '<img src="data/emoji_new/2716.png" alt=""/>')
    newtext = newtext.replace('\u2744', '<img src="data/emoji_new/2744.png" alt=""/>')
    newtext = newtext.replace('\u2747', '<img src="data/emoji_new/2747.png" alt=""/>')
    newtext = newtext.replace('\u274E', '<img src="data/emoji_new/274E.png" alt=""/>')
    newtext = newtext.replace('\u2795', '<img src="data/emoji_new/2795.png" alt=""/>')
    newtext = newtext.replace('\u2796', '<img src="data/emoji_new/2796.png" alt=""/>')
    newtext = newtext.replace('\u2797', '<img src="data/emoji_new/2797.png" alt=""/>')
    newtext = newtext.replace('\u27B0', '<img src="data/emoji_new/27B0.png" alt=""/>')
    newtext = newtext.replace('\u2934', '<img src="data/emoji_new/2934.png" alt=""/>')
    newtext = newtext.replace('\u2935', '<img src="data/emoji_new/2935.png" alt=""/>')
    newtext = newtext.replace('\u2B1B', '<img src="data/emoji_new/2B1B.png" alt=""/>')
    newtext = newtext.replace('\u2B1C', '<img src="data/emoji_new/2B1C.png" alt=""/>')
    newtext = newtext.replace('\u3030', '<img src="data/emoji_new/3030.png" alt=""/>')

    # old emojis
    newtext = newtext.replace('\ue415', '<img src="data/emoji/e415.png" alt=""/>')
    newtext = newtext.replace('\ue056', '<img src="data/emoji/e056.png" alt=""/>')
    newtext = newtext.replace('\ue057', '<img src="data/emoji/e057.png" alt=""/>')
    newtext = newtext.replace('\ue414', '<img src="data/emoji/e414.png" alt=""/>')
    newtext = newtext.replace('\ue405', '<img src="data/emoji/e405.png" alt=""/>')
    newtext = newtext.replace('\ue106', '<img src="data/emoji/e106.png" alt=""/>')
    newtext = newtext.replace('\ue418', '<img src="data/emoji/e418.png" alt=""/>')

    newtext = newtext.replace('\ue417', '<img src="data/emoji/e417.png" alt=""/>')
    newtext = newtext.replace('\ue40d', '<img src="data/emoji/e40d.png" alt=""/>')
    newtext = newtext.replace('\ue40a', '<img src="data/emoji/e40a.png" alt=""/>')
    newtext = newtext.replace('\ue404', '<img src="data/emoji/e404.png" alt=""/>')
    newtext = newtext.replace('\ue105', '<img src="data/emoji/e105.png" alt=""/>')
    newtext = newtext.replace('\ue409', '<img src="data/emoji/e409.png" alt=""/>')
    newtext = newtext.replace('\ue40e', '<img src="data/emoji/e40e.png" alt=""/>')

    newtext = newtext.replace('\ue402', '<img src="data/emoji/e402.png" alt=""/>')
    newtext = newtext.replace('\ue108', '<img src="data/emoji/e108.png" alt=""/>')
    newtext = newtext.replace('\ue403', '<img src="data/emoji/e403.png" alt=""/>')
    newtext = newtext.replace('\ue058', '<img src="data/emoji/e058.png" alt=""/>')
    newtext = newtext.replace('\ue407', '<img src="data/emoji/e407.png" alt=""/>')
    newtext = newtext.replace('\ue401', '<img src="data/emoji/e401.png" alt=""/>')
    newtext = newtext.replace('\ue40f', '<img src="data/emoji/e40f.png" alt=""/>')

    newtext = newtext.replace('\ue40b', '<img src="data/emoji/e40b.png" alt=""/>')
    newtext = newtext.replace('\ue406', '<img src="data/emoji/e406.png" alt=""/>')
    newtext = newtext.replace('\ue413', '<img src="data/emoji/e413.png" alt=""/>')
    newtext = newtext.replace('\ue411', '<img src="data/emoji/e411.png" alt=""/>')
    newtext = newtext.replace('\ue412', '<img src="data/emoji/e412.png" alt=""/>')
    newtext = newtext.replace('\ue410', '<img src="data/emoji/e410.png" alt=""/>')
    newtext = newtext.replace('\ue107', '<img src="data/emoji/e107.png" alt=""/>')

    newtext = newtext.replace('\ue059', '<img src="data/emoji/e059.png" alt=""/>')
    newtext = newtext.replace('\ue416', '<img src="data/emoji/e416.png" alt=""/>')
    newtext = newtext.replace('\ue408', '<img src="data/emoji/e408.png" alt=""/>')
    newtext = newtext.replace('\ue40c', '<img src="data/emoji/e40c.png" alt=""/>')
    newtext = newtext.replace('\ue11a', '<img src="data/emoji/e11a.png" alt=""/>')
    newtext = newtext.replace('\ue10c', '<img src="data/emoji/e10c.png" alt=""/>')
    newtext = newtext.replace('\ue32c', '<img src="data/emoji/e32c.png" alt=""/>')

    newtext = newtext.replace('\ue32a', '<img src="data/emoji/e32a.png" alt=""/>')
    newtext = newtext.replace('\ue32d', '<img src="data/emoji/e32d.png" alt=""/>')
    newtext = newtext.replace('\ue328', '<img src="data/emoji/e328.png" alt=""/>')
    newtext = newtext.replace('\ue32b', '<img src="data/emoji/e32b.png" alt=""/>')
    newtext = newtext.replace('\ue022', '<img src="data/emoji/e022.png" alt=""/>')
    newtext = newtext.replace('\ue023', '<img src="data/emoji/e023.png" alt=""/>')
    newtext = newtext.replace('\ue327', '<img src="data/emoji/e327.png" alt=""/>')

    newtext = newtext.replace('\ue329', '<img src="data/emoji/e329.png" alt=""/>')
    newtext = newtext.replace('\ue32e', '<img src="data/emoji/e32e.png" alt=""/>')
    newtext = newtext.replace('\ue32f', '<img src="data/emoji/e32f.png" alt=""/>')
    newtext = newtext.replace('\ue335', '<img src="data/emoji/e335.png" alt=""/>')
    newtext = newtext.replace('\ue334', '<img src="data/emoji/e334.png" alt=""/>')
    newtext = newtext.replace('\ue021', '<img src="data/emoji/e021.png" alt=""/>')
    newtext = newtext.replace('\ue337', '<img src="data/emoji/e337.png" alt=""/>')

    newtext = newtext.replace('\ue020', '<img src="data/emoji/e020.png" alt=""/>')
    newtext = newtext.replace('\ue336', '<img src="data/emoji/e336.png" alt=""/>')
    newtext = newtext.replace('\ue13c', '<img src="data/emoji/e13c.png" alt=""/>')
    newtext = newtext.replace('\ue330', '<img src="data/emoji/e330.png" alt=""/>')
    newtext = newtext.replace('\ue331', '<img src="data/emoji/e331.png" alt=""/>')
    newtext = newtext.replace('\ue326', '<img src="data/emoji/e326.png" alt=""/>')
    newtext = newtext.replace('\ue03e', '<img src="data/emoji/e03e.png" alt=""/>')

    newtext = newtext.replace('\ue11d', '<img src="data/emoji/e11d.png" alt=""/>')
    newtext = newtext.replace('\ue05a', '<img src="data/emoji/e05a.png" alt=""/>')
    newtext = newtext.replace('\ue00e', '<img src="data/emoji/e00e.png" alt=""/>')
    newtext = newtext.replace('\ue421', '<img src="data/emoji/e421.png" alt=""/>')
    newtext = newtext.replace('\ue420', '<img src="data/emoji/e420.png" alt=""/>')
    newtext = newtext.replace('\ue00d', '<img src="data/emoji/e00d.png" alt=""/>')
    newtext = newtext.replace('\ue010', '<img src="data/emoji/e010.png" alt=""/>')

    newtext = newtext.replace('\ue011', '<img src="data/emoji/e011.png" alt=""/>')
    newtext = newtext.replace('\ue41e', '<img src="data/emoji/e41e.png" alt=""/>')
    newtext = newtext.replace('\ue012', '<img src="data/emoji/e012.png" alt=""/>')
    newtext = newtext.replace('\ue422', '<img src="data/emoji/e422.png" alt=""/>')
    newtext = newtext.replace('\ue22e', '<img src="data/emoji/e22e.png" alt=""/>')
    newtext = newtext.replace('\ue22f', '<img src="data/emoji/e22f.png" alt=""/>')
    newtext = newtext.replace('\ue231', '<img src="data/emoji/e231.png" alt=""/>')

    newtext = newtext.replace('\ue230', '<img src="data/emoji/e230.png" alt=""/>')
    newtext = newtext.replace('\ue427', '<img src="data/emoji/e427.png" alt=""/>')
    newtext = newtext.replace('\ue41d', '<img src="data/emoji/e41d.png" alt=""/>')
    newtext = newtext.replace('\ue00f', '<img src="data/emoji/e00f.png" alt=""/>')
    newtext = newtext.replace('\ue41f', '<img src="data/emoji/e41f.png" alt=""/>')
    newtext = newtext.replace('\ue14c', '<img src="data/emoji/e14c.png" alt=""/>')
    newtext = newtext.replace('\ue201', '<img src="data/emoji/e201.png" alt=""/>')

    newtext = newtext.replace('\ue115', '<img src="data/emoji/e115.png" alt=""/>')
    newtext = newtext.replace('\ue428', '<img src="data/emoji/e428.png" alt=""/>')
    newtext = newtext.replace('\ue51f', '<img src="data/emoji/e51f.png" alt=""/>')
    newtext = newtext.replace('\ue429', '<img src="data/emoji/e429.png" alt=""/>')
    newtext = newtext.replace('\ue424', '<img src="data/emoji/e424.png" alt=""/>')
    newtext = newtext.replace('\ue423', '<img src="data/emoji/e423.png" alt=""/>')
    newtext = newtext.replace('\ue253', '<img src="data/emoji/e253.png" alt=""/>')

    newtext = newtext.replace('\ue426', '<img src="data/emoji/e426.png" alt=""/>')
    newtext = newtext.replace('\ue111', '<img src="data/emoji/e111.png" alt=""/>')
    newtext = newtext.replace('\ue425', '<img src="data/emoji/e425.png" alt=""/>')
    newtext = newtext.replace('\ue31e', '<img src="data/emoji/e31e.png" alt=""/>')
    newtext = newtext.replace('\ue31f', '<img src="data/emoji/e31f.png" alt=""/>')
    newtext = newtext.replace('\ue31d', '<img src="data/emoji/e31d.png" alt=""/>')
    newtext = newtext.replace('\ue001', '<img src="data/emoji/e001.png" alt=""/>')

    newtext = newtext.replace('\ue002', '<img src="data/emoji/e002.png" alt=""/>')
    newtext = newtext.replace('\ue005', '<img src="data/emoji/e005.png" alt=""/>')
    newtext = newtext.replace('\ue004', '<img src="data/emoji/e004.png" alt=""/>')
    newtext = newtext.replace('\ue51a', '<img src="data/emoji/e51a.png" alt=""/>')
    newtext = newtext.replace('\ue519', '<img src="data/emoji/e519.png" alt=""/>')
    newtext = newtext.replace('\ue518', '<img src="data/emoji/e518.png" alt=""/>')
    newtext = newtext.replace('\ue515', '<img src="data/emoji/e515.png" alt=""/>')

    newtext = newtext.replace('\ue516', '<img src="data/emoji/e516.png" alt=""/>')
    newtext = newtext.replace('\ue517', '<img src="data/emoji/e517.png" alt=""/>')
    newtext = newtext.replace('\ue51b', '<img src="data/emoji/e51b.png" alt=""/>')
    newtext = newtext.replace('\ue152', '<img src="data/emoji/e152.png" alt=""/>')
    newtext = newtext.replace('\ue04e', '<img src="data/emoji/e04e.png" alt=""/>')
    newtext = newtext.replace('\ue51c', '<img src="data/emoji/e51c.png" alt=""/>')
    newtext = newtext.replace('\ue51e', '<img src="data/emoji/e51e.png" alt=""/>')

    newtext = newtext.replace('\ue11c', '<img src="data/emoji/e11c.png" alt=""/>')
    newtext = newtext.replace('\ue536', '<img src="data/emoji/e536.png" alt=""/>')
    newtext = newtext.replace('\ue003', '<img src="data/emoji/e003.png" alt=""/>')
    newtext = newtext.replace('\ue41c', '<img src="data/emoji/e41c.png" alt=""/>')
    newtext = newtext.replace('\ue41b', '<img src="data/emoji/e41b.png" alt=""/>')
    newtext = newtext.replace('\ue419', '<img src="data/emoji/e419.png" alt=""/>')
    newtext = newtext.replace('\ue41a', '<img src="data/emoji/e41a.png" alt=""/>')

    newtext = newtext.replace('\ue04a', '<img src="data/emoji/e04a.png" alt=""/>')
    newtext = newtext.replace('\ue04b', '<img src="data/emoji/e04b.png" alt=""/>')
    newtext = newtext.replace('\ue049', '<img src="data/emoji/e049.png" alt=""/>')
    newtext = newtext.replace('\ue048', '<img src="data/emoji/e048.png" alt=""/>')
    newtext = newtext.replace('\ue04c', '<img src="data/emoji/e04c.png" alt=""/>')
    newtext = newtext.replace('\ue13d', '<img src="data/emoji/e13d.png" alt=""/>')
    newtext = newtext.replace('\ue443', '<img src="data/emoji/e443.png" alt=""/>')

    newtext = newtext.replace('\ue43e', '<img src="data/emoji/e43e.png" alt=""/>')
    newtext = newtext.replace('\ue04f', '<img src="data/emoji/e04f.png" alt=""/>')
    newtext = newtext.replace('\ue052', '<img src="data/emoji/e052.png" alt=""/>')
    newtext = newtext.replace('\ue053', '<img src="data/emoji/e053.png" alt=""/>')
    newtext = newtext.replace('\ue524', '<img src="data/emoji/e524.png" alt=""/>')
    newtext = newtext.replace('\ue52c', '<img src="data/emoji/e52c.png" alt=""/>')
    newtext = newtext.replace('\ue52a', '<img src="data/emoji/e52a.png" alt=""/>')

    newtext = newtext.replace('\ue531', '<img src="data/emoji/e531.png" alt=""/>')
    newtext = newtext.replace('\ue050', '<img src="data/emoji/e050.png" alt=""/>')
    newtext = newtext.replace('\ue527', '<img src="data/emoji/e527.png" alt=""/>')
    newtext = newtext.replace('\ue051', '<img src="data/emoji/e051.png" alt=""/>')
    newtext = newtext.replace('\ue10b', '<img src="data/emoji/e10b.png" alt=""/>')
    newtext = newtext.replace('\ue52b', '<img src="data/emoji/e52b.png" alt=""/>')
    newtext = newtext.replace('\ue52f', '<img src="data/emoji/e52f.png" alt=""/>')

    newtext = newtext.replace('\ue528', '<img src="data/emoji/e528.png" alt=""/>')
    newtext = newtext.replace('\ue01a', '<img src="data/emoji/e01a.png" alt=""/>')
    newtext = newtext.replace('\ue134', '<img src="data/emoji/e134.png" alt=""/>')
    newtext = newtext.replace('\ue530', '<img src="data/emoji/e530.png" alt=""/>')
    newtext = newtext.replace('\ue529', '<img src="data/emoji/e529.png" alt=""/>')
    newtext = newtext.replace('\ue526', '<img src="data/emoji/e526.png" alt=""/>')
    newtext = newtext.replace('\ue52d', '<img src="data/emoji/e52d.png" alt=""/>')

    newtext = newtext.replace('\ue521', '<img src="data/emoji/e521.png" alt=""/>')
    newtext = newtext.replace('\ue523', '<img src="data/emoji/e523.png" alt=""/>')
    newtext = newtext.replace('\ue52e', '<img src="data/emoji/e52e.png" alt=""/>')
    newtext = newtext.replace('\ue055', '<img src="data/emoji/e055.png" alt=""/>')
    newtext = newtext.replace('\ue525', '<img src="data/emoji/e525.png" alt=""/>')
    newtext = newtext.replace('\ue10a', '<img src="data/emoji/e10a.png" alt=""/>')
    newtext = newtext.replace('\ue109', '<img src="data/emoji/e109.png" alt=""/>')

    newtext = newtext.replace('\ue522', '<img src="data/emoji/e522.png" alt=""/>')
    newtext = newtext.replace('\ue019', '<img src="data/emoji/e019.png" alt=""/>')
    newtext = newtext.replace('\ue054', '<img src="data/emoji/e054.png" alt=""/>')
    newtext = newtext.replace('\ue520', '<img src="data/emoji/e520.png" alt=""/>')
    newtext = newtext.replace('\ue306', '<img src="data/emoji/e306.png" alt=""/>')
    newtext = newtext.replace('\ue030', '<img src="data/emoji/e030.png" alt=""/>')
    newtext = newtext.replace('\ue304', '<img src="data/emoji/e304.png" alt=""/>')

    newtext = newtext.replace('\ue110', '<img src="data/emoji/e110.png" alt=""/>')
    newtext = newtext.replace('\ue032', '<img src="data/emoji/e032.png" alt=""/>')
    newtext = newtext.replace('\ue305', '<img src="data/emoji/e305.png" alt=""/>')
    newtext = newtext.replace('\ue303', '<img src="data/emoji/e303.png" alt=""/>')
    newtext = newtext.replace('\ue118', '<img src="data/emoji/e118.png" alt=""/>')
    newtext = newtext.replace('\ue447', '<img src="data/emoji/e447.png" alt=""/>')
    newtext = newtext.replace('\ue119', '<img src="data/emoji/e119.png" alt=""/>')

    newtext = newtext.replace('\ue307', '<img src="data/emoji/e307.png" alt=""/>')
    newtext = newtext.replace('\ue308', '<img src="data/emoji/e308.png" alt=""/>')
    newtext = newtext.replace('\ue444', '<img src="data/emoji/e444.png" alt=""/>')
    newtext = newtext.replace('\ue441', '<img src="data/emoji/e441.png" alt=""/>')

    newtext = newtext.replace('\ue436', '<img src="data/emoji/e436.png" alt=""/>')
    newtext = newtext.replace('\ue437', '<img src="data/emoji/e437.png" alt=""/>')
    newtext = newtext.replace('\ue438', '<img src="data/emoji/e438.png" alt=""/>')
    newtext = newtext.replace('\ue43a', '<img src="data/emoji/e43a.png" alt=""/>')
    newtext = newtext.replace('\ue439', '<img src="data/emoji/e439.png" alt=""/>')
    newtext = newtext.replace('\ue43b', '<img src="data/emoji/e43b.png" alt=""/>')
    newtext = newtext.replace('\ue117', '<img src="data/emoji/e117.png" alt=""/>')

    newtext = newtext.replace('\ue440', '<img src="data/emoji/e440.png" alt=""/>')
    newtext = newtext.replace('\ue442', '<img src="data/emoji/e442.png" alt=""/>')
    newtext = newtext.replace('\ue446', '<img src="data/emoji/e446.png" alt=""/>')
    newtext = newtext.replace('\ue445', '<img src="data/emoji/e445.png" alt=""/>')
    newtext = newtext.replace('\ue11b', '<img src="data/emoji/e11b.png" alt=""/>')
    newtext = newtext.replace('\ue448', '<img src="data/emoji/e448.png" alt=""/>')
    newtext = newtext.replace('\ue033', '<img src="data/emoji/e033.png" alt=""/>')

    newtext = newtext.replace('\ue112', '<img src="data/emoji/e112.png" alt=""/>')
    newtext = newtext.replace('\ue325', '<img src="data/emoji/e325.png" alt=""/>')
    newtext = newtext.replace('\ue312', '<img src="data/emoji/e312.png" alt=""/>')
    newtext = newtext.replace('\ue310', '<img src="data/emoji/e310.png" alt=""/>')
    newtext = newtext.replace('\ue126', '<img src="data/emoji/e126.png" alt=""/>')
    newtext = newtext.replace('\ue127', '<img src="data/emoji/e127.png" alt=""/>')
    newtext = newtext.replace('\ue008', '<img src="data/emoji/e008.png" alt=""/>')

    newtext = newtext.replace('\ue03d', '<img src="data/emoji/e03d.png" alt=""/>')
    newtext = newtext.replace('\ue00c', '<img src="data/emoji/e00c.png" alt=""/>')
    newtext = newtext.replace('\ue12a', '<img src="data/emoji/e12a.png" alt=""/>')
    newtext = newtext.replace('\ue00a', '<img src="data/emoji/e00a.png" alt=""/>')
    newtext = newtext.replace('\ue00b', '<img src="data/emoji/e00b.png" alt=""/>')
    newtext = newtext.replace('\ue009', '<img src="data/emoji/e009.png" alt=""/>')
    newtext = newtext.replace('\ue316', '<img src="data/emoji/e316.png" alt=""/>')

    newtext = newtext.replace('\ue129', '<img src="data/emoji/e129.png" alt=""/>')
    newtext = newtext.replace('\ue141', '<img src="data/emoji/e141.png" alt=""/>')
    newtext = newtext.replace('\ue142', '<img src="data/emoji/e142.png" alt=""/>')
    newtext = newtext.replace('\ue317', '<img src="data/emoji/e317.png" alt=""/>')
    newtext = newtext.replace('\ue128', '<img src="data/emoji/e128.png" alt=""/>')
    newtext = newtext.replace('\ue14b', '<img src="data/emoji/e14b.png" alt=""/>')
    newtext = newtext.replace('\ue211', '<img src="data/emoji/e211.png" alt=""/>')

    newtext = newtext.replace('\ue114', '<img src="data/emoji/e114.png" alt=""/>')
    newtext = newtext.replace('\ue145', '<img src="data/emoji/e145.png" alt=""/>')
    newtext = newtext.replace('\ue144', '<img src="data/emoji/e144.png" alt=""/>')
    newtext = newtext.replace('\ue03f', '<img src="data/emoji/e03f.png" alt=""/>')
    newtext = newtext.replace('\ue313', '<img src="data/emoji/e313.png" alt=""/>')
    newtext = newtext.replace('\ue116', '<img src="data/emoji/e116.png" alt=""/>')
    newtext = newtext.replace('\ue10f', '<img src="data/emoji/e10f.png" alt=""/>')

    newtext = newtext.replace('\ue104', '<img src="data/emoji/e104.png" alt=""/>')
    newtext = newtext.replace('\ue103', '<img src="data/emoji/e103.png" alt=""/>')
    newtext = newtext.replace('\ue101', '<img src="data/emoji/e101.png" alt=""/>')
    newtext = newtext.replace('\ue102', '<img src="data/emoji/e102.png" alt=""/>')
    newtext = newtext.replace('\ue13f', '<img src="data/emoji/e13f.png" alt=""/>')
    newtext = newtext.replace('\ue140', '<img src="data/emoji/e140.png" alt=""/>')
    newtext = newtext.replace('\ue11f', '<img src="data/emoji/e11f.png" alt=""/>')

    newtext = newtext.replace('\ue12f', '<img src="data/emoji/e12f.png" alt=""/>')
    newtext = newtext.replace('\ue031', '<img src="data/emoji/e031.png" alt=""/>')
    newtext = newtext.replace('\ue30e', '<img src="data/emoji/e30e.png" alt=""/>')
    newtext = newtext.replace('\ue311', '<img src="data/emoji/e311.png" alt=""/>')
    newtext = newtext.replace('\ue113', '<img src="data/emoji/e113.png" alt=""/>')
    newtext = newtext.replace('\ue30f', '<img src="data/emoji/e30f.png" alt=""/>')
    newtext = newtext.replace('\ue13b', '<img src="data/emoji/e13b.png" alt=""/>')

    newtext = newtext.replace('\ue42b', '<img src="data/emoji/e42b.png" alt=""/>')
    newtext = newtext.replace('\ue42a', '<img src="data/emoji/e42a.png" alt=""/>')
    newtext = newtext.replace('\ue018', '<img src="data/emoji/e018.png" alt=""/>')
    newtext = newtext.replace('\ue016', '<img src="data/emoji/e016.png" alt=""/>')
    newtext = newtext.replace('\ue015', '<img src="data/emoji/e015.png" alt=""/>')
    newtext = newtext.replace('\ue014', '<img src="data/emoji/e014.png" alt=""/>')
    newtext = newtext.replace('\ue42c', '<img src="data/emoji/e42c.png" alt=""/>')

    newtext = newtext.replace('\ue42d', '<img src="data/emoji/e42d.png" alt=""/>')
    newtext = newtext.replace('\ue017', '<img src="data/emoji/e017.png" alt=""/>')
    newtext = newtext.replace('\ue013', '<img src="data/emoji/e013.png" alt=""/>')
    newtext = newtext.replace('\ue20e', '<img src="data/emoji/e20e.png" alt=""/>')
    newtext = newtext.replace('\ue20c', '<img src="data/emoji/e20c.png" alt=""/>')
    newtext = newtext.replace('\ue20f', '<img src="data/emoji/e20f.png" alt=""/>')
    newtext = newtext.replace('\ue20d', '<img src="data/emoji/e20d.png" alt=""/>')

    newtext = newtext.replace('\ue131', '<img src="data/emoji/e131.png" alt=""/>')
    newtext = newtext.replace('\ue12b', '<img src="data/emoji/e12b.png" alt=""/>')
    newtext = newtext.replace('\ue130', '<img src="data/emoji/e130.png" alt=""/>')
    newtext = newtext.replace('\ue12d', '<img src="data/emoji/e12d.png" alt=""/>')
    newtext = newtext.replace('\ue324', '<img src="data/emoji/e324.png" alt=""/>')
    newtext = newtext.replace('\ue301', '<img src="data/emoji/e301.png" alt=""/>')
    newtext = newtext.replace('\ue148', '<img src="data/emoji/e148.png" alt=""/>')

    newtext = newtext.replace('\ue502', '<img src="data/emoji/e502.png" alt=""/>')
    newtext = newtext.replace('\ue03c', '<img src="data/emoji/e03c.png" alt=""/>')
    newtext = newtext.replace('\ue30a', '<img src="data/emoji/e30a.png" alt=""/>')
    newtext = newtext.replace('\ue042', '<img src="data/emoji/e042.png" alt=""/>')
    newtext = newtext.replace('\ue040', '<img src="data/emoji/e040.png" alt=""/>')
    newtext = newtext.replace('\ue041', '<img src="data/emoji/e041.png" alt=""/>')
    newtext = newtext.replace('\ue12c', '<img src="data/emoji/e12c.png" alt=""/>')

    newtext = newtext.replace('\ue007', '<img src="data/emoji/e007.png" alt=""/>')
    newtext = newtext.replace('\ue31a', '<img src="data/emoji/e31a.png" alt=""/>')
    newtext = newtext.replace('\ue13e', '<img src="data/emoji/e13e.png" alt=""/>')
    newtext = newtext.replace('\ue31b', '<img src="data/emoji/e31b.png" alt=""/>')
    newtext = newtext.replace('\ue006', '<img src="data/emoji/e006.png" alt=""/>')
    newtext = newtext.replace('\ue302', '<img src="data/emoji/e302.png" alt=""/>')
    newtext = newtext.replace('\ue319', '<img src="data/emoji/e319.png" alt=""/>')

    newtext = newtext.replace('\ue321', '<img src="data/emoji/e321.png" alt=""/>')
    newtext = newtext.replace('\ue322', '<img src="data/emoji/e322.png" alt=""/>')
    newtext = newtext.replace('\ue314', '<img src="data/emoji/e314.png" alt=""/>')
    newtext = newtext.replace('\ue503', '<img src="data/emoji/e503.png" alt=""/>')
    newtext = newtext.replace('\ue10e', '<img src="data/emoji/e10e.png" alt=""/>')
    newtext = newtext.replace('\ue318', '<img src="data/emoji/e318.png" alt=""/>')
    newtext = newtext.replace('\ue43c', '<img src="data/emoji/e43c.png" alt=""/>')

    newtext = newtext.replace('\ue11e', '<img src="data/emoji/e11e.png" alt=""/>')
    newtext = newtext.replace('\ue323', '<img src="data/emoji/e323.png" alt=""/>')
    newtext = newtext.replace('\ue31c', '<img src="data/emoji/e31c.png" alt=""/>')
    newtext = newtext.replace('\ue034', '<img src="data/emoji/e034.png" alt=""/>')
    newtext = newtext.replace('\ue035', '<img src="data/emoji/e035.png" alt=""/>')
    newtext = newtext.replace('\ue045', '<img src="data/emoji/e045.png" alt=""/>')
    newtext = newtext.replace('\ue338', '<img src="data/emoji/e338.png" alt=""/>')

    newtext = newtext.replace('\ue047', '<img src="data/emoji/e047.png" alt=""/>')
    newtext = newtext.replace('\ue30c', '<img src="data/emoji/e30c.png" alt=""/>')
    newtext = newtext.replace('\ue044', '<img src="data/emoji/e044.png" alt=""/>')
    newtext = newtext.replace('\ue30b', '<img src="data/emoji/e30b.png" alt=""/>')
    newtext = newtext.replace('\ue043', '<img src="data/emoji/e043.png" alt=""/>')
    newtext = newtext.replace('\ue120', '<img src="data/emoji/e120.png" alt=""/>')
    newtext = newtext.replace('\ue33b', '<img src="data/emoji/e33b.png" alt=""/>')

    newtext = newtext.replace('\ue33f', '<img src="data/emoji/e33f.png" alt=""/>')
    newtext = newtext.replace('\ue341', '<img src="data/emoji/e341.png" alt=""/>')
    newtext = newtext.replace('\ue34c', '<img src="data/emoji/e34c.png" alt=""/>')
    newtext = newtext.replace('\ue344', '<img src="data/emoji/e344.png" alt=""/>')
    newtext = newtext.replace('\ue342', '<img src="data/emoji/e342.png" alt=""/>')
    newtext = newtext.replace('\ue33d', '<img src="data/emoji/e33d.png" alt=""/>')
    newtext = newtext.replace('\ue33e', '<img src="data/emoji/e33e.png" alt=""/>')

    newtext = newtext.replace('\ue340', '<img src="data/emoji/e340.png" alt=""/>')
    newtext = newtext.replace('\ue34d', '<img src="data/emoji/e34d.png" alt=""/>')
    newtext = newtext.replace('\ue339', '<img src="data/emoji/e339.png" alt=""/>')
    newtext = newtext.replace('\ue147', '<img src="data/emoji/e147.png" alt=""/>')
    newtext = newtext.replace('\ue343', '<img src="data/emoji/e343.png" alt=""/>')
    newtext = newtext.replace('\ue33c', '<img src="data/emoji/e33c.png" alt=""/>')
    newtext = newtext.replace('\ue33a', '<img src="data/emoji/e33a.png" alt=""/>')

    newtext = newtext.replace('\ue43f', '<img src="data/emoji/e43f.png" alt=""/>')
    newtext = newtext.replace('\ue34b', '<img src="data/emoji/e34b.png" alt=""/>')
    newtext = newtext.replace('\ue046', '<img src="data/emoji/e046.png" alt=""/>')
    newtext = newtext.replace('\ue345', '<img src="data/emoji/e345.png" alt=""/>')
    newtext = newtext.replace('\ue346', '<img src="data/emoji/e346.png" alt=""/>')
    newtext = newtext.replace('\ue348', '<img src="data/emoji/e348.png" alt=""/>')
    newtext = newtext.replace('\ue347', '<img src="data/emoji/e347.png" alt=""/>')

    newtext = newtext.replace('\ue34a', '<img src="data/emoji/e34a.png" alt=""/>')
    newtext = newtext.replace('\ue349', '<img src="data/emoji/e349.png" alt=""/>')

    newtext = newtext.replace('\ue036', '<img src="data/emoji/e036.png" alt=""/>')
    newtext = newtext.replace('\ue157', '<img src="data/emoji/e157.png" alt=""/>')
    newtext = newtext.replace('\ue038', '<img src="data/emoji/e038.png" alt=""/>')
    newtext = newtext.replace('\ue153', '<img src="data/emoji/e153.png" alt=""/>')
    newtext = newtext.replace('\ue155', '<img src="data/emoji/e155.png" alt=""/>')
    newtext = newtext.replace('\ue14d', '<img src="data/emoji/e14d.png" alt=""/>')
    newtext = newtext.replace('\ue156', '<img src="data/emoji/e156.png" alt=""/>')

    newtext = newtext.replace('\ue501', '<img src="data/emoji/e501.png" alt=""/>')
    newtext = newtext.replace('\ue158', '<img src="data/emoji/e158.png" alt=""/>')
    newtext = newtext.replace('\ue43d', '<img src="data/emoji/e43d.png" alt=""/>')
    newtext = newtext.replace('\ue037', '<img src="data/emoji/e037.png" alt=""/>')
    newtext = newtext.replace('\ue504', '<img src="data/emoji/e504.png" alt=""/>')
    newtext = newtext.replace('\ue44a', '<img src="data/emoji/e44a.png" alt=""/>')
    newtext = newtext.replace('\ue146', '<img src="data/emoji/e146.png" alt=""/>')

    newtext = newtext.replace('\ue50a', '<img src="data/emoji/e50a.png" alt=""/>')
    newtext = newtext.replace('\ue505', '<img src="data/emoji/e505.png" alt=""/>')
    newtext = newtext.replace('\ue506', '<img src="data/emoji/e506.png" alt=""/>')
    newtext = newtext.replace('\ue122', '<img src="data/emoji/e122.png" alt=""/>')
    newtext = newtext.replace('\ue508', '<img src="data/emoji/e508.png" alt=""/>')
    newtext = newtext.replace('\ue509', '<img src="data/emoji/e509.png" alt=""/>')
    newtext = newtext.replace('\ue03b', '<img src="data/emoji/e03b.png" alt=""/>')

    newtext = newtext.replace('\ue04d', '<img src="data/emoji/e04d.png" alt=""/>')
    newtext = newtext.replace('\ue449', '<img src="data/emoji/e449.png" alt=""/>')
    newtext = newtext.replace('\ue44b', '<img src="data/emoji/e44b.png" alt=""/>')
    newtext = newtext.replace('\ue51d', '<img src="data/emoji/e51d.png" alt=""/>')
    newtext = newtext.replace('\ue44c', '<img src="data/emoji/e44c.png" alt=""/>')
    newtext = newtext.replace('\ue124', '<img src="data/emoji/e124.png" alt=""/>')
    newtext = newtext.replace('\ue121', '<img src="data/emoji/e121.png" alt=""/>')

    newtext = newtext.replace('\ue433', '<img src="data/emoji/e433.png" alt=""/>')
    newtext = newtext.replace('\ue202', '<img src="data/emoji/e202.png" alt=""/>')
    newtext = newtext.replace('\ue135', '<img src="data/emoji/e135.png" alt=""/>')
    newtext = newtext.replace('\ue01c', '<img src="data/emoji/e01c.png" alt=""/>')
    newtext = newtext.replace('\ue01d', '<img src="data/emoji/e01d.png" alt=""/>')
    newtext = newtext.replace('\ue10d', '<img src="data/emoji/e10d.png" alt=""/>')
    newtext = newtext.replace('\ue136', '<img src="data/emoji/e136.png" alt=""/>')

    newtext = newtext.replace('\ue42e', '<img src="data/emoji/e42e.png" alt=""/>')
    newtext = newtext.replace('\ue01b', '<img src="data/emoji/e01b.png" alt=""/>')
    newtext = newtext.replace('\ue15a', '<img src="data/emoji/e15a.png" alt=""/>')
    newtext = newtext.replace('\ue159', '<img src="data/emoji/e159.png" alt=""/>')
    newtext = newtext.replace('\ue432', '<img src="data/emoji/e432.png" alt=""/>')
    newtext = newtext.replace('\ue430', '<img src="data/emoji/e430.png" alt=""/>')
    newtext = newtext.replace('\ue431', '<img src="data/emoji/e431.png" alt=""/>')

    newtext = newtext.replace('\ue42f', '<img src="data/emoji/e42f.png" alt=""/>')
    newtext = newtext.replace('\ue01e', '<img src="data/emoji/e01e.png" alt=""/>')
    newtext = newtext.replace('\ue039', '<img src="data/emoji/e039.png" alt=""/>')
    newtext = newtext.replace('\ue435', '<img src="data/emoji/e435.png" alt=""/>')
    newtext = newtext.replace('\ue01f', '<img src="data/emoji/e01f.png" alt=""/>')
    newtext = newtext.replace('\ue125', '<img src="data/emoji/e125.png" alt=""/>')
    newtext = newtext.replace('\ue03a', '<img src="data/emoji/e03a.png" alt=""/>')

    newtext = newtext.replace('\ue14e', '<img src="data/emoji/e14e.png" alt=""/>')
    newtext = newtext.replace('\ue252', '<img src="data/emoji/e252.png" alt=""/>')
    newtext = newtext.replace('\ue137', '<img src="data/emoji/e137.png" alt=""/>')
    newtext = newtext.replace('\ue209', '<img src="data/emoji/e209.png" alt=""/>')
    newtext = newtext.replace('\ue154', '<img src="data/emoji/e154.png" alt=""/>')
    newtext = newtext.replace('\ue133', '<img src="data/emoji/e133.png" alt=""/>')
    newtext = newtext.replace('\ue150', '<img src="data/emoji/e150.png" alt=""/>')

    newtext = newtext.replace('\ue320', '<img src="data/emoji/e320.png" alt=""/>')
    newtext = newtext.replace('\ue123', '<img src="data/emoji/e123.png" alt=""/>')
    newtext = newtext.replace('\ue132', '<img src="data/emoji/e132.png" alt=""/>')
    newtext = newtext.replace('\ue143', '<img src="data/emoji/e143.png" alt=""/>')
    newtext = newtext.replace('\ue50b', '<img src="data/emoji/e50b.png" alt=""/>')
    newtext = newtext.replace('\ue514', '<img src="data/emoji/e514.png" alt=""/>')
    newtext = newtext.replace('\ue513', '<img src="data/emoji/e513.png" alt=""/>')

    newtext = newtext.replace('\ue50c', '<img src="data/emoji/e50c.png" alt=""/>')
    newtext = newtext.replace('\ue50d', '<img src="data/emoji/e50d.png" alt=""/>')
    newtext = newtext.replace('\ue511', '<img src="data/emoji/e511.png" alt=""/>')
    newtext = newtext.replace('\ue50f', '<img src="data/emoji/e50f.png" alt=""/>')
    newtext = newtext.replace('\ue512', '<img src="data/emoji/e512.png" alt=""/>')
    newtext = newtext.replace('\ue510', '<img src="data/emoji/e510.png" alt=""/>')
    newtext = newtext.replace('\ue50e', '<img src="data/emoji/e50e.png" alt=""/>')

    newtext = newtext.replace('\ue21c', '<img src="data/emoji/e21c.png" alt=""/>')
    newtext = newtext.replace('\ue21d', '<img src="data/emoji/e21d.png" alt=""/>')
    newtext = newtext.replace('\ue21e', '<img src="data/emoji/e21e.png" alt=""/>')
    newtext = newtext.replace('\ue21f', '<img src="data/emoji/e21f.png" alt=""/>')
    newtext = newtext.replace('\ue220', '<img src="data/emoji/e220.png" alt=""/>')
    newtext = newtext.replace('\ue221', '<img src="data/emoji/e221.png" alt=""/>')
    newtext = newtext.replace('\ue222', '<img src="data/emoji/e222.png" alt=""/>')

    newtext = newtext.replace('\ue223', '<img src="data/emoji/e223.png" alt=""/>')
    newtext = newtext.replace('\ue224', '<img src="data/emoji/e224.png" alt=""/>')
    newtext = newtext.replace('\ue225', '<img src="data/emoji/e225.png" alt=""/>')
    newtext = newtext.replace('\ue210', '<img src="data/emoji/e210.png" alt=""/>')
    newtext = newtext.replace('\ue232', '<img src="data/emoji/e232.png" alt=""/>')
    newtext = newtext.replace('\ue233', '<img src="data/emoji/e233.png" alt=""/>')
    newtext = newtext.replace('\ue235', '<img src="data/emoji/e235.png" alt=""/>')

    newtext = newtext.replace('\ue234', '<img src="data/emoji/e234.png" alt=""/>')
    newtext = newtext.replace('\ue236', '<img src="data/emoji/e236.png" alt=""/>')
    newtext = newtext.replace('\ue237', '<img src="data/emoji/e237.png" alt=""/>')
    newtext = newtext.replace('\ue238', '<img src="data/emoji/e238.png" alt=""/>')
    newtext = newtext.replace('\ue239', '<img src="data/emoji/e239.png" alt=""/>')
    newtext = newtext.replace('\ue23b', '<img src="data/emoji/e23b.png" alt=""/>')
    newtext = newtext.replace('\ue23a', '<img src="data/emoji/e23a.png" alt=""/>')

    newtext = newtext.replace('\ue23d', '<img src="data/emoji/e23d.png" alt=""/>')
    newtext = newtext.replace('\ue23c', '<img src="data/emoji/e23c.png" alt=""/>')
    newtext = newtext.replace('\ue24d', '<img src="data/emoji/e24d.png" alt=""/>')
    newtext = newtext.replace('\ue212', '<img src="data/emoji/e212.png" alt=""/>')
    newtext = newtext.replace('\ue24c', '<img src="data/emoji/e24c.png" alt=""/>')
    newtext = newtext.replace('\ue213', '<img src="data/emoji/e213.png" alt=""/>')
    newtext = newtext.replace('\ue214', '<img src="data/emoji/e214.png" alt=""/>')

    newtext = newtext.replace('\ue507', '<img src="data/emoji/e507.png" alt=""/>')
    newtext = newtext.replace('\ue203', '<img src="data/emoji/e203.png" alt=""/>')
    newtext = newtext.replace('\ue20b', '<img src="data/emoji/e20b.png" alt=""/>')
    newtext = newtext.replace('\ue22a', '<img src="data/emoji/e22a.png" alt=""/>')
    newtext = newtext.replace('\ue22b', '<img src="data/emoji/e22b.png" alt=""/>')
    newtext = newtext.replace('\ue226', '<img src="data/emoji/e226.png" alt=""/>')
    newtext = newtext.replace('\ue227', '<img src="data/emoji/e227.png" alt=""/>')

    newtext = newtext.replace('\ue22c', '<img src="data/emoji/e22c.png" alt=""/>')
    newtext = newtext.replace('\ue22d', '<img src="data/emoji/e22d.png" alt=""/>')
    newtext = newtext.replace('\ue215', '<img src="data/emoji/e215.png" alt=""/>')
    newtext = newtext.replace('\ue216', '<img src="data/emoji/e216.png" alt=""/>')
    newtext = newtext.replace('\ue217', '<img src="data/emoji/e217.png" alt=""/>')
    newtext = newtext.replace('\ue218', '<img src="data/emoji/e218.png" alt=""/>')
    newtext = newtext.replace('\ue228', '<img src="data/emoji/e228.png" alt=""/>')

    newtext = newtext.replace('\ue151', '<img src="data/emoji/e151.png" alt=""/>')
    newtext = newtext.replace('\ue138', '<img src="data/emoji/e138.png" alt=""/>')
    newtext = newtext.replace('\ue139', '<img src="data/emoji/e139.png" alt=""/>')
    newtext = newtext.replace('\ue13a', '<img src="data/emoji/e13a.png" alt=""/>')
    newtext = newtext.replace('\ue208', '<img src="data/emoji/e208.png" alt=""/>')
    newtext = newtext.replace('\ue14f', '<img src="data/emoji/e14f.png" alt=""/>')
    newtext = newtext.replace('\ue20a', '<img src="data/emoji/e20a.png" alt=""/>')

    newtext = newtext.replace('\ue434', '<img src="data/emoji/e434.png" alt=""/>')
    newtext = newtext.replace('\ue309', '<img src="data/emoji/e309.png" alt=""/>')
    newtext = newtext.replace('\ue315', '<img src="data/emoji/e315.png" alt=""/>')
    newtext = newtext.replace('\ue30d', '<img src="data/emoji/e30d.png" alt=""/>')
    newtext = newtext.replace('\ue207', '<img src="data/emoji/e207.png" alt=""/>')
    newtext = newtext.replace('\ue229', '<img src="data/emoji/e229.png" alt=""/>')
    newtext = newtext.replace('\ue206', '<img src="data/emoji/e206.png" alt=""/>')

    newtext = newtext.replace('\ue205', '<img src="data/emoji/e205.png" alt=""/>')
    newtext = newtext.replace('\ue204', '<img src="data/emoji/e204.png" alt=""/>')
    newtext = newtext.replace('\ue12e', '<img src="data/emoji/e12e.png" alt=""/>')
    newtext = newtext.replace('\ue250', '<img src="data/emoji/e250.png" alt=""/>')
    newtext = newtext.replace('\ue251', '<img src="data/emoji/e251.png" alt=""/>')
    newtext = newtext.replace('\ue14a', '<img src="data/emoji/e14a.png" alt=""/>')
    newtext = newtext.replace('\ue149', '<img src="data/emoji/e149.png" alt=""/>')

    newtext = newtext.replace('\ue23f', '<img src="data/emoji/e23f.png" alt=""/>')
    newtext = newtext.replace('\ue240', '<img src="data/emoji/e240.png" alt=""/>')
    newtext = newtext.replace('\ue241', '<img src="data/emoji/e241.png" alt=""/>')
    newtext = newtext.replace('\ue242', '<img src="data/emoji/e242.png" alt=""/>')
    newtext = newtext.replace('\ue243', '<img src="data/emoji/e243.png" alt=""/>')
    newtext = newtext.replace('\ue244', '<img src="data/emoji/e244.png" alt=""/>')
    newtext = newtext.replace('\ue245', '<img src="data/emoji/e245.png" alt=""/>')

    newtext = newtext.replace('\ue246', '<img src="data/emoji/e246.png" alt=""/>')
    newtext = newtext.replace('\ue247', '<img src="data/emoji/e247.png" alt=""/>')
    newtext = newtext.replace('\ue248', '<img src="data/emoji/e248.png" alt=""/>')
    newtext = newtext.replace('\ue249', '<img src="data/emoji/e249.png" alt=""/>')
    newtext = newtext.replace('\ue24a', '<img src="data/emoji/e24a.png" alt=""/>')
    newtext = newtext.replace('\ue24b', '<img src="data/emoji/e24b.png" alt=""/>')
    newtext = newtext.replace('\ue23e', '<img src="data/emoji/e23e.png" alt=""/>')

    newtext = newtext.replace('\ue532', '<img src="data/emoji/e532.png" alt=""/>')
    newtext = newtext.replace('\ue533', '<img src="data/emoji/e533.png" alt=""/>')
    newtext = newtext.replace('\ue534', '<img src="data/emoji/e534.png" alt=""/>')
    newtext = newtext.replace('\ue535', '<img src="data/emoji/e535.png" alt=""/>')
    newtext = newtext.replace('\ue21a', '<img src="data/emoji/e21a.png" alt=""/>')
    newtext = newtext.replace('\ue219', '<img src="data/emoji/e219.png" alt=""/>')
    newtext = newtext.replace('\ue21b', '<img src="data/emoji/e21b.png" alt=""/>')

    newtext = newtext.replace('\ue02f', '<img src="data/emoji/e02f.png" alt=""/>')
    newtext = newtext.replace('\ue024', '<img src="data/emoji/e024.png" alt=""/>')
    newtext = newtext.replace('\ue025', '<img src="data/emoji/e025.png" alt=""/>')
    newtext = newtext.replace('\ue026', '<img src="data/emoji/e026.png" alt=""/>')
    newtext = newtext.replace('\ue027', '<img src="data/emoji/e027.png" alt=""/>')
    newtext = newtext.replace('\ue028', '<img src="data/emoji/e028.png" alt=""/>')
    newtext = newtext.replace('\ue029', '<img src="data/emoji/e029.png" alt=""/>')

    newtext = newtext.replace('\ue02a', '<img src="data/emoji/e02a.png" alt=""/>')
    newtext = newtext.replace('\ue02b', '<img src="data/emoji/e02b.png" alt=""/>')
    newtext = newtext.replace('\ue02c', '<img src="data/emoji/e02c.png" alt=""/>')
    newtext = newtext.replace('\ue02d', '<img src="data/emoji/e02d.png" alt=""/>')
    newtext = newtext.replace('\ue02e', '<img src="data/emoji/e02e.png" alt=""/>')
    newtext = newtext.replace('\ue332', '<img src="data/emoji/e332.png" alt=""/>')
    newtext = newtext.replace('\ue333', '<img src="data/emoji/e333.png" alt=""/>')

    newtext = newtext.replace('\ue24e', '<img src="data/emoji/e24e.png" alt=""/>')
    newtext = newtext.replace('\ue24f', '<img src="data/emoji/e24f.png" alt=""/>')
    newtext = newtext.replace('\ue537', '<img src="data/emoji/e537.png" alt=""/>')

    return newtext

def convertsmileys (text):
    global PYTHON_VERSION
    if PYTHON_VERSION == 2:
        newtext = convert_smileys_python_2.convertsmileys_python2 (text)
    elif PYTHON_VERSION == 3:
        newtext = convertsmileys_python3 (text)
    return newtext

################################################################################
#Functions for Find Offline File

def filelistonce (folder, date):
    flnames = []
    flsizes = []

    # for Folder
    flistnames = glob.glob( os.path.join(folder, '*'+date+'*') )
    flistsizes = []
    for i in range(len(flistnames)):
        statinfo = os.stat(flistnames[i])
        fsize = statinfo.st_size
        flistsizes.append(fsize)

    for i in range (len(flistnames)):
        flnames.append(flistnames[i])
        flsizes.append(flistsizes[i])

    # for Subfolders
    for root, dirs, files in os.walk(folder):
        for sdir in dirs:
            sfolder = join(root, sdir)


            flistnames = glob.glob( os.path.join(sfolder, '*'+date+'*') )
            flistsizes = []
            for i in range(len(flistnames)):
                statinfo = os.stat(flistnames[i])
                fsize = statinfo.st_size
                flistsizes.append(fsize)

            flnames += flistnames
            flsizes += flistsizes

    flist = [flnames, flsizes]
    return flist

def filelist (type, date):
    folder = None
    flist = None

    if type == 'IMG':
        folder = GetPath(outfile)+'/WhatsApp/Media/WhatsApp Images/'
        if not date in flistimg:
            flistimg[date] = filelistonce (folder, date)
        flist = flistimg[date]
    elif type == 'AUD':
        folder = GetPath(outfile)+'/WhatsApp/Media/WhatsApp Audio/'
        if not date in flistaud:
            flistaud[date] = filelistonce (folder, date)
        flist = flistaud[date]
    elif type == 'VID':
        folder = GetPath(outfile)+'/WhatsApp/Media/WhatsApp Video/'
        if not date in flistvid:
            flistvid[date] = filelistonce (folder, date)
        flist = flistvid[date]
    elif type == 'PTT':
        folder = GetPath(outfile)+'/WhatsApp/Media/WhatsApp Voice Notes/'
        if not date in flistptt:
            flistptt[date] = filelistonce (folder, date)
        flist = flistptt[date]
    return folder, flist

def findfile (type, size, localurl, date, priordays, additionaldays):
    fname = ''

    if mode == ANDROID:
        # extractet FilePathName from thumb_image to localurl
        folder = '/WhatsApp/Media/'
        if len(localurl) > 0:
            if localurl[0] == "/":
                localurl = localurl[1:]
        if os.path.exists(localurl):
            fname = localurl
        else:

            # fallback
            # The findfile Function (search on Date and size) malfunctioning!!!!
            # sometime is the media content from the Thumbnail-Picture and mediasize different to the related File width the filename in "media_name" and the located File in the Media-Folder

            fname = ''
            date = str(date)

            timestampreceived = int(str(time.mktime(datetime.datetime.strptime(date, "%Y%m%d").timetuple()))[:-2])
            timestamptobegin = timestampreceived - 86400 * priordays
            newdate = str(datetime.datetime.fromtimestamp(timestamptobegin))[:10]
            newdate = newdate.replace("-","")
            date = newdate

            z = 0
            while fname == '':
                z = z + 1

                #use or create list of ALL media files of that type and that date
                folder, flist = filelist (type, date)
                #search the file with the given size
                try:
                    fname = flist [0] [ flist[1].index(size) ]
                except:
                    fname = ''

                if fname == '':

                    #if file is not found for begin ("today" - priordays), then try for "tomorrow" and "the day after tomorrow" ("today" + additionaldays - setp per day).
                    #If it's still not found, then try to find the temporary file, if not successful then just link the media folder

                    if z >= 1 + priordays + additionaldays:
                        # search all files in folder and subfolders
                        for root, dirs, files in os.walk(folder):
                            try:
                                fname = join(root, files [ files.index(localurl) ])
                                continue
                            except:
                                pass
                        # if itÂ´s not found by name
                        if fname == '':
                            fname = folder

                    else:
                        # add one day to date
                        timestamptoday = int(str(time.mktime(datetime.datetime.strptime(date, "%Y%m%d").timetuple()))[:-2])
                        timestamptomorrow = timestamptoday + 86400
                        tomorrow = str(datetime.datetime.fromtimestamp(timestamptomorrow))[:10]
                        tomorrow = tomorrow.replace("-","")
                        date = tomorrow
    elif mode == IPHONE:
        folder = '/Media/'
        if len(localurl) > 0:
            if localurl[0] == "/":
                localurl = localurl[1:]
        if os.path.exists(localurl):
            fname = localurl
        else:
            fname = folder

    #return the file name
    return fname

################################################################################
# Functions for opening and closing of output files


# Receives the name of an output file to create and initialize, and also a
# DB owner name
def outputfile_open(file_name, file_objectB):

    global have_tf
    global strtsFrom
    global strtsTo
    global db_owner
    global db_owner_name

    global APPLICATION
    AppDictPNG = {"WA":"whatsapp.png", "KiraWA":"KiraWA.png"}
    AppDictALT = {"WA":"WhatsApp", "KiraWA":"NEWhatsapp (Kira)"}

    if APPLICATION in AppDictPNG:
        AppPNG = AppDictPNG[APPLICATION]
        AppALT = AppDictALT[APPLICATION]
    else:
        AppPNG = ""
        AppALT = "Messenger"

    file_object = None;

    file_object = open(file_name,'wb')

    NTF = False
    INFstr =""
    if is_str(file_objectB):
        if file_objectB.find("NTF") != -1:
            # NoTimeFilter
            NTF = True
        if file_objectB.find("GAI") != -1:
            # Group analysis Infotext
            INFstr = "<h3>Attention! - Group Analysis </br>"\
                    "The list of group members based on the stored messages and status messages, this is not conclusive. </br>"\
                    "Has 'Display Name' the value 'N/A', then the contact is not in the address book.</h3>"

        # reset file_objectB
        file_objectB = None

    print("Creating file " + file_name + "...")
    # writes page header
    outputfileAB(file_object, file_objectB, '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\n'.encode('utf-8'))
    outputfileAB(file_object, file_objectB, '"http://www.w3.org/TR/html4/loose.dtd">\n'.encode('utf-8'))
    outputfileAB(file_object, '<html><head><title>{0}</title>\n'.format(file_name).encode('utf-8'))
    outputfileAB(file_objectB, '<html><head><title>{0}</title>\n'.format(file_name).encode('utf-8'))
    outputfileAB(file_object, file_objectB, '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>\n'.encode('utf-8'))
    outputfileAB(file_object, file_objectB, '<meta name="GENERATOR" content="WhatsApp Xtract v{0}"/>\n'.format(XTRACT_VERSION).encode('utf-8'))
    # adds page style
    outputfileAB(file_object, file_objectB, css_style.encode('utf-8'))

    # adds javascript to make the tables sortable
    outputfileAB(file_object, file_objectB, '\n<script type="text/javascript">\n'.encode('utf-8'))
    outputfileAB(file_object, file_objectB, popups.encode('utf-8'))
    outputfileAB(file_object, file_objectB, sortable.encode('utf-8'))
    outputfileAB(file_object, file_objectB, '</script>\n\n'.encode('utf-8'))
    outputfileAB(file_object, file_objectB, '</head><body>\n'.encode('utf-8'))

    # H1 Title
    #outputfileAB(file_object, file_objectB, '<h1>Zena Forensics<h1>'.encode('utf-8'))

    # H2 DB Owner
    outputfileAB(file_object, file_objectB, '<a name="top"></a><h2>'.encode('utf-8'))
    outputfileAB(file_object, file_objectB, 'WhatsApp&nbsp;'.encode('utf-8'))
    outputfileAB(file_object, file_objectB, '<img src="data/img/{0}" alt="{1}" '.format(AppPNG, AppALT).encode('utf-8'))
    outputfileAB(file_object, file_objectB, 'style="width:40px;height:40px;vertical-align:middle"/>'.encode('utf-8'))
    outputfileAB(file_object, file_objectB, '&nbsp;Xtract {0}&nbsp;({1})&nbsp;&nbsp;&nbsp;'.format(XTRACT_VERSION, XTRACT_DATE).encode('utf-8'))

    if mode == IPHONE:
        outputfileAB(file_object, file_objectB, '<img src="data/img/apple.png" alt="iPhone" '.encode('utf-8'))
    elif mode == ANDROID:
        outputfileAB(file_object, file_objectB, '<img src="data/img/android.png" alt="Android" '.encode('utf-8'))
    outputfileAB(file_object, file_objectB, 'style="width:35px;height:35px;"/>'.encode('utf-8'))

    if db_owner == "":
        if db_owner_name == "":
            outputfileAB(file_object, file_objectB, '</h2>\n'.encode('utf-8'))
        else:
            outputfileAB(file_object, file_objectB, '[me: {0}]</h2>\n'.format(db_owner_name).encode('utf-8'))
    else:
        if db_owner_name == "":
            outputfileAB(file_object, file_objectB, '&nbsp;&nbsp;&nbsp; [me: {0}]</h2>\n'.format(db_owner).encode('utf-8'))
        else:
            outputfileAB(file_object, file_objectB, '&nbsp;&nbsp;&nbsp; [me: {1} - {0}]</h2>\n'.format(db_owner, db_owner_name).encode('utf-8'))



    # Info Str
    if INFstr != "":
        outputfileAB(file_object, file_objectB, '{0}\n'.format(INFstr).encode('utf-8'))

    # writes TimeFilter Information when enable (-f Y)
    if have_tf and NTF == False:
        outputfileAB(file_object, file_objectB, '<h3>Time Filter:\n'.encode('utf-8'))
        outputfileAB(file_object, file_objectB, '<table border=0 > \n'.encode('utf-8'))
        outputfileAB(file_object, file_objectB, '<tr><td>From:</td><td>{}</td></tr>\n'.format(strtsFrom).encode('utf-8'))
        outputfileAB(file_object, file_objectB, '<tr><td>To:</td><td>{}</td></tr>\n'.format(strtsTo).encode('utf-8'))
        outputfileAB(file_object, file_objectB, '</table></h3>\n'.encode('utf-8'))

    return file_object;


def outputfileAB(*args):
    # (file_objectA, Optional file_objectB, outputTEXT)
    file_objectA = None
    file_objectB = None
    outputTEXT = ''

    if len(args) < 2 or len(args) > 3:
        exit

    if len(args) == 2:
        file_objectA = args[0]
        outputTEXT = args[1]

    if len(args) == 3:
        file_objectA = args[0]
        file_objectB = args[1]
        outputTEXT = args[2]

    if not (file_objectA is None or file_objectA == ''):
        file_objectA.write(outputTEXT)
    if not (file_objectB is None or file_objectB == ''):
        file_objectB.write(outputTEXT)

    return;

def outputfile_close(file_object):

    # writes page footer
    file_object.write('</body></html>\n'.encode('utf-8'))
    file_object.close()

    return;

def GroupInfo (Cid):
    GroupAdmin = None
    GroupCreationTime = None

    if '@g.us' in Cid:
        Group = Cid.split("@")[0]
        GroupAdmin, GroupCreationTimeStamp = Group.split("-")
        #GroupCreationTime = str(datetime.datetime.fromtimestamp(int(GroupCreationTimeStamp)))[:10]
        GroupCreationTime = convertTimeStamp(GroupCreationTimeStamp)
    return GroupAdmin, GroupCreationTime

def dbjournaling(dbFile):
    # Open Databse for Testing - only uncrypted SQLite DB
    with open(dbFile, "r+b") as dbf:
        dbf.seek(0,0)
        descriptor_bytes = dbf.read(15)
        expected_descriptor_bytes = b"SQLite format 3"
        if descriptor_bytes == expected_descriptor_bytes:

            # Test for write/read as 1 = legacy; 2 = WAL
            dbf.seek(18,0)
            file_format_bytes = dbf.read(2)

            if file_format_bytes[0] == b'\x02' or file_format_bytes[1] == b'\x02':
                dbf.seek(18,0)
                dbf.write(b'\x01\x01')

                print(dbFile)
                print("SQLite database file format WAL -> set to legacy")
        dbf.close

def me_owner():
    # get owner PhoneNo from me file
    global db_owner
    global FilePathF

    with open(FilePathF+"me", "r") as me_file:
        blob_me=me_file.read()
    me_file.close

    # check of me file
    posStart=str(blob_me).find("\x00\x13")

    if posStart != -1:
        tempTEXT=blob_me[posStart+2:posStart+2+len("com.whatsapp.App")]

    if tempTEXT == "com.whatsapp.App":
        # get Phone No
        posStart=str(blob_me).find("\x00\x0D")
        if posStart == -1:
            posStart=str(blob_me).find("\x00\x0C")


        if posStart != -1:
            tempPhone=blob_me[posStart+2:]
            Phone=tempPhone[:tempPhone.find("\x74")]
            # set db_owner as wa jid
            db_owner = Phone + "@s.whatsapp.net"

    return

def me_owner_name():
    # get owner Name
    # from com.whatsapp_preferences.xml file - node: "string" - attribute: name = "push_name" - Value Node = db_owner_name
    global db_owner_name
    global FilePathSP

    xmldoc = minidom.parse(FilePathSP+'com.whatsapp_preferences.xml')

    cNodes = xmldoc.childNodes
    for node in cNodes:
        eList = node.getElementsByTagName("string")
        for e in eList:
            if e.hasAttribute("name"):
                if e.getAttribute("name") == "push_name":
                    db_owner_name = " ".join(t.nodeValue for t in e.childNodes if t.nodeType == t.TEXT_NODE)

    return


def convertTimeStamp(timestamp, TimeZone="LOCAL"):
    # Convert Timestamp Unix Epoch into Date-Time - Standrad = Local-Time ( "LOCAL" or "UTC")

    if not isinstance(timestamp, int):
        try:
            timestamp = int(timestamp)
        except (TypeError, ValueError) as msg:
            date = "N/A error"

    if TimeZone =="UTC":
        try:
            date = datetime.datetime.utcfromtimestamp(timestamp)
        except (TypeError, ValueError) as msg:
            date = "N/A error"
    else:
        try:
            date = datetime.datetime.fromtimestamp(timestamp)
        except (TypeError, ValueError) as msg:
            date = "N/A error"

    return date

def totimestamp(dt, TimeZone="LOCAL"):
    # convert Date [Standrad = Local-Time ( "LOCAL" or "UTC")] into Epoch-Timestamp
    # Formates:
    # YYYY-MM-DD HH:MM:SS
    #
    # DD.MM.YYYY
    # DD.MM.YYYY HH:MM
    # DD.MM.YYYY HH:MM:SS

    # 1 Year = 31536000 Sec.

    epoch=datetime.datetime(1970,1,1)

    if asciifunc(dt):
        strdt= str(dt).strip()

        if strdt.find("-") > 0:
            try:
                dt = datetime.datetime.strptime(strdt,"%Y-%m-%d %H:%M:%S")
            except:
                try:
                    dt = datetime.datetime.strptime(strdt,"%Y-%m-%d %H:%M")
                except:
                    dt = datetime.datetime.strptime(strdt,"%Y-%m-%d")

        else:
            strdt=strdt.replace(" Uhr","")
            strdt=strdt.replace(" uhr","")
            strdt=strdt.replace("Uhr","")
            strdt=strdt.replace("uhr","")

            try:
                dt = datetime.datetime.strptime(strdt,"%d.%m.%Y %H:%M:%S")
            except:
                try:
                    dt = datetime.datetime.strptime(strdt,"%d.%m.%Y %H:%M")
                except:
                    dt = datetime.datetime.strptime(strdt,"%d.%m.%Y")

    if TimeZone == "LOCAL":
        # return td.total_seconds() - LOCAL
        strts = str(time.mktime(dt.timetuple()))

    else:
        # return td.total_seconds() - UTC
        td = dt - epoch
        strts = str((td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 1e6)

    posPoint=strts.find(".")
    strts = strts[:posPoint]

    return int(strts)

def MediaFileType(Fullpath):
    strType = 'N/A'

    if mode == ANDROID:
        if len(Fullpath) > 0:
            if Fullpath.find("WhatsApp Voice Notes") > 0:
                strType = 'Voice Note'
            if Fullpath.find("WhatsApp Audio") > 0:
                strType = "Audio"
            if Fullpath.find("WhatsApp Images") > 0:
                strType = "Image"
            if Fullpath.find("WhatsApp Video") > 0:
                strType = "Video"
    elif mode == IPHONE:
        if len(Fullpath) > 0:
            strType = "iPHONE"

    return strType

def MediaFilePath(Fullpath):
    strName = 'N/A'

    if mode == ANDROID:
        if len(Fullpath) > 0:
            if Fullpath.find("WhatsApp Voice Notes") > 0:
                strX = Fullpath.find("WhatsApp Voice Notes") + len("WhatsApp Voice Notes")
                strName = Fullpath[strX:]
            if Fullpath.find("WhatsApp Audio") > 0:
                strX = Fullpath.find("WhatsApp Audio") + len("WhatsApp Audio")
                strName = Fullpath[strX:]
            if Fullpath.find("WhatsApp Images") > 0:
                strX = Fullpath.find("WhatsApp Images") + len("WhatsApp Images")
                strName = Fullpath[strX:]
            if Fullpath.find("WhatsApp Video") > 0:
                strX = Fullpath.find("WhatsApp Video") + len("WhatsApp Video")
                strName = Fullpath[strX:]
    elif mode == IPHONE:
        if len(Fullpath) > 0:
                strX = Fullpath.find(GetPath(outfile)+"WhatsApp") + len(GetPath(outfile)+"WhatsApp")
                strName = Fullpath[strX:]

    strOld = '\\'
    strNew = '/'
    strName = strName.replace(strOld, strNew)

    return strName

def printable(input):
    return ''.join([c for c in input if (ord(c) > 31 or ord(c) == 9) and ord(c) < 128])


def timeperiod(sekunden):

    # timeperiod provides time as string

    delta = datetime.timedelta(seconds = sekunden)
    delta_str = str(delta)[-8:] # i.E: " 1:01:01"

    return delta_str

def is_str (s):
    # if var s String
    if type(s) == type("TEXT"):
        return True
    else:
        return False




################################################################################
################################################################################
# MAIN
def main(argv):

    chat_session_list = []
    global mode
    global PYTHON_VERSION
    global content_type

    global DoOut

    global have_tf
    global strtsFrom
    global strtsTo

    global APPLICATION

    global have_groups
    global db_owner
    global db_owner_name

    global FilePathDB
    global FilePathF
    global FilePathSP
    global FilePathCrypt

    global AppVersion

    strInputFrom = ""
    strInputTo   = ""
    have_groups = False
    ChatIsGroup = False

    #debug
    debugzaehler = 0
    # parser options
    parser = ArgumentParser(description='Converts a Whatsapp database to HTML.')
    parser.add_argument(dest='infile',
                       help="input 'msgstore.db'; 'msgstore.db.crypt' or 'msgstore.db.db' (Android) or 'ChatStorage.sqlite' (iPhone) file to scan",nargs='?',default='Report\com.whatsapp\databases\msgstore.db')
    parser.add_argument('-w', '--wafile', dest='wafile',
                       help="optionally input 'wa.db' (Android) file to scan")
    parser.add_argument('-o', '--outfile',  dest='outfile',
                       help="optionally choose name of output file",default='./Report/Report')
    parser.add_argument('-f', '--filter',  dest='timefilter',
                       help="optionally choose Y for activate TimeFilter")
    options = parser.parse_args()


    # Print Output Version and Last Update
    print('WhatsApp_Xtract {0} ({1})'.format(XTRACT_VERSION, XTRACT_DATE))
    print

    # checks for the com.whatsapp_preferences.xml file
    if os.path.exists(FilePathSP+"com.whatsapp_preferences.xml"):
        have_preferences = True
    else:
        have_preferences = False

    print ("have preferences: " + str(have_preferences))
    print

    # checks for the me file
    if os.path.exists(FilePathF+"me"):
        have_me = True
    else:
        have_me = False

    print ("have me: " + str(have_me))
    print

    # checks for the wadb file
    if options.wafile is None:
        if os.path.exists(GetPath(options.infile)+"/wa.db"):
            FilePathDB=GetPath(options.infile)+"/"
            options.wafile="wa.db"
            have_wa = True
        else:
            have_wa = False
    elif not os.path.exists(FilePathDB+options.wafile):
        print('Warning: "{0}" file is not found!'.format(options.wafile))
        sys.exit(1)
    else:
        have_wa = True

    print ("have wa: " +  str(have_wa))
    print

    # checks for the TimeFilter
    if options.timefilter is None:
        have_tf = False
    else:
        toption = options.timefilter.upper()
        if toption in ["J", "Y"]:
            have_tf = True
        else:
            have_tf = False

    print ("have TimeFilter: " + str(have_tf))
    print

    global outfile

    if options.outfile is None:
        if owner == "":
            outfile = options.infile.replace(".crypt", "")
        else:
            outfile = owner
    else:
        outfile = options.outfile

    if have_tf:
        print ("Input Format:")
        print ("dd.mm.YYYY")
        print ("dd.mm.YYYY HH:MM")
        print ("dd.mm.YYYY HH:MM:SS")
        print ("YYYY-mm-dd HH:MM:SS")
        print ("")
        strInputFrom = raw_input("Date[Time] From or Enter = first message: ")
        strInputTo   = raw_input("Date[Time] To   or Enter = last  message: ")
        print ("")

        strInputFrom = strInputFrom.strip()
        strInputTo = strInputTo.strip()

    if strInputFrom == "":
        # No Input - tsFrom = 0 = 01.01.1970 00:00 Uhr
        tsFrom = 0
        strtsFrom = "First stored message."
    else:
        tsFrom = totimestamp(strInputFrom)
        strtsFrom = str(convertTimeStamp(tsFrom))

    if strInputTo == "":
        # No Input - tsTo = now + 1 Year
        now = str(datetime.datetime.now())
        posPoint = now.find(".")
        now = now[:posPoint]
        tsTo = totimestamp(now) + 31536000
        strtsTo = "Last stored message."
    else:
        if len(strInputTo) < 11:
            strInputTo = strInputTo + " 23:59:59"
        tsTo = totimestamp(strInputTo)
        strtsTo = str(convertTimeStamp(tsTo))

    if have_tf:
        #print "TimeStamp From: " + str(tsFrom)
        #print "TimeStamp To  : " + str(tsTo)
        #print ""

        print ("TimeStamp From: " + strtsFrom)
        print ("TimeStamp To  : " + strtsTo)
        print ("")

    # checks for the input file
    if options.infile is None:
        options.infile=FilePathDB+"msgstore.db"
    if not os.path.exists(options.infile):
        print('Warning: "{0}" file is not found!'.format(options.infile))
        sys.exit(1)

    # First, let's see if this is actually an encrypted file or not
    with open(options.infile, "rb") as f:
        f.seek(0,0)
        descriptor_bytes = b"SQLite format 3"
        descriptor_bytes = f.read(15)
        expected_descriptor_bytes = b"SQLite format 3"
        f.close

        print(options.infile)

        if descriptor_bytes == expected_descriptor_bytes:

            print("Detected an SQLite database")

            dbjournaling(options.infile)

        # If we have an encrypted file, try and decrypt it
        else:

            print('Detected non-SQLite database, potentially an encrypted Android database')
            print("Trying to decrypt Android database...")

            if (options.infile.find(".crypt")):
                decodedfile=decryptwhatsapp(options.infile,GetPath(outfile))

            print("Decrypted file written to " + decodedfile)
            #print ("size:" + str(len (decoded)) )

            # Let's try it again
            with open(decodedfile, "rb") as f:
                descriptor_bytes = f.read(15)

                if descriptor_bytes == expected_descriptor_bytes:

                    print ('Success! Decrypted file is an SQLite database')
                    options.infile = decodedfile

                    dbjournaling(decodedfile)

                else:

                    print ('Error: File is not an encrypted Android database')
                    sys.exit(1)

    # Okay, by this point we have a valid SQLite datbase, but integrity is not certain.
    # AlonD: Check for SQLite string is not perfect. If it is not truly an SQLite
    # database the app will happily crash. Up to the user to get the point :P

    # Connects to the database(s)
    msgstore = sqlite3.connect(options.infile)
    msgstore.row_factory = sqlite3.Row
    c1 = msgstore.cursor()
    c2 = msgstore.cursor()
    c3 = msgstore.cursor()
    c4 = msgstore.cursor()

    # Check on platform
    try:

        c1.execute("SELECT * FROM ZWACHATSESSION")
        # if succeeded --> IPHONE mode
        mode = IPHONE
        print
        print ("iPhone mode!\n")
        print

    except:

        # if failed --> ANDROID mode
        mode = ANDROID
        print
        print ("Android mode!")
        print

    if mode == ANDROID:

        # detect Application NEWhatsApp (Kiara)
        if os.path.exists(GetPath(options.outfile)+"WhatsApp\\NEWhatsApp Images"):
            print ("Database Source:     NEWhatsApp (Kiara)")
            APPLICATION = "KiraWA"
        elif os.path.exists(GetPath(options.outfile)+"WhatsApp\\NEWhatsApp Video"):
            print ("Database Source:     NEWhatsApp (Kiara)")
            APPLICATION = "KiraWA"
        elif os.path.exists(GetPath(options.outfile)+"WhatsApp\\NEWhatsApp Voice Notes"):
            print ("Database Source:     NEWhatsApp (Kiara)")
            APPLICATION = "KiraWA"
        else:
            print ("Database Source:     WhatsApp")
            APPLICATION = "WA"

        if have_preferences:
            me_owner_name()
            print ("Database Owner Name: " + str(db_owner_name))
            #print

        if have_me:
            me_owner()
            print ("Database Owner:      " + db_owner)
            #print


        # Open the WA file for contacts and stuff
        print
        if have_wa:

            # Test for dbjournaling and set to legacy when WAL was used
            dbjournaling(FilePathDB+options.wafile)

            wastore = sqlite3.connect(FilePathDB+options.wafile)
            wastore.row_factory = sqlite3.Row
            wa = wastore.cursor()
            w2 = wastore.cursor()

        # Check the integrity of the SQLite file
        print ('Checking Android database integrity...')

        # This doesn't throw an exception on Python 2.x and does on 3.x - yay.
        try:

            # Get the integrity status. 'ok' means we're good
            integrity_status = c1.execute("PRAGMA integrity_check;").fetchone()[0]

        except sqlite3.DatabaseError:

            integrity_status = "not ok";


        # Do we have integrity problems?
        if integrity_status == "ok":

            # Integrity is fine
            print ("Android database has no integrity issues\n")

        else:

            # Yep, we have integrity problems
            print ("Android database has integrity issues. Attempting to fix it...")

            # AlonD: instead of using iterdump and so forth, which should be the correct way to do this,
            # we'll just use SQLite as it is faster to code. Shoot me

            # Make sure sqlite3 is available
            if os.system("echo .exit | sqlite3") != 0:

                print('Error: sqlite3 file not found!')
                print('Get it from https://www.sqlite.org/download.html')
                print('Correct download for Windows users begins with "sqlite-shell-win32", put file in same directory as this script')
                sys.exit(1)

            # Close database
            c1.close()
            c2.close()
            c3.close()
            msgstore.close()

            # Dump an SQL output of our database
            os.system('echo .dump | sqlite3 "{0}" > {1}'.format(options.infile, options.infile + '.sql'))

            # Open the file and try and remove the following lines which prevent the SQL from committing successfully:
            #    CREATE UNIQUE INDEX messages_key_index on messages (key_remote_jid, key_from_me, key_id);
            #    ROLLBACK; -- due to errors
            # Yes, we'll lose the index, but we do not care

            with io.open(options.infile + '.sql', 'r', encoding='utf-8') as f:

                with io.open(options.infile + '.repaired.sql', 'w', encoding='utf-8') as f2:

                    # Remove bad lines.
                    # AlonD: Would be better to just edit SQL file but again, lazy
                    for line in f:

                        if line != "CREATE UNIQUE INDEX messages_key_index on messages (key_remote_jid, key_from_me, key_id);\n" and \
                           line != "ROLLBACK; -- due to errors\n":

                            f2.write(line);

                    f2.write(u"COMMIT;");


            # Make sure new fixed database file doesn't exist
            repairedfile = options.infile + '.repaired.db'

            # Delete the repaired file if it already exists
            if os.path.exists(repairedfile):
                os.remove(repairedfile)

            os.system('echo .exit | sqlite3 -init "{0}" "{1}"'.format(options.infile + '.repaired.sql', repairedfile))

            # Alright, let's try again..

            # Open database stuff
            msgstore = sqlite3.connect(repairedfile)
            msgstore.row_factory = sqlite3.Row
            c1 = msgstore.cursor()
            c2 = msgstore.cursor()
            c3 = msgstore.cursor()
            c4 = msgstore.cursor()

            # Get the integrity status. 'ok' means we're good
            integrity_status = c1.execute("PRAGMA integrity_check;").fetchone()[0]

            # Do we have integrity problems?
            if integrity_status == "ok":

                # Integrity is fine
                print ("Android database has been succesfully repaired and has no integrity issues\n")

            else:

                print('Warning: failed repairing database')
                sys.exit(1)

    msgstore.text_factory = lambda x: str(x, 'utf_8_sig')

    # gets metadata plist info (iphone only)
    if mode == IPHONE:
        try:
            # ------------------------------------------------------ #
            #  IPHONE  ChatStorage.sqlite file *** Z_METADATA TABLE  #
            # ------------------------------------------------------ #
            # Z_VERSION INTEGER PRIMARY KEY
            # Z_UUID VARCHAR
            # Z_PLIST BLOB
            from bplist import BPlistReader
            c1.execute("SELECT * FROM Z_METADATA")
            metadata = c1.fetchone()
            print ("*** METADATA PLIST DUMP ***\n")
            print ("Plist ver.:  {0}".format(metadata["Z_VERSION"]))
            print ("UUID:        {0}".format(metadata["Z_UUID"]))
            bpReader = BPlistReader(metadata["Z_PLIST"])
            plist = bpReader.parse()

            for entry in plist.items():
                if entry[0] == "NSStoreModelVersionHashes":
                    print ("{0}:".format(entry[0]))
                    for inner_entry in entry[1].items():
                        print ("\t{0}: {1}".format(inner_entry[0],base64.b64encode(inner_entry[1]).decode("utf-8")))
                else:
                    print ("{0}: {1}".format(entry[0],entry[1]))
                    # NSStoreModelVersionIdentifiers: ['2.12.14']
                    if entry[0] == "NSStoreModelVersionIdentifiers":
                        AppVersion=entry[1][0]
            print ("\n***************************\n")

        except:
            print ("Metadata Plist Dump is failed. Note that you need to use Python 2.7 for that bplist.py works")

    # Okay, by this point we have a valid and integral databas file

    # gets all the chat sessions
    if 1==1: #debug
    #try:
        if mode == ANDROID:
            if have_wa:
                # wa.execute("SELECT * FROM wa_contacts WHERE is_whatsapp_user = 1 GROUP BY jid")
                # check all Users,

                wa.execute("SELECT display_name FROM wa_contacts GROUP BY display_name")
                testwa = wa.fetchall()

                if len(testwa) == 1:
                    wa.execute("SELECT display_name FROM wa_contacts GROUP BY display_name")
                    testwa = wa.fetchone()[0]

                if testwa == "" or testwa is None or len(testwa) == 0:
                    have_wa = False

                if have_wa:
                    wa.execute("SELECT * FROM wa_contacts GROUP BY jid")
                    for chats in wa:
                        # ------------------------------------------ #
                        #  ANDROID WA.db file *** wa_contacts TABLE  #
                        # ------------------------------------------ #
                        # chats[0] --> id (primary key)
                        # chats[1] --> jid
                        # chats[2] --> is_whatsapp_user
                        # chats[3] --> is_iphone
                        # chats[4] --> status
                        # chats[5] --> number
                        # chats[6] --> raw_contact_id
                        # chats[7] --> display_name
                        # chats[8] --> phone_type
                        # chats[9] --> phone_label
                        # chats[10] -> unseen_msg_count
                        # chats[11] -> photo_ts
                        # chats[12] -> thumb_ts
                        # chats[13] -> photo_id_timestamp
                        # chats[14] -> given_name
                        # chats[15] -> family_name
                        # chats[16] -> wa_name
                        try:
                            c2.execute("SELECT timestamp FROM messages WHERE key_remote_jid='{}' ORDER BY timestamp DESC LIMIT 1;".format(chats["jid"]))
                            lastmessagedate = c2.fetchone()[0]
                        except: #not all contacts that are whatsapp users may already have been chatted with
                            lastmessagedate = None

                        # WA Database have Groups
                        if chats["jid"].find("@g.us") >0:
                            have_groups = True

                        curr_chat = Chatsession(chats["_id"],chats["display_name"],chats["wa_name"],chats["jid"],None,chats["unseen_msg_count"],chats["status"],lastmessagedate,chats["is_whatsapp_user"])
                        chat_session_list.append(curr_chat)
                else:
                    print ("-----------------------------------")
                    print ("----------- Warnning ! ------------")
                    print ("-----------------------------------")
                    print (options.wafile + " have no Data or is incomplete")
                    print (" and is ignored!")
                    print ("-----------------------------------")
                    print ("----------- Warnning ! ------------")
                    print ("-----------------------------------")

            if not have_wa:
                c1.execute("SELECT * FROM chat_list")
                for chats in c1:
                    # ---------------------------------------------- #
                    #  ANDROID MSGSTORE.db file *** chat_list TABLE  #
                    # ---------------------------------------------- #
                    # chats[0] --> _id (primary key)
                    # chats[1] --> key_remote_jid (contact jid or group chat jid)
                    # chats[2] --> message_table_id (id of last message in this chat, corresponds to table messages primary key)
                    name = chats["key_remote_jid"].split('@')[0]
                    try:
                       # lastmessage = chats["message_table_id"]
                       # c2.execute("SELECT timestamp FROM messages WHERE _id=?", [lastmessage])
                        c2.execute("SELECT timestamp FROM messages WHERE key_remote_jid='{}' ORDER BY timestamp DESC LIMIT 1;".format(chats["key_remote_jid"]))
                        lastmessagedate = c2.fetchone()[0]
                    except:
                        lastmessagedate = None

                    # WA Database have Groups
                    if chats["key_remote_jid"].find("@g.us") >0:
                        have_groups = True

                    curr_chat = Chatsession(chats["_id"],name,None,chats["key_remote_jid"],None,None,None,lastmessagedate,None)
                    chat_session_list.append(curr_chat)

        elif mode == IPHONE:
            c1.execute("SELECT * FROM ZWACHATSESSION")
            for chats in c1:
                # ---------------------------------------------------------- #
                #  IPHONE  ChatStorage.sqlite file *** ZWACHATSESSION TABLE  #
                # ---------------------------------------------------------- #
                # chats[0] --> Z_PK (primary key)
                # chats[1] --> Z_ENT
                # chats[2] --> Z_OPT
                # chats[3] --> ZINCLUDEUSERNAME
                # chats[4] --> ZUNREADCOUNT
                # chats[5] --> ZCONTACTABID
                # chats[6] --> ZMESSAGECOUNTER
                # chats[7] --> ZLASTMESSAGEDATE
                # chats[8] --> ZCONTACTJID
                # chats[9] --> ZSAVEDINPUT
                # chats[10] -> ZPARTNERNAME
                # chats[11] -> ZLASTMESSAGETEXT

                try:
                    c2.execute("SELECT ZSTATUSTEXT FROM ZWASTATUS WHERE ZCONTACTABID =?;", [chats["ZCONTACTABID"]])
                    statustext = c2.fetchone()[0]
                except:
                    statustext = None
                # ---------------------------------------------------------- #
                #  IPHONE  ChatStorage.sqlite file *** ZWASTATUS TABLE       #
                # ---------------------------------------------------------- #
                # Z_PK (primary key)
                # Z_ENT
                # Z_OPT
                # ZEXPIRATIONTIME
                # ZCONTACTABID
                # ZNOPUSH
                # ZFAVORITE
                # ZSTATUSDATE
                # ZPHONENUMBER
                # c2.fetchone()[0] --> ZSTATUSTEXT
                # ZWHATSAPPID

                # NICKName for SessionList
                try:
                    c4.execute("Select ZPUSHNAME From ZWAMESSAGE Where ZFROMJID like '{}' Group By ZPUSHNAME Order By Z_PK DESC;".format(chats["ZCONTACTJID"]))
                    waNICK = c4.fetchone()[0]
                except:
                    waNICK = None

                # WA Database have Groups
                if chats["ZCONTACTJID"].find("@g.us") >0:
                    have_groups = True

                curr_chat = Chatsession(chats["Z_PK"],chats["ZPARTNERNAME"],waNICK,chats["ZCONTACTJID"],chats["ZMESSAGECOUNTER"],chats["ZUNREADCOUNT"],statustext,chats["ZLASTMESSAGEDATE"],None)
                chat_session_list.append(curr_chat)
        chat_session_list = sorted(chat_session_list, key=lambda Chatsession: Chatsession.last_message_date, reverse=True)

    if 0==1: #debug
    #except sqlite3.Error as msg:
        print('Error: {0}'.format(msg))
        sys.exit(1)

    # for each chat session, gets all messages
    count_chats = 0
    for chats in chat_session_list:
        count_chats = count_chats + 1
        GroupMembers = []
        try:
            if mode == ANDROID:
                c1.execute("SELECT * FROM messages WHERE key_remote_jid=? ORDER BY _id ASC;", [chats.contact_id])
            elif mode == IPHONE:
                c1.execute("SELECT * FROM ZWAMESSAGE WHERE ZCHATSESSION=? ORDER BY Z_PK ASC;", [chats.pk_cs])
            count_messages = 0
            for msgs in c1:
                count_messages = count_messages + 1
                try:
                    if mode == ANDROID:
                        # --------------------------------------------- #
                        #  ANDROID MSGSTORE.db file *** messages TABLE  #
                        # --------------------------------------------- #
                        # msgs[0] --> _id (primary key)
                        # msgs[1] --> key_remote_jid
                        # msgs[2] --> key_from_me
                        # msgs[3] --> key_id
                        # msgs[4] --> status
                        # msgs[5] --> needs_push
                        # msgs[6] --> data
                        # msgs[7] --> timestamp
                        # msgs[8] --> media_url
                        # msgs[9] --> media_mime_type
                        # msgs[10] -> media_wa_type
                        # msgs[11] -> media_size
                        # msgs[12] -> media_name
                        # msgs[13] -> media_duration
                        # msgs[14] -> latitude
                        # msgs[15] -> longitude
                        # msgs[16] -> thumb_image
                        # msgs[17] -> remote_resource
                        # msgs[18] -> received_timestamp
                        # msgs[19] -> send_timestamp
                        # msgs[20] -> receipt_server_timestamp
                        # msgs[21] -> receipt_device_timestamp

                        # message sender
                        contactfromNICK = None
                        messagedata = None
                        broadcast = None

                        if msgs["remote_resource"] == "" or msgs["remote_resource"] is None:
                            contactfrom = msgs["key_remote_jid"]
                        else:
                            if "@" in msgs["remote_resource"]:
                                if msgs["remote_resource"].split("@")[1] == "broadcast":
                                    contactfrom = msgs["key_remote_jid"]
                                    broadcast = msgs["remote_resource"]
                                else:
                                    contactfrom = msgs["remote_resource"]
                            else:
                                contactfrom = msgs["key_remote_jid"]

                            if have_wa:
                                # message sender NICK
                                try:
                                    w2.execute("SELECT wa_name FROM wa_contacts WHERE jid=? ORDER BY _id ASC;", [contactfrom])
                                    contactfromNICK = w2.fetchone()[0]
                                    if contactfromNICK == "" or contactfromNICK is None:
                                        contactfromNICK = msgs["remote_resource"].split("@")[0]
                                except:
                                    try:
                                        w2.execute("SELECT display_name FROM wa_contacts WHERE jid=? ORDER BY _id ASC;", [contactfrom])
                                        contactfromNICK = w2.fetchone()[0]
                                        if contactfromNICK == "" or contactfromNICK is None:
                                            contactfromNICK = msgs["remote_resource"].split("@")[0]
                                    except:
                                       contactfromNICK = msgs["remote_resource"].split("@")[0]

                        # Media File FullPath or Media_Name
                        try:
                            localurlX = msgs["thumb_image"]
                            if localurlX.find("Media") >0:
                                posStart=localurlX.find("Media")
                                localurl = localurlX[posStart:-3]
                            else:
                                try:
                                    localurl = msgs["media_name"]
                                except:
                                    localurl = None
                        except:
                            try:
                                localurl = msgs["media_name"]
                            except:
                                localurl = None

                        # Thumbnail
                        try:
                            thumbnaildata = msgs["raw_data"]
                        except:
                            thumbnaildata = None

                        # Audio / Video duration
                        try:
                            mduration =  msgs["media_duration"]
                        except:
                            mduration = None


                        # By Group (status = 6) is key_from_me always 1
                        # thats not allways right
                        if msgs["key_from_me"] == 1 and msgs["status"] != 6:
                        #if msgs["key_from_me"] == 1:
                            contactfrom = "me"

                        if contactfrom != "me" and have_wa:
                            # message sender NICK
                            try:
                                w2.execute("SELECT wa_name FROM wa_contacts WHERE jid=? ORDER BY _id ASC;", [contactfrom])
                                contactfromNICK = w2.fetchone()[0]
                                if contactfromNICK == "" or contactfromNICK is None:
                                    contactfromNICK = contactfrom
                            except:
                                contactfromNICK = None
                                if msgs["key_from_me"] == 1:
                                    contactfrom = "me"
                                    if db_owner_name != "":
                                        contactfromNICK = db_owner_name


                        # GroupMember encode('utf-8')
                        try:
                            GroupMemberX = printable(msgs["thumb_image"])

                            if GroupMemberX.find("s.whatsapp.net") >0:
                                if GroupMemberX.find("lxpt") >0:
                                    posStart=GroupMemberX.find("lxpt")+4
                                    posEnd=GroupMemberX.find("s.whatsapp.net")-1
                                    GroupMember = GroupMemberX[posStart:posEnd]

                                if GroupMemberX.find("xpwt") >0:
                                    posStart=GroupMemberX.find("xpwt")+4
                                    posEnd=GroupMemberX.find("s.whatsapp.net")-1
                                    GroupMember = GroupMemberX[posStart:posEnd]
                            # or in the future like me_owner
                            # find("\x00\x1B")
                            # find("\x00\x1C")
                            else:
                                GroupMember = ""
                        except:
                            GroupMember = ""

                        # remote_resource
                        try:
                            RemoteResource = msgs["remote_resource"]
                        except:
                            RemoteResource = None


                        # Group analysis
                        if msgs["key_remote_jid"].find("@g.us") != -1:
                            ChatIsGroup = True
                        else:
                            ChatIsGroup = False

                        GM_display_name = ""
                        GM_wa_name = ""

                        GroupMemberID = ""      # "phone@s.whatsapp.net"
                        GroupMemberStatus = 0   # 0 sent
                                                # 1 create / change Group
                                                # 2 change Picture
                                                # 3 add (join)
                                                # 4 left



                         # add more Group Information - Android
                         # new Group-Status
                        if msgs["status"] == 6:

                            if RemoteResource == "" or RemoteResource is None:
                                RemoteResource ="@"

                            if msgs["media_size"] == 1:
                                #messagedata = "Chat-Group was created or changed from User '{}' to '{}'.".format(contactfrom.split("@")[0], msgs["data"])
                                messagedata = "Chat-Group was created or changed from User '{}' to '{}'.".format(RemoteResource.split("@")[0], msgs["data"])
                                GroupMemberID = RemoteResource
                                GroupMemberStatus = 1

                            elif msgs["media_size"] == 11:
                                messagedata = "Chat-Group was created or changed from User '{}' to '{}'.".format(RemoteResource.split("@")[0], msgs["data"])
                                GroupMemberID = RemoteResource
                                GroupMemberStatus = 1

                            elif msgs["media_size"] == 19:
                                #messagedata = "🔒 Nachrichten, die du in diesem Chat sendest,<br \>sowie Anrufe sind jetzt mit Ende-zu-Ende-<br \>Verschlüsselung geschützt. Tipp für mehr Infos."
                                messagedata = "🔒 Messages you send to this chat and calls are <br \>now secured with end-to-end encryption. <br \>Tap for more info."

                                GroupMemberID = RemoteResource
                                GroupMemberStatus = 1
                            elif msgs["media_size"] == 4:
                                messagedata = "User '{}' joins the group.".format(RemoteResource.split("@")[0])
                                GroupMemberID = RemoteResource
                                GroupMemberStatus = 3

                            elif msgs["media_size"] == 12:
                                if len(RemoteResource) > 5:
                                    messagedata = "User '{}' joins the group. Initiated by '{}'".format(GroupMember, RemoteResource.split("@")[0])
                                    GroupMemberID = GroupMember + "@s.whatsapp.net"
                                    GroupMemberStatus = 3
                                else:
                                    messagedata = "User '{}' joins the group.".format(GroupMember)
                                    GroupMemberID = GroupMember + "@s.whatsapp.net"
                                    GroupMemberStatus = 3

                            elif msgs["media_size"] == 5:
                                messagedata = "User '{}' has left the group.".format(RemoteResource.split("@")[0])
                                GroupMemberID = RemoteResource
                                GroupMemberStatus = 4

                            elif msgs["media_size"] == 14: # not veryfied
                                if len(RemoteResource) > 5:
                                    messagedata = "User '{}' was removed from group. Initiated by '{}'".format(GroupMember, RemoteResource.split("@")[0])
                                    GroupMemberID = GroupMember + "@s.whatsapp.net"
                                    GroupMemberStatus = 4
                                else:
                                    messagedata = "User '{}' was removed from group.".format(GroupMember)
                                    GroupMemberID = GroupMember + "@s.whatsapp.net"
                                    GroupMemberStatus = 4

                            elif msgs["media_size"] == 6:
                                messagedata = "User '{}' has changed the group picture. Time: '{}'".format(RemoteResource.split("@")[0], convertTimeStamp(msgs["data"]))
                                GroupMemberID = RemoteResource
                                GroupMemberStatus = 2
                            else:
                                messagedata = msgs["data"]
                                GroupMemberID = RemoteResource
                                GroupMemberStatus = 0
                        else:
                            messagedata = msgs["data"]
                            GroupMemberID = RemoteResource
                            GroupMemberStatus = 0


                        # broadcast Information
                        if broadcast != None:
                            broadcasttime = convertTimeStamp(broadcast.split("@")[0])
                            messagedata = "<b>[Broadcast send {}]</b> </br>{}".format(broadcasttime, messagedata)

                        try:
                            msgmediacaption = msgs["media_caption"]
                        except:
                            msgmediacaption = None

                        if (contactfrom == "me") and (db_owner_name != ""):
                            contactfromNICK = db_owner_name


                       #curr_message = Message(msgs["_id"],msgs["key_from_me"],msgs["timestamp"],msgs["data"],contactfrom,None,msgs["status"],msgs["media_name"],msgs["media_url"],thumbnaildata,None,msgs["media_wa_type"],msgs["media_size"],mduration,msgs["latitude"],msgs["longitude"],None,None)
                        curr_message = Message(msgs["_id"],msgs["key_from_me"],msgs["timestamp"],messagedata,contactfrom,contactfromNICK,msgs["status"],localurl,msgs["media_url"],msgmediacaption,thumbnaildata,None,msgs["media_wa_type"],msgs["media_size"],mduration,msgs["latitude"],msgs["longitude"],None,None,None,GroupMember)

                        if ChatIsGroup:
                            GM_display_name = contactfrom
                            GM_wa_name = contactfromNICK

                    #--------------------------------------------------------------
                    elif mode == IPHONE:
                        #  IPHONE ChatStorage.sqlite file *** ZWACHATSESSION TABLE  #
                        # ------------------------------------------------------- #
                        # ------------------------------------------------------- #
                        # msgs[0] --> Z_PK (primary key)
                        # msgs[1] --> Z_ENT
                        # msgs[2] --> Z_OPT
                        # msgs[3] --> ZISFROMME
                        # msgs[4] --> ZSORT
                        # msgs[5] --> ZMESSAGESTATUS
                        # msgs[6] --> ZMESSAGETYPE
                        # msgs[7] --> ZMEDIAITEM
                        # msgs[8] --> ZCHATSESSION
                        # msgs[9] --> ZMESSAGEDATE
                        # msgs[10] -> ZTEXT
                        # msgs[11] -> ZTOJID
                        # msgs[12] -> ZFROMJID
                        # msgs[13] -> ZSTANZAID

                        #          -> ZGROUPEVENTTYPE
                        #          -> ZGROUPMEMBER

                        contactfromjid =""
                        if msgs["ZISFROMME"] == 1:
                            contactfrom = "me"
                        else:
                            if msgs["ZGROUPMEMBER"] is None:
                                contactfrom = msgs["ZFROMJID"]
                                contactfromjid = ""
                            else:
                                c3.execute("SELECT * FROM ZWAGROUPMEMBER WHERE Z_PK=?;", [msgs["ZGROUPMEMBER"]])
                                contactgroupid = c3.fetchone()
                                contactfrom = contactgroupid["ZCONTACTNAME"]
                                contactfromjid = contactgroupid["ZMEMBERJID"]

                        # Group analysis
                        ChatIsGroup = False
                        if msgs["ZFROMJID"] is not None:
                            if msgs["ZFROMJID"].find("@g.us") != -1:
                                ChatIsGroup = True
                        if msgs["ZTOJID"] is not None:
                            if msgs["ZTOJID"].find("@g.us") != -1:
                                ChatIsGroup = True






                        GM_display_name = ""
                        GM_wa_name = ""


                        GroupMemberID = ""      # "phone@s.whatsapp.net"
                        GroupMemberStatus = 0   # 0 sent
                                                # 1 create / change Group
                                                # 2 change Picture
                                                # 3 add (join)
                                                # 4 left / deleted


                        # add more Group Information
                        # verified on iPhone
                        if msgs["ZMESSAGETYPE"] == 6:
                            if contactfromjid == "":
                                member="ITSELF"
                                GroupMemberID = contactfrom
                            else:
                                member=contactfromjid.split("@")[0]
                                GroupMemberID = contactfromjid



                            if msgs["ZGROUPEVENTTYPE"] == 1:
                                messagedata = "Subject was changed from User '{}' to '{}'.".format(member, msgs["ZTEXT"])
                                GroupMemberStatus = 1
                            elif msgs["ZGROUPEVENTTYPE"] == 12: #changed Group Title and joind Group ?
                                messagedata = "Subject was changed from User '{}' to '{}'.".format(member, msgs["ZTEXT"])
                                GroupMemberStatus = 1
                            elif msgs["ZGROUPEVENTTYPE"] == 2:
                                messagedata = "User '{}' joins the group.".format(member)
                                GroupMemberStatus = 3
                            elif msgs["ZGROUPEVENTTYPE"] == 3:
                                messagedata = "User '{}' has left the group.".format(member)
                                GroupMemberStatus = 4
                            elif msgs["ZGROUPEVENTTYPE"] == 4:
                                messagedata = "User '{}' has changed the group picture.".format(member)
                                GroupMemberStatus = 2
                            elif msgs["ZGROUPEVENTTYPE"] == 7:
                                messagedata = "User '{}' was removed from group.".format(member)
                                GroupMemberStatus = 4
                            else:
                                messagedata = msgs["ZTEXT"]
                        else:
                            messagedata = msgs["ZTEXT"]

                        if ChatIsGroup:
                            GroupMemberID = contactfromjid
                            GM_display_name = contactfrom
                            GM_wa_name = msgs["ZPUSHNAME"]

                            # correction - not in Adressbook
                            if msgs["ZGROUPMEMBER"] is not None:
                                c3.execute("SELECT * FROM ZWAGROUPMEMBER WHERE Z_PK=?;", [msgs["ZGROUPMEMBER"]])
                                contactgroupid = c3.fetchone()
                                if contactgroupid["ZCONTACTABID"] == 0:
                                    GM_display_name = ""
                                    GM_wa_name = contactfrom

                            # correction - me
                            if msgs["ZISFROMME"] == 1 or member == "ITSELF":
                                GM_display_name = "me"


                        # iPhone Media
                        if msgs["ZMEDIAITEM"] is None:
                            try:
                                mediawatype = msgs["ZMESSAGETYPE"]
                            except:
                                mediawatype = None

                            # Status Messeges
                            if int(mediawatype) == 10:
                                if int(msgs["Z_OPT"]) == 2:      # Chat now end-to-end encrypted
                                    if msgs["ZGROUPEVENTTYPE"] == 2:
                                        #messagedata = "🔒 Nachrichten, die du in diesem Chat sendest, <br \>sowie Anrufe sind jetzt mit Ende-zu-Ende-<br \>Verschlüsselung geschützt. Tippen Sie für mehr Infos."
                                        messagedata = "🔒 Messages you send to this chat and calls are <br \>now secured with end-to-end encryption. <br \>Tap for more info."
                                    elif msgs["ZGROUPEVENTTYPE"] == 3:
                                        #messagedata = "Die Sicherheitsnummer von {}<br \>hat sich geändert. Tippen Sie für mehr Infos.".format(chats.contact_name)
                                        messagedata = "The security number of {} has changed. <br \>Tap for more info.".format(chats.contact_name)
                                    else:
                                        messagedata = "Encryption status messages ({}) unknown.".format(msgs["ZGROUPEVENTTYPE"])

                                elif int(msgs["Z_OPT"]) == 3:    # Missed Call at [Time] hh:mm - msgs["ZMESSAGEDATE"] - [11:16]
                                    messagedata = "Missed Call at " + str(datetime.datetime.fromtimestamp(int(msgs["ZMESSAGEDATE"])+11323*60*1440))[11:16]
                            curr_message = Message(msgs["Z_PK"],msgs["ZISFROMME"],msgs["ZMESSAGEDATE"],messagedata,contactfrom,msgs["ZPUSHNAME"],msgs["ZMESSAGESTATUS"],None,None,None,None,None,msgs["ZMESSAGETYPE"],None,None,None,None,None,None,msgs["ZGROUPEVENTTYPE"],contactfromjid)
                        else:
                            try:
                                messagedata = str(msgs["ZTEXT"])

                            except:
                                messagedata = ""

                            try:
                                c2.execute("SELECT * FROM ZWAMEDIAITEM WHERE Z_PK=?;", [msgs["ZMEDIAITEM"]])
                                media = c2.fetchone()
                                # ------------------------------------------------------- #
                                #  IPHONE ChatStorage.sqlite file *** ZWAMEDIAITEM TABLE  #
                                # ------------------------------------------------------- #
                                # Z_PK INTEGER PRIMARY KEY
                                # Z_ENT INTEGER
                                # Z_OPT INTEGER
                                # ZMOVIEDURATION INTEGER
                                # ZMEDIASAVED INTEGER
                                # ZFILESIZE INTEGER
                                # ZMESSAGE INTEGER
                                # ZLONGITUDE FLOAT
                                # ZHACCURACY FLOAT
                                # ZLATITUDE FLOAT
                                # ZVCARDSTRING VARCHAR
                                # ZXMPPTHUMBPATH VARCHAR
                                # ZMEDIALOCALPATH VARCHAR
                                # ZMEDIAURL VARCHAR
                                # ZVCARDNAME VARCHAR
                                # ZTHUMBNAILLOCALPATH VARCHAR
                                # ZTHUMBNAILDATA BLOB
                                try:
                                    movieduration = media["ZMOVIEDURATION"]
                                except:
                                    movieduration = None
                                try:
                                    mediawatype = msgs["ZMESSAGETYPE"]
                                except:
                                    mediawatype = None
                                try:
                                    ZXMPPTHUMBPATH = media["ZXMPPTHUMBPATH"]
                                except:
                                    ZXMPPTHUMBPATH = None
                                # correction of beginnig
                                if ZXMPPTHUMBPATH != None:
                                    if len(ZXMPPTHUMBPATH) > 0:
                                        if ZXMPPTHUMBPATH[0] == "/":
                                            ZXMPPTHUMBPATH = ZXMPPTHUMBPATH[1:]

                                # media_caption
                                if media["ZTITLE"] == "" or media["ZTITLE"] is None:
                                    media_caption = ""
                                else:
                                    media_caption = media["ZTITLE"]

                                # curr_message = Message(msgs["Z_PK"],msgs["ZISFROMME"],msgs["ZMESSAGEDATE"],msgs["ZTEXT"],contactfrom,msgs["ZPUSHNAME"],msgs["ZMESSAGESTATUS"],media["ZMEDIALOCALPATH"],media["ZMEDIAURL"],media["ZTHUMBNAILDATA"],ZXMPPTHUMBPATH,mediawatype,media["ZFILESIZE"],media["ZLATITUDE"],media["ZLONGITUDE"],media["ZVCARDNAME"],media["ZVCARDSTRING"])
                                # new Database Schema
                                curr_message = Message(msgs["Z_PK"],msgs["ZISFROMME"],msgs["ZMESSAGEDATE"],messagedata,contactfrom,msgs["ZPUSHNAME"],msgs["ZMESSAGESTATUS"],media["ZMEDIALOCALPATH"],media["ZMEDIAURL"],media_caption,None,ZXMPPTHUMBPATH,mediawatype,media["ZFILESIZE"],movieduration,media["ZLATITUDE"],media["ZLONGITUDE"],media["ZVCARDNAME"],media["ZVCARDSTRING"],msgs["ZGROUPEVENTTYPE"],contactfromjid)

                            except TypeError as msg:
                                print('Error TypeError while reading media message #{0} in chat #{1}: {2}'.format(count_messages, chats.pk_cs, msg) + "\nI guess this means that the media part of this message can't be found in the DB")
                                curr_message = Message(msgs["Z_PK"],msgs["ZISFROMME"],msgs["ZMESSAGEDATE"],messagetext + "<br>MediaMessage_Error: see output in DOS window",contactfrom,msgs["ZPUSHNAME"],msgs["ZMESSAGESTATUS"],None,None,None,None,None,None,None,None,None,None,None,None,None,None)
                            except sqlite3.Error as msg:
                                print('Error sqlite3.Error while reading media message #{0} in chat #{1}: {2}'.format(count_messages, chats.pk_cs, msg))
                                curr_message = Message(msgs["Z_PK"],msgs["ZISFROMME"],msgs["ZMESSAGEDATE"],messagetext + "<br>MediaMessage_Error: see output in DOS window",contactfrom,msgs["ZPUSHNAME"],msgs["ZMESSAGESTATUS"],None,None,None,None,None,None,None,None,None,None,None,None,None,None)
                    #--end if------------------------------------------------------------

                except sqlite3.Error as msg:
                    print('Error while reading message #{0} in chat #{1}: {2}'.format(count_messages, chats.pk_cs, msg))
                    curr_message = Message(None,None,None,"_Error: sqlite3.Error, see output in DOS window",None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None)
                except TypeError as msg:
                    print('Error while reading message #{0} in chat #{1}: {2}'.format(count_messages, chats.pk_cs, msg))
                    curr_message = Message(None,None,None,"_Error: TypeError, see output in DOS window",None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None)

                chats.msg_list.append(curr_message)

                # Android and iPhone
                # chat session is Group
                if ChatIsGroup:
                    NewGM = True

                    # Update
                    try:
                        for GM in GroupMembers:
                            if (GM.group_member_jid == GroupMemberID) or ((GM.display_name == GM_display_name) and GM_display_name=="me"):
                                NewGM = False
                                # Update DATA

                                if GroupMemberStatus == 0: # sent
                                    GM.has_send = GM.has_send +1
                                elif GroupMemberStatus == 1: # 1 create / change Group
                                    GM.has_changed_Group = GM.has_changed_Group +1
                                elif GroupMemberStatus == 2: # 2 change Picture
                                    GM.has_changed_GroupPicture = GM.has_changed_GroupPicture +1
                                elif GroupMemberStatus == 3: # 3 add (join)
                                    GM.is_added = GM.is_added +1
                                elif GroupMemberStatus == 4: # 4 left
                                    GM.is_deleted = GM.is_deleted +1
                    except:
                        pass

                    # New
                    if NewGM:
                        # NEW - GroupMembers not in List
                        #GM_display_name = ""
                        #GM_wa_name = ""
                        #GroupMemberID = ""
                        #GroupMemberStatus = 0

                        #

                        # Display Name
                        for n in chat_session_list:
                            if n.contact_id == GroupMemberID:
                                GM_display_name = n.contact_name
                                GM_wa_name = n.wa_name

                        if "@g.us" not in GM_display_name:





                            if GroupMemberStatus == 0: # sent
                                GM_sent=1
                            else:
                                GM_sent=0
                            if GroupMemberStatus == 1: # 1 create / change Group
                                GM_change_Group=1
                            else:
                                GM_change_Group=0
                            if GroupMemberStatus == 2: # 2 change Picture
                                GM_change_Picture=1
                            else:
                                GM_change_Picture=0
                            if GroupMemberStatus == 3: # 3 add (join)
                                GM_add=1
                            else:
                                GM_add=0
                            if GroupMemberStatus == 4: # 4 left
                                GM_left=1
                            else:
                                GM_left=0

                            # me - correction
                            if GM_display_name == "me":
                                GroupMemberID = db_owner
                                GM_wa_name = db_owner_name
                            if GroupMemberID == db_owner:
                                GM_display_name =  "me"
                                GM_wa_name = db_owner_name

                            curr_member=GMembers(GroupMemberID, GM_display_name, GM_wa_name, GM_sent, GM_change_Group, GM_change_Picture, GM_add, GM_left)
                            GroupMembers.append(curr_member)
            chats.contact_msg_count = count_messages

            # chat session is Group
            if ChatIsGroup:
                # chat session add all Groupmebers found
                chats.members = len(GroupMembers)
                chats.gms_list = GroupMembers


        except sqlite3.Error as msg:
            print('Error sqlite3.Error while reading chat #{0}: {1}'.format(chats.pk_cs, msg))
            sys.exit(1)
        except TypeError as msg:
            print('Error TypeError while reading chat #{0}: {1}'.format(chats.pk_cs, msg))
            sys.exit(1)

    # gets the db owner id
    try:
        if mode == ANDROID:
            #c1.execute("SELECT key_remote_jid FROM messages WHERE key_from_me=1 AND key_remote_jid LIKE '%@s.whatsapp.net%' ")
            #doesn't work
            owner = ""
        elif mode == IPHONE:
            c1.execute("SELECT ZFROMJID FROM ZWAMESSAGE WHERE ZISFROMME=1")
        try:
            owner = (c1.fetchone()[0]).split('/')[0]
        except:
            owner = ""
    except sqlite3.Error as msg:
        print('Error: {0}'.format(msg))

    # OUTPUT
    # multiple Files
    print("Generating html files")

    if (GetPath(outfile)!=""):
        copyDirectory("data",GetPath(outfile)+"/data")

    #  output filename unify - on manually entcrypted .crypt5 Databses
    if outfile == "msgstore.db.db":
        outfile = options.infile.replace("msgstore.db.db","msgstore.db")

    main_file_name = '%s.html' % outfile

    # replace ".plain" in Filenames and Links
    main_file_name = main_file_name.replace(".plain.",".")
    outfile = outfile.replace(".plain.",".")

    # DB owner name Android (dosnÂ´t work) and iPhone (blank)
    # Open main file, give it the DB owner name

    # OLD B - One File
    one_file_name = '%s.html' % outfile
    one_file = outputfile_open(one_file_name, None)

    # OLD A - multible Files
    # Open main file
    main_file_name = '%s.main.html' % outfile
    main_file = outputfile_open(main_file_name, None)

    if have_groups:
        main_file_name_group = main_file_name.replace(".html",".G.html")
        one_file_name_group = one_file_name.replace(".html",".G.html")

        main_file_group = outputfile_open(main_file_name_group, "NTF, GAI")
        one_file_group = outputfile_open(one_file_name_group, "NTF, GAI")

    if have_groups:
        outputfileAB(main_file, '<h3><a href="{0}">Return to overview</a> &nbsp;&nbsp;&nbsp; <a href="{1}">GROUP analysis</a></h3>'.format( GetBase(one_file_name), GetBase(main_file_name_group) ).encode( 'utf-8' ) )
        outputfileAB(one_file, '<h3><a href="{0}">Only index</a> &nbsp;&nbsp;&nbsp; <a href="{1}">GROUP analysis</a></h3>'.format( GetBase(main_file_name), GetBase(one_file_name_group) ).encode( 'utf-8' ) )
    else:
        outputfileAB(main_file, '<h3><a href="{0}">Return to overview</a></h3>'.format( GetBase(one_file_name) ).encode( 'utf-8' ) )
        outputfileAB(one_file, '<h3><a href="{0}">Only index</a></h3>'.format( GetBase(main_file_name) ).encode( 'utf-8' ) )

    # writes 1st table header "CHAT SESSION"
    outputfileAB(main_file, one_file, '<table class="sortable" id="chatsession" border="1" cellpadding="2" cellspacing="0">\n'.encode('utf-8'))
    outputfileAB(main_file, one_file, '<thead>\n'.encode('utf-8'))
    outputfileAB(main_file, one_file, '<tr>\n'.encode('utf-8'))
    outputfileAB(main_file, one_file, '<th>PK</th>\n'.encode('utf-8'))
    outputfileAB(main_file, one_file, '<th>Contact Name</th>\n'.encode('utf-8'))
    outputfileAB(main_file, one_file, '<th>Contact ID</th>\n'.encode('utf-8'))
    outputfileAB(main_file, one_file, '<th>Status</th>\n'.encode('utf-8'))
    outputfileAB(main_file, one_file, '<th># Msg</th>\n'.encode('utf-8'))
    outputfileAB(main_file, one_file, '<th># Unread Msg</th>\n'.encode('utf-8'))
    outputfileAB(main_file, one_file, '<th>Last Message</th>\n'.encode('utf-8'))
    outputfileAB(main_file, one_file, '</tr>\n'.encode('utf-8'))
    outputfileAB(main_file, one_file, '</thead>\n'.encode('utf-8'))

    if have_groups:
        outputfileAB(main_file_group, '<h3><a href="{0}">Return to GROUP overview</a> &nbsp;&nbsp;&nbsp; <a href="{1}">Return to Chats</a></h3>'.format( GetBase(one_file_name_group), GetBase(main_file_name) ).encode( 'utf-8' ) )
        outputfileAB(one_file_group, '<h3><a href="{0}">Only GROUP index</a> &nbsp;&nbsp;&nbsp; <a href="{1}">Return to Chats</a></h3>'.format( GetBase(main_file_name_group), GetBase(one_file_name) ).encode( 'utf-8' ) )

        # writes 1st table header "CHAT SESSION"
        outputfileAB(main_file_group, one_file_group, '<table class="sortable" id="chatsession" border="1" cellpadding="2" cellspacing="0">\n'.encode('utf-8'))
        outputfileAB(main_file_group, one_file_group, '<thead>\n'.encode('utf-8'))
        outputfileAB(main_file_group, one_file_group, '<tr>\n'.encode('utf-8'))
        outputfileAB(main_file_group, one_file_group, '<th>PK</th>\n'.encode('utf-8'))
        outputfileAB(main_file_group, one_file_group, '<th>Contact Name</th>\n'.encode('utf-8'))
        outputfileAB(main_file_group, one_file_group, '<th>Contact ID</th>\n'.encode('utf-8'))
        outputfileAB(main_file_group, one_file_group, '<th># Members</th>\n'.encode('utf-8'))
        outputfileAB(main_file_group, one_file_group, '<th># Msg</th>\n'.encode('utf-8'))
        outputfileAB(main_file_group, one_file_group, '<th># Unread Msg</th>\n'.encode('utf-8'))
        outputfileAB(main_file_group, one_file_group, '<th>Last Message</th>\n'.encode('utf-8'))
        outputfileAB(main_file_group, one_file_group, '</tr>\n'.encode('utf-8'))
        outputfileAB(main_file_group, one_file_group, '</thead>\n'.encode('utf-8'))

    # writes 1st table content
    outputfileAB(main_file, one_file, '<tbody>\n'.encode('utf-8'))

    if have_groups:
        # writes 1st table content
        outputfileAB(main_file_group, one_file_group, '<tbody>\n'.encode('utf-8'))


    for i in chat_session_list:

        #No Output when no message width contact
        if i.contact_msg_count == 0:
            continue;

        #TimeFilter enable
        if have_tf:
            try:
                tsmgs = totimestamp(i.last_message_date)
            except:
                #Debug
                print("#" + i.last_message_date + "# - " + i.contact_id)
                continue

            #if not ((tsmgs >= tsFrom) and (tsmgs <= tsTo)):
            if not ((tsmgs >= tsFrom)):
                continue

        if i.contact_name == "N/A":

            # use Contact-id if we can
            try:
                i.contact_name = i.contact_id.split('@')[0]
            except:
                i.contact_name = i.contact_id
            contactname = i.contact_name
        else:
            contactname = convertsmileys ( i.contact_name ) # chat name

        if i.wa_name != "N/A":
            Cnickname = " ({})".format(convertsmileys ( i.wa_name ))
        else:
            Cnickname =""

        contactstatus = convertsmileys ( str(i.contact_status) )
        lastmessagedate = i.last_message_date

        outputfileAB(main_file, one_file, '<tr>\n'.encode('utf-8'))
        outputfileAB(main_file, one_file, '<td>{0}</td>\n'.format(i.pk_cs).encode('utf-8'))
        outputfileAB(main_file, one_file, '<td class="contact"><a href="{0}.{1}.html">{2}</a>{3} | <a href="{0}.{1}.media.html">Media</a></td>\n'.format(GetBase(outfile),i.contact_id.split('@')[0],contactname, Cnickname).encode('utf-8'))
        outputfileAB(main_file, one_file, '<td class="contact">{0}</td>\n'.format(i.contact_id).encode('utf-8'))
        outputfileAB(main_file, one_file, '<td>{0}</td>\n'.format(contactstatus).encode('utf-8'))
        outputfileAB(main_file, one_file, '<td>{0}</td>\n'.format(i.contact_msg_count).encode('utf-8'))
        outputfileAB(main_file, one_file, '<td>{0}</td>\n'.format(i.contact_unread_msg).encode('utf-8'))
        outputfileAB(main_file, one_file, '<td>{0}</td>\n'.format(lastmessagedate).encode('utf-8'))
        outputfileAB(main_file, one_file, '</tr>\n'.encode('utf-8'))

        if have_groups and i.contact_id.find("@g.us") != -1:
            outputfileAB(main_file_group, one_file_group, '<tr>\n'.encode('utf-8'))
            outputfileAB(main_file_group, one_file_group, '<td>{0}</td>\n'.format(i.pk_cs).encode('utf-8'))
            outputfileAB(main_file_group, one_file_group, '<td class="contact"><a href="{0}.{1}.G.html">{2}</a>{3} </td>\n'.format(GetBase(outfile),i.contact_id.split('@')[0],contactname, Cnickname).encode('utf-8'))
            outputfileAB(main_file_group, one_file_group, '<td class="contact">{0}</td>\n'.format(i.contact_id).encode('utf-8'))
            outputfileAB(main_file_group, one_file_group, '<td>{0}</td>\n'.format(i.members).encode('utf-8'))
            outputfileAB(main_file_group, one_file_group, '<td>{0}</td>\n'.format(i.contact_msg_count).encode('utf-8'))
            outputfileAB(main_file_group, one_file_group, '<td>{0}</td>\n'.format(i.contact_unread_msg).encode('utf-8'))
            outputfileAB(main_file_group, one_file_group, '<td>{0}</td>\n'.format(lastmessagedate).encode('utf-8'))
            outputfileAB(main_file_group, one_file_group, '</tr>\n'.encode('utf-8'))

    outputfileAB(main_file, one_file, '</tbody>\n'.encode('utf-8'))
    # writes 1st table footer
    outputfileAB(main_file, one_file, '</table>\n'.encode('utf-8'))

    # Close main file
    outputfile_close(main_file)

    if have_groups:
        outputfileAB(main_file_group, one_file_group, '</tbody>\n'.encode('utf-8'))
        # writes 1st table footer
        outputfileAB(main_file_group, one_file_group, '</table>\n'.encode('utf-8'))

        # Close main file
        outputfile_close(main_file_group)

    global content_type

    # creates a chat file for each chat session
    for i in chat_session_list:#

        #No Output when no message width contact
        #if i.contact_msg_count == 0:
        #    continue;

        chat_file_name = '{0}.{1}.html'.format(outfile,i.contact_id.split('@')[0])
        chat_file = outputfile_open(chat_file_name, None)

        chat_media_file_name = '{0}.{1}.media.html'.format(outfile,i.contact_id.split('@')[0])
        chat_media_file = outputfile_open(chat_media_file_name, None)

        if have_groups and i.contact_id.find("@g.us") != -1:
            chat_file_name_group = '{0}.{1}.G.html'.format(outfile,i.contact_id.split('@')[0])
            chat_file_group = outputfile_open(chat_file_name_group, "NTF, GAI")

        #contactname = convertsmileys ( i.contact_name ) # chat name
        if i.contact_name == "N/A":

            # use Contact-id if we can
            try:
                i.contact_name = i.contact_id.split('@')[0]
            except:
                i.contact_name = i.contact_id
            contactname = i.contact_name
        else:
            contactname = convertsmileys ( i.contact_name ) # chat name

        try:
            chatid = i.contact_id.split('@')[0]
        except:
            chatid = i.contact_id

        outputfileAB(chat_file, '<h3><a href="{0}.{1}.media.html">Media index</a></h3>'.format(GetBase(outfile),chatid).encode('utf-8'))
        outputfileAB(chat_file, '<h3><a href="{0}">Return to index</a></h3>'.format( GetBase(main_file_name) ).encode( 'utf-8' ) )
        outputfileAB(chat_file, '<h3><a href="{0}">Return to overview</a></h3>'.format(GetBase(one_file_name)).encode('utf-8'))
        # add contact ID only when not equil
        if str(i.contact_name) == str(i.contact_id.split('@')[0]):
            outputfileAB(chat_file, one_file, '<h3>Chat session #{0}: <a name="{1}">{2}</a></h3>\n'.format(i.pk_cs, i.contact_name, contactname).encode('utf-8'))
        else:
            outputfileAB(chat_file, one_file, '<h3>Chat session #{0}: <a name="{1}">{2}</a> - {3}</h3>\n'.format(i.pk_cs, i.contact_name, contactname, i.contact_id.split('@')[0]).encode('utf-8'))

        # Group Information
        GAdmin, GCreationTime = GroupInfo(i.contact_id)
        if GAdmin is not None:
            outputfileAB(chat_file, one_file, '<h3>Group Creation-Time: {1} - Group Admin: {0}</h3>\n'.format(GAdmin, GCreationTime).encode('utf-8'))

        if have_groups and i.contact_id.find("@g.us") != -1:
            outputfileAB(chat_file_group, '<h3><a href="{0}">Return to GROUP index</a></h3>'.format( GetBase(main_file_name_group) ).encode( 'utf-8' ) )
            outputfileAB(chat_file_group, '<h3><a href="{0}">Return to GROUP overview</a></h3>'.format(GetBase(one_file_name_group)).encode('utf-8'))
            # add contact ID only when not equil
            if str(i.contact_name) == str(i.contact_id.split('@')[0]):
                outputfileAB(chat_file_group, one_file_group, '<h3>Chat session #{0}: <a name="{1}">{2}</a></h3>\n'.format(i.pk_cs, i.contact_name, contactname).encode('utf-8'))
            else:
                outputfileAB(chat_file_group, one_file_group, '<h3>Chat session #{0}: <a name="{1}">{2}</a> - {3}</h3>\n'.format(i.pk_cs, i.contact_name, contactname, i.contact_id.split('@')[0]).encode('utf-8'))

            # Group Information
            GAdmin, GCreationTime = GroupInfo(i.contact_id)
            if GAdmin is not None:
                outputfileAB(chat_file_group, one_file_group, '<h3>Group Creation-Time: {1} - Group Admin: {0} - Members found: {2}</h3>\n'.format(GAdmin, GCreationTime, i.members).encode('utf-8'))

            outputfileAB(chat_file_group, one_file_group, '<table class="sortable" id="msg_{0}" border="1" cellpadding="2" cellspacing="0">\n'.format(chatid).encode('utf-8'))
            outputfileAB(chat_file_group, one_file_group, '<thead>\n'.encode('utf-8'))
            outputfileAB(chat_file_group, one_file_group, '<tr>\n'.encode('utf-8'))
            outputfileAB(chat_file_group, one_file_group, '<th>Member ID</th>\n'.encode('utf-8'))
            outputfileAB(chat_file_group, one_file_group, '<th>Display Name</th>\n'.encode('utf-8'))
            outputfileAB(chat_file_group, one_file_group, '<th>Nick</th>\n'.encode('utf-8'))
            outputfileAB(chat_file_group, one_file_group, '<th># Msg sent</th>\n'.encode('utf-8'))
            outputfileAB(chat_file_group, one_file_group, '<th># Change Group Name</th>\n'.encode('utf-8'))
            outputfileAB(chat_file_group, one_file_group, '<th># Change Group Picture</th>\n'.encode('utf-8'))
            outputfileAB(chat_file_group, one_file_group, '<th># is added</th>\n'.encode('utf-8'))
            outputfileAB(chat_file_group, one_file_group, '<th># is deleted</th>\n'.encode('utf-8'))
            outputfileAB(chat_file_group, one_file_group, '</tr>\n'.encode('utf-8'))
            outputfileAB(chat_file_group, one_file_group, '</thead>\n'.encode('utf-8'))

            for z in i.gms_list:
                #Row-Color
                # row class selection
                if z.display_name == "N/A": # CONTENT_NEWGROUPNAME
                   outputfileAB(chat_file_group, one_file_group, '<tr class="newgroupname">\n'.encode('utf-8'))
                elif z.display_name == "me":
                    outputfileAB(chat_file_group, one_file_group, '<tr class="me">\n'.encode('utf-8'))
                else:
                    outputfileAB(chat_file_group, one_file_group, '<tr class="other">\n'.encode('utf-8'))

                # Member ID
                outputfileAB(chat_file_group, one_file_group, '<td>{0}</td>\n'.format(z.group_member_jid).encode('utf-8'))

                displayname = convertsmileys ( z.display_name ) # chat display-name
                outputfileAB(chat_file_group, one_file_group, '<td class="contact">{0}</td>\n'.format(displayname).encode('utf-8'))

                # Whatsapp Name
                nickname = convertsmileys ( z.wa_name ) # chat nick-name
                outputfileAB(chat_file_group, one_file_group, '<td class="contact">{0}</td>\n'.format(nickname).encode('utf-8'))

                # Msg sent
                outputfileAB(chat_file_group, one_file_group, '<td>{0}</td>\n'.format(str(z.has_send)).encode('utf-8'))

                # Change Group Name
                outputfileAB(chat_file_group, one_file_group, '<td>{0}</td>\n'.format(str(z.has_changed_Group)).encode('utf-8'))

                # Change Group Picture
                outputfileAB(chat_file_group, one_file_group, '<td>{0}</td>\n'.format(str(z.has_changed_GroupPicture)).encode('utf-8'))

                # is added
                outputfileAB(chat_file_group, one_file_group, '<td>{0}</td>\n'.format(str(z.is_added)).encode('utf-8'))

                # is deleted (left / removed)
                outputfileAB(chat_file_group, one_file_group, '<td>{0}</td>\n'.format(str(z.is_deleted)).encode('utf-8'))

                # Row End
                outputfileAB(chat_file_group, one_file_group, '</tr>\n'.encode('utf-8'))

            # writes table-body footer
            outputfileAB(chat_file_group, one_file_group, '</tbody>\n'.encode('utf-8'))
            # writes table footer
            outputfileAB(chat_file_group, one_file_group, '</table>\n'.encode('utf-8'))

            # #####

        outputfileAB(chat_file, one_file, '<table class="sortable" id="msg_{0}" border="1" cellpadding="2" cellspacing="0">\n'.format(chatid).encode('utf-8'))
        outputfileAB(chat_file, one_file, '<thead>\n'.encode('utf-8'))
        outputfileAB(chat_file, one_file, '<tr>\n'.encode('utf-8'))
        outputfileAB(chat_file, one_file, '<th>PK</th>\n'.encode('utf-8'))
        outputfileAB(chat_file, one_file, '<th>Chat</th>\n'.encode('utf-8'))
        outputfileAB(chat_file, one_file, '<th>Msg date</th>\n'.encode('utf-8'))
        outputfileAB(chat_file, one_file, '<th>From</th>\n'.encode('utf-8'))
        outputfileAB(chat_file, one_file, '<th>Nick</th>\n'.encode('utf-8'))
        outputfileAB(chat_file, one_file, '<th>Msg content</th>\n'.encode('utf-8'))
        outputfileAB(chat_file, one_file, '<th>Msg status</th>\n'.encode('utf-8'))
        outputfileAB(chat_file, one_file, '<th>Media Type</th>\n'.encode('utf-8'))
        outputfileAB(chat_file, one_file, '<th>Media Size</th>\n'.encode('utf-8'))
        outputfileAB(chat_file, one_file, '</tr>\n'.encode('utf-8'))
        outputfileAB(chat_file, one_file, '</thead>\n'.encode('utf-8'))

        outputfileAB(chat_media_file, '<h3><a href="{0}.{1}.html">Back to messages</a></h3>'.format(GetBase(outfile),chatid).encode('utf-8'))
        outputfileAB(chat_media_file, '<h3><a href="{0}">Return to index</a></h3>'.format( GetBase(main_file_name)).encode( 'utf-8' ) )
        outputfileAB(chat_media_file, '<h3><a href="{0}">Return to overview</a></h3>'.format(GetBase(one_file_name)).encode('utf-8'))

        outputfileAB(chat_media_file, '<h3>Media files #{0}: <a name="{1}">{2}</a></h3>\n'.format(i.pk_cs, i.contact_name, contactname).encode('utf-8'))
        outputfileAB(chat_media_file, '<table id="msg_{0}" border="1" cellpadding="2" cellspacing="0" width=500>\n'.format(chatid).encode('utf-8'))
        outputfileAB(chat_media_file, '<tr>\n'.encode('utf-8'))

        # writes table content
        outputfileAB(chat_file, one_file, '<tbody>\n'.encode('utf-8'))

        media_files = 0

        for y in i.msg_list:

            #TimeFilter enable
            if have_tf:
                tsmgs = totimestamp(y.msg_date)
                if not ((tsmgs >= tsFrom) and (tsmgs <= tsTo)):
                    continue

            # Determine type of content
            content_type = None
            if mode == ANDROID:
                if y.from_me == 1:
                    if y.status == 6:
                        content_type = CONTENT_NEWGROUPNAME

                if  y.status == 6 and str(y.media_wa_type) == "8":
                    content_type = CONTENT_NEWGROUPNAME
                        #       media_type
                        # status        media_siz       y.media_duration
                        # 6         8           Calls

                try:
                    if "[Broadcast send" in y.msg_text :
                        content_type = CONTENT_NEWGROUPNAME
                        # Broadcast
                except:
                    pass

                if content_type is None:
                    if str(y.media_wa_type) == "4":
                        content_type = CONTENT_VCARD
                        y.vcard_string = y.msg_text
                        y.vcard_name = y.local_url
                    elif str(y.media_wa_type) == "1" or str(y.media_wa_type) == "3" or str(y.media_wa_type) == "5":
                        if str(y.msg_text)[:3] == "/9j":
                            y.media_thumb = "data:image/jpg;base64,\n" + y.msg_text
                        else:
                            try:
                                y.media_thumb = "data:image/jpg;base64,\n" + base64.b64encode(y.media_thumb).decode("utf-8")
                            except:
                                y.media_thumb = ""
                        if str(y.media_wa_type) == "5":
                            content_type = CONTENT_GPS
                            if y.local_url:
                                gpsname = y.local_url
                            else:
                                gpsname = None
                        else:
                            if str(y.media_wa_type) == "3":
                                content_type = CONTENT_VIDEO
                            else:
                                content_type = CONTENT_IMAGE
                    else:
                        if str(y.media_wa_type) == "2":
                            content_type = CONTENT_AUDIO
                        else:
                            content_type = CONTENT_TEXT
            # IPHONE mode
            elif mode == IPHONE:
                # Yello Background
                if str(y.media_wa_type) == "6" or str(y.media_wa_type) == "10":
                    content_type = CONTENT_NEWGROUPNAME

                # prepare thumb
                # y.media_wa_type = "1"; "2"; "5"
                if y.media_thumb:
                    y.media_thumb = "data:image/jpg;base64,\n" + base64.b64encode(y.media_thumb).decode("utf-8")
                elif y.media_thumb_local_url:
                    y.media_thumb = y.media_thumb_local_url
                # Start if Clause
                # GPS
                if y.media_wa_type == "5":
                    content_type = CONTENT_GPS
                    #y.media_wa_type = "5"
                    gpsname = None
                # VCARD
                elif y.media_wa_type == "4":
                #elif y.vcard_string:
                    content_type = CONTENT_VCARD
                    #y.media_wa_type = "4"

                # MEDIA
                elif y.media_url:
                    if y.media_thumb:
                        content_type = CONTENT_MEDIA_THUMB
                        if str(y.media_wa_type) == "2":
                            content_type = CONTENT_VIDEO
                        else:
                            content_type = CONTENT_IMAGE
                            #y.media_wa_type = "1"
                    else:
                        if str(y.media_wa_type) == "3":
                            content_type = CONTENT_AUDIO
                        else:
                            content_type = CONTENT_MEDIA_NOTHUMB
                # TEXT
                elif str(y.media_wa_type) == "0":
                    content_type = CONTENT_TEXT

                # End if Clause

            # row class selection
            if content_type == CONTENT_NEWGROUPNAME:
               outputfileAB(chat_file, one_file, '<tr class="newgroupname">\n'.encode('utf-8'))
            elif y.from_me == 1:
                outputfileAB(chat_file, one_file, '<tr class="me">\n'.encode('utf-8'))
            else:
                outputfileAB(chat_file, one_file, '<tr class="other">\n'.encode('utf-8'))

            # get corresponding contact name for the contact_from of this message:
            if y.contact_from != "me":
                if y.contact_from == i.contact_id: #if sender is identical to chat name
                    y.contact_from = contactname
                else: # for group chats
                    for n in chat_session_list:
                        if n.contact_id == y.contact_from:
                            y.contact_from = convertsmileys ( n.contact_name )

            # y.contact_from - split only when jid
            if len(y.contact_from) > len("@s.whatsapp.net"):
                if y.contact_from[-len("@s.whatsapp.net"):] == "@s.whatsapp.net":
                    y.contact_from = y.contact_from.split("@")[0]

            # PK
            outputfileAB(chat_file, one_file, '<td>{0}</td>\n'.format(y.pk_msg).encode('utf-8'))

            # Chat name
            outputfileAB(chat_file, one_file, '<td class="contact">{0}</td>\n'.format(contactname).encode('utf-8'))
            # Msg date
            outputfileAB(chat_file, one_file, '<td>{0}</td>\n'.format(str(y.msg_date).replace(" ","&nbsp;")).encode('utf-8'))
            # From
            outputfileAB(chat_file, one_file, '<td class="contact">{0}</td>\n'.format(y.contact_from).encode('utf-8'))
            # Whatsapp Name
            nickname = convertsmileys ( y.wa_name ) # chat nick-name
            outputfileAB(chat_file, one_file, '<td class="contact">{0}</td>\n'.format(nickname).encode('utf-8'))

            # date elaboration for further use
            date = str(y.msg_date)[:10]
            if date != 'N/A' and date != 'N/A error':
                date = int(date.replace("-",""))

            # Media_msg_text
            if y.msg_text != None:
                T_MediaMsg = "</br><b>Msg:&nbsp;</b>{}".format(y.msg_text)
                #T_MediaMsg.replace(chr(13)+chr(10),"</br>")
                # replace dosn´t work with CR+LF direktly
            else:
                T_MediaMsg = ""
            # media_caption
            if len(y.media_caption) >0:
                T_MediaCaption = "</br><b>Caption:&nbsp;</b>{}".format(y.media_caption)
                M_MediaCaption = "</br><b>Caption:</b></br>{}".format(y.media_caption)
            else:
                T_MediaCaption = ""
                M_MediaCaption = ""

            # Display Msg content (Text/Media)

            if content_type == CONTENT_IMAGE:
                #Search for offline file with current date (+2 days) and known media size
                linkimage = findfile ("IMG", y.media_size, y.local_url, date, 2, 2)
                linkimage = linkimage[len(GetPath(outfile))+1:]
                media_file_Typ = MediaFileType (linkimage)
                if media_file_Typ == "iPHONE":
                    media_file_Typ = "Image"
                media_file_Path = MediaFilePath (linkimage)
                try:
                    #outputfileAB(chat_file, one_file, '<td class="text"><a onclick="image(this.href);return(false);" target="image" href="{0}"><img src="{1}" alt="Image"/></a>&nbsp;|&nbsp;<a onclick="image(this.href);return(false);" target="image" href="{2}">Image</a>'.format(y.media_url, y.media_thumb, linkimage).encode('utf-8'))
                    outputfileAB(chat_file, one_file, '<td class="text"><img src="{2}" alt="Image"/></a>&nbsp;|&nbsp;{0}</br><a target="_blank" href="{3}">{1}</a>{4}'.format(media_file_Typ, media_file_Path, y.media_thumb, linkimage, T_MediaCaption).encode('utf-8'))

                    try:
                        if media_files % 4 == 0:
                            outputfileAB(chat_media_file, '<tr>\n'.encode('utf-8'))

                        media_files = media_files + 1
                        #outputfileAB(chat_media_file, '<td><a onclick="image(this.href);return(false);" target="image" href="{0}"><img src="{1}" alt="Image"/></a></td>\n'.format(linkimage, y.media_thumb).encode('utf-8'))
                        outputfileAB(chat_media_file, '<td><b>PK:&nbsp;{0}</b></br>{1}</br><img src="{4}" alt="Video"/></br><a target="_blank" href="{3}">{2}</a>{5}</td>'.format(y.pk_msg, media_file_Typ, media_file_Path, linkimage, y.media_thumb, M_MediaCaption).encode('utf-8'))

                        if media_files % 4 == 0:
                            outputfileAB(chat_media_file, '</tr>\n'.encode('utf-8'))
                    except:
                        pass

                except:
                    outputfileAB(chat_file, one_file, '<td class="text">Bild N/A'.encode('utf-8'))
            elif content_type == CONTENT_AUDIO:
                #Search for offline file with current date (+2 days) and known media size
                linkaudio = findfile ("PTT", y.media_size, y.local_url, date, 2, 2)
                if linkaudio[-1] == "/":
                    linkaudio = findfile ("AUD", y.media_size, y.local_url, date, 2, 2)
                if y.media_duration == "":
                    T_mduration = ""
                    M_mduration = ""
                else:
                    T_mduration = "&nbsp;-&nbsp;({0} Sek.)".format(y.media_duration).encode('utf-8')
                    M_mduration = "({0}&nbsp;Sek.)".format(y.media_duration).encode('utf-8')
                media_file_Typ = MediaFileType (linkaudio)
                if media_file_Typ == "iPHONE":
                    media_file_Typ = "Audio"
                media_file_Path = MediaFilePath (linkaudio)
                try:
                    #outputfileAB(chat_file, one_file, '<td class="text"><a onclick="media(this.href);return(false);" target="media" href="{0}">Audio (online)</a>&nbsp;|&nbsp;<a onclick="media(this.href);return(false);" target="media" href="{1}">Audio (offline)</a>{2}'.format(y.media_url, linkaudio, T_mduration).encode('utf-8'))
                    outputfileAB(chat_file, one_file, '<td class="text">{0}&nbsp{3}</br><a target="_blank" href="{2}">{1}</a>{4}'.format(media_file_Typ, media_file_Path, linkaudio, T_mduration, T_MediaCaption,T_MediaMsg).encode('utf-8'))

                    try:
                        if media_files % 4 == 0:
                            outputfileAB(chat_media_file, '<tr>\n'.encode('utf-8'))

                        media_files = media_files + 1
                        #outputfileAB(chat_media_file, '<td><a onclick="media(this.href);return(false);" target="media" href="{0}">Audio (online)</a>&nbsp;|&nbsp;<a onclick="media(this.href);return(false);" target="media" href="{1}">Audio (offline)</a>&nbsp;-&nbsp;({3}&nbsp;Sek.)</td>'.format(y.media_url, linkaudio, y.media_duration).encode('utf-8'))
                        #outputfileAB(chat_media_file, '<td><a onclick="media(this.href);return(false);" target="media" href="{0}">Audio (online)</a>&nbsp;<a onclick="media(this.href);return(false);" target="media" href="{1}">Audio (offline)</a>&nbsp;{2}</td>'.format(y.media_url, linkaudio, M_mduration).encode('utf-8'))
                        outputfileAB(chat_media_file, '<td><b>PK:&nbsp;{0}</b></br>{1}&nbsp;{4}</br><a target="_blank" href="{3}">{2}</a>{5}</td>'.format(y.pk_msg, media_file_Typ, media_file_Path, linkaudio, M_mduration, M_MediaCaption).encode('utf-8'))

                        if media_files % 4 == 0:
                            outputfileAB(chat_media_file, '</tr>\n'.encode('utf-8'))
                    except:
                        pass

                except:
                    outputfileAB(chat_file, one_file, '<td class="text">Audio N/A'.encode('utf-8'))
            elif content_type == CONTENT_VIDEO:
                #Search for offline file with current date (+2 days) and known media size
                linkvideo = findfile ("VID", y.media_size, y.local_url, date, 2, 2)
                if y.media_duration == "":
                    T_mduration = ""
                    M_mduration = ""
                else:
                    T_mduration = " -  ({0} Sek.)".format(y.media_duration).encode('utf-8')
                    M_mduration = "({0}&nbsp;Sek.)".format(y.media_duration).encode('utf-8')
                media_file_Typ = MediaFileType (linkvideo)
                if media_file_Typ == "iPHONE":
                    media_file_Typ = "Video"
                media_file_Path = MediaFilePath (linkvideo)
                try:
                    #outputfileAB(chat_file, one_file, '<td class="text"><a onclick="media(this.href);return(false);" target="media" href="{0}"><img src="{1}" alt="Video"/></a>&nbsp;|&nbsp;<a onclick="media(this.href);return(false);" target="media" href="{2}">Video</a>{3}'.format(y.media_url, y.media_thumb, linkvideo, T_mduration).encode('utf-8'))
                    outputfileAB(chat_file, one_file, '<td class="text"><img src="{2}" alt="Video"/></a>&nbsp;|&nbsp;{0}&nbsp{4}</br><a target="_blank" href="{3}">{1}</a>{5}'.format(media_file_Typ, media_file_Path, y.media_thumb, linkvideo, T_mduration, T_MediaCaption, T_MediaMsg).encode('utf-8'))

                    try:
                        if media_files % 4 == 0:
                            outputfileAB(chat_media_file, '<tr>\n'.encode('utf-8'))

                        media_files = media_files + 1
                        #outputfileAB(chat_media_file, '<td><a onclick="media(this.href);return(false);" target="media" href="{0}"><img src="{1}" alt="Video"/></a>&nbsp;|&nbsp;<a onclick="media(this.href);return(false);" target="media" href="{2}">Video</a>&nbsp;-&nbsp;({3}&nbsp;Sek.)</td>'.format(y.media_url, y.media_thumb, linkvideo, y.media_duration).encode('utf-8'))
                        #outputfileAB(chat_media_file, '<td><a onclick="media(this.href);return(false);" target="media" href="{0}"><img src="{1}" alt="Video"/></a>&nbsp;<a onclick="media(this.href);return(false);" target="media" href="{2}">Video</a>&nbsp;{3}</td>'.format(y.media_url, y.media_thumb, linkvideo, M_mduration).encode('utf-8'))
                        outputfileAB(chat_media_file, '<td><b>PK:&nbsp;{0}</b></br>{1}&nbsp;{4}</br><img src="{5}" alt="Video"/></br><a target="_blank" href="{3}">{2}</a>{6}</td>'.format(y.pk_msg, media_file_Typ, media_file_Path, linkvideo, M_mduration, y.media_thumb, M_MediaCaption).encode('utf-8'))

                        if media_files % 4 == 0:
                            outputfileAB(chat_media_file, '</tr>\n'.encode('utf-8'))
                    except:
                        pass

                except:
                    outputfileAB(chat_file, one_file, '<td class="text">Video N/A'.encode('utf-8'))
            elif content_type == CONTENT_MEDIA_THUMB:
                #Search for offline file with current date (+2 days) and known media size
                linkmedia = findfile ("MEDIA_THUMB", y.media_size, y.local_url, date, 2, 2)
                try:
                    outputfileAB(chat_file, one_file, '<td class="text"><a onclick="image(this.href);return(false);" target="image" href="{0}"><img src="{1}" alt="Media"/></a>&nbsp;|&nbsp;<a onclick="image(this.href);return(false);" target="image" href="{2}">Media</a>'.format(y.media_url, y.media_thumb, linkmedia).encode('utf-8'))
                except:
                    outputfileAB(chat_file, one_file, '<td class="text">Media N/A'.encode('utf-8'))
            elif content_type == CONTENT_MEDIA_NOTHUMB:
                #Search for offline file with current date (+2 days) and known media size
                linkmedia = findfile ("MEDIA_NOTHUMB", y.media_size, y.local_url, date, 2, 2)
                try:
                    outputfileAB(chat_file, one_file, '<td class="text"><a onclick="media(this.href);return(false);" target="media" href="{0}">Media (online)</a>&nbsp;|&nbsp;<a onclick="media(this.href);return(false);" target="media" href="{1}">Media (offline)</a>'.format(y.media_url, linkmedia).encode('utf-8'))
                except:
                    outputfileAB(chat_file, one_file, '<td class="text">Media N/A'.encode('utf-8'))
            elif content_type == CONTENT_VCARD:
                if y.vcard_name == "" or y.vcard_name is None:
                    vcardintro = ""
                else:
                    vcardintro = "CONTACT: <b>" + y.vcard_name + "</b><br>\n"
                y.vcard_string = y.vcard_string.replace ("\n", "<br>\n")
                try:
                    outputfileAB(chat_file, one_file, '<td class="text">{0}'.format(vcardintro + y.vcard_string).encode('utf-8'))
                except:
                    outputfileAB(chat_file, one_file, '<td class="text">VCARD N/A'.encode('utf-8'))
            elif content_type == CONTENT_GPS:
                # Google 1: https://maps.google.com/?q={},{}"><img src="{}" alt="GPS"/></a>

                # add
                # Open-Street-Map: "http://www.openstreetmap.org/?mlat=" & Lat & "&amp;mlon=" & Lon & "#map=14/" & Lat & "/" & Lon; "Karte"
                sLocation = '&nbsp;|&nbsp;<a target="_blank" href="http://www.openstreetmap.org/?mlat={0}&amp;mlon={1}#map=14/{0}/{1}">Karte-OSM</a></br><b>LAT:</b>&nbsp;{0}</br><b>LON:</b>&nbsp;{1}'.format(y.latitude, y.longitude,)

                try:
                    if gpsname == "" or gpsname == None:
                        gpsname = ""
                    else:
                        #gpsname = "\n" + gpsname
                        gpsname = "&nbsp;|&nbsp;<b>" + gpsname + "</b>"
                    #gpsname = gpsname.replace ("\n", "<br>\n")

                    if y.media_thumb:
                        #outputfileAB(chat_file, one_file, '<td class="text"><a onclick="image(this.href);return(false);" target="image" href="https://maps.google.com/?q={0},{1}"><img src="{2}" alt="GPS"/></a>{3}'.format(y.latitude, y.longitude, y.media_thumb, gpsname).encode('utf-8'))
                        outputfileAB(chat_file, one_file, '<td class="text"><a target="_blank" href="https://maps.google.com/?q={},{}"><img src="{}" alt="GPS"/></a>{}{}'.format(y.latitude, y.longitude, y.media_thumb, gpsname, sLocation).encode('utf-8'))
                    else:
                        #outputfileAB(chat_file, one_file, '<td class="text"><a onclick="image(this.href);return(false);" target="image" href="https://maps.google.com/?q={0},{1}">GPS: {0}, {1}</a>{2}'.format(y.latitude, y.longitude, y.latitude, y.longitude, gpsname).encode('utf-8'))
                        outputfileAB(chat_file, one_file, '<td class="text"><a target="_blank" href="https://maps.google.com/?q={},{}">Karte-Google:&nbsp;</a>{}{}'.format(y.latitude, y.longitude, gpsname, sLocation).encode('utf-8'))
                except:
                    outputfileAB(chat_file, one_file, '<td class="text">GPS N/A'.encode('utf-8'))
            elif content_type == CONTENT_NEWGROUPNAME:
                content_type = CONTENT_OTHER
            elif content_type != CONTENT_TEXT:
                content_type = CONTENT_OTHER
            # End of If-Clause, now text or other type of content:
            if content_type == CONTENT_TEXT or content_type == CONTENT_OTHER:
                msgtext = convertsmileys ( y.msg_text )
                msgtext = re.sub(r'(http[^\s\n\r]+)', r'<a onclick="image(this.href);return(false);" target="image" href="\1">\1</a>', msgtext)
                msgtext = re.sub(r'((?<!\S)www\.[^\s\n\r]+)', r'<a onclick="image(this.href);return(false);" target="image" href="http://\1">\1</a>', msgtext)
                msgtext = msgtext.replace ("\n", "<br>\n")
                try:
                    outputfileAB(chat_file, one_file, '<td class="text">{0}'.format(msgtext).encode('utf-8'))
                except:
                    outputfileAB(chat_file, one_file, '<td class="text">N/A'.encode('utf-8'))
            # outputfileAB(chat_file, one_file, str(content_type)) #Debug
            outputfileAB(chat_file, one_file, '</td>\n'.encode('utf-8'))

            # Msg status
            outputfileAB(chat_file, one_file, '<td>{0}</td>\n'.format(y.status).encode('utf-8'))

            # Media type
            outputfileAB(chat_file, one_file, '<td>{0}</td>\n'.format(y.media_wa_type).encode('utf-8'))

            # Media size
            # in equvalent to Android of Group Information
            mediasize = y.media_size

            if mode == IPHONE:
                if str(y.media_wa_type) == "6" or str(y.media_wa_type) == "10":
                    mediasize = y.group_event_type

            outputfileAB(chat_file, one_file, '<td>{0}</td>\n'.format(mediasize).encode('utf-8'))

            # Row End
            outputfileAB(chat_file, one_file, '</tr>\n'.encode('utf-8'))

        outputfileAB(chat_file, one_file, '</tbody>\n'.encode('utf-8'))
        # writes 1st table footer
        outputfileAB(chat_file, one_file, '</table>\n'.encode('utf-8'))

        outputfileAB(chat_media_file, '</table>\n'.encode('utf-8'))

        # Back-Link
        outputfileAB(chat_file, '<h3><a href="{0}">Return to index</a></h3>'.format( GetBase(main_file_name) ).encode( 'utf-8' ) )

        outputfileAB(chat_media_file, '<h3><a href="{0}.{1}.html">Back to messages</a></h3>'.format(GetBase(outfile),i.contact_id.split('@')[0],contactname).encode('utf-8'))
        outputfileAB(chat_media_file, '<h3><a href="{0}">Return to index</a></h3>'.format( GetBase(main_file_name) ).encode( 'utf-8' ) )


        # Close chat file
        outputfile_close(chat_file);

        # Close media file
        outputfile_close(chat_media_file);

        if have_groups and i.contact_id.find("@g.us") != -1:
            # Back-Link
            outputfileAB(chat_file_group, '<h3><a href="{0}">Return to GROUP index</a></h3>'.format( GetBase(main_file_name_group) ).encode( 'utf-8' ) )

            # Close chat file
            outputfile_close(chat_file_group);


    # Close one file
    outputfile_close(one_file);

    if have_groups:
        # Close one file
        outputfile_close(one_file_group);

    #End Out

    print("done!")


    #END
    #webbrowser.open(main_file_name)


##### GLOBAL variables #####

PYTHON_VERSION = None
if (sys.version_info >= (3,0)):
    PYTHON_VERSION = 3
    print("Python Version 3.x\n")
else:
    PYTHON_VERSION = 2
    print("Python Version 2.x\n")
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
    import convert_smileys_python_2


mode    = None
IPHONE  = 1
ANDROID = 2

DoOut = ""
have_tf = False
strtsFrom = ""
strtsTo = ""
APPLICATION = "WA"

have_groups = False
db_owner = ""
db_owner_name = ""

FilePathDB = "databases\\"
FilePathF = "files\\"
FilePathSP = "shared_prefs\\"
FilePathCrypt = "WhatsApp\\Databases\\"


content_type          = None
CONTENT_TEXT          = 0
CONTENT_IMAGE         = 1
CONTENT_AUDIO         = 2
CONTENT_VIDEO         = 3
CONTENT_VCARD         = 4
CONTENT_GPS           = 5
CONTENT_NEWGROUPNAME  = 6
CONTENT_MEDIA_THUMB   = 7
CONTENT_MEDIA_NOTHUMB = 8
CONTENT_OTHER         = 99

flistvid = {}
flistaud = {}
flistimg = {}
flistptt = {}

css_style = """
<style type="text/css">
body {
    font-family: calibri;
    background-color: #f5f5f5;
}
h1 {
    font-family: courier;
    font-style:italic;
    color: #444444;
}
h2 {
    font-style:italic;
    color: #444444;
}
h3 {
    font-style:italic;
}
table {
    text-align: center;
}
th {
    font-style:italic;
}
td.text {
    width: 600px;
    text-align: left;
}
td.contact {
    width: 250px;
}
tr.even {
    background-color: #DDDDDD
}
tr.me {
    background-color: #88FF88;
}
tr.other {
    background-color: #F5F5F5;
}
tr.newgroupname {
    background-color: #FFCC33;
}
</style>
"""

popups = """
function media( url )
{
  if (typeof(newwindow) !== "undefined" && !newwindow.closed)
  {
    newwindow.close();
  } else
  {
  }
  newwindow=window.open("about:blank", "media", "menubar=0,location=1");
  // PlugIn spielt Video/audio evtl. nicht richtig ab!!
  //newwindow.document.write('<html><body><embed src="' + url + '" width="800" height="600" /></body></html>');
  // HTML5 Tag "VIDEO" - FireFox, Chrom, IE9 --> Ok
  newwindow.document.write('<video src="' + url + '" controls="controls">video doesn not work</video>');
}

function image( url )
{
  if (typeof(imagewindow) !== "undefined" && !imagewindow.closed)
  {
    imagewindow=window.open(url,'image','menubar=0,location=1');
    imagewindow.focus();
  } else
  {
    imagewindow=window.open(url,'image','menubar=0,location=1');
  }
}
"""

sortable = """
/*
Table sorting script  by Joost de Valk, check it out at http://www.joostdevalk.nl/code/sortable-table/.
Based on a script from http://www.kryogenix.org/code/browser/sorttable/.
Distributed under the MIT license: http://www.kryogenix.org/code/browser/licence.html .

Copyright (c) 1997-2007 Stuart Langridge, Joost de Valk.

Version 1.5.7
*/

/* You can change these values */
var image_path = "data/sort-table/";
var image_up = "arrow-up.gif";
var image_down = "arrow-down.gif";
var image_none = "arrow-none.gif";
var europeandate = true;
var alternate_row_colors = true;

/* Don't change anything below this unless you know what you're doing */
addEvent(window, "load", sortables_init);

var SORT_COLUMN_INDEX;
var thead = false;

function sortables_init() {
    // Find all tables with class sortable and make them sortable
    if (!document.getElementsByTagName) return;
    tbls = document.getElementsByTagName("table");
    for (ti=0;ti<tbls.length;ti++) {
        thisTbl = tbls[ti];
        if (((' '+thisTbl.className+' ').indexOf("sortable") != -1) && (thisTbl.id)) {
            ts_makeSortable(thisTbl);
        }
    }
}

function ts_makeSortable(t) {
    if (t.rows && t.rows.length > 0) {
        if (t.tHead && t.tHead.rows.length > 0) {
            var firstRow = t.tHead.rows[t.tHead.rows.length-1];
            thead = true;
        } else {
            var firstRow = t.rows[0];
        }
    }
    if (!firstRow) return;

    // We have a first row: assume it's the header, and make its contents clickable links
    for (var i=0;i<firstRow.cells.length;i++) {
        var cell = firstRow.cells[i];
        var txt = ts_getInnerText(cell);
        if (cell.className != "unsortable" && cell.className.indexOf("unsortable") == -1) {
            cell.innerHTML = '<a href="#" class="sortheader" onclick="ts_resortTable(this, '+i+');return false;">'+txt+'<span class="sortarrow">&nbsp;&nbsp;<img src="'+ image_path + image_none + '" alt="&darr;"/></span></a>';
        }
    }
    if (alternate_row_colors) {
        alternate(t);
    }
}

function ts_getInnerText(el) {
    if (typeof el == "string") return el;
    if (typeof el == "undefined") { return el };
    if (el.innerText) return el.innerText;    //Not needed but it is faster
    var str = "";

    var cs = el.childNodes;
    var l = cs.length;
    for (var i = 0; i < l; i++) {
        switch (cs[i].nodeType) {
            case 1: //ELEMENT_NODE
                str += ts_getInnerText(cs[i]);
                break;
            case 3:    //TEXT_NODE
                str += cs[i].nodeValue;
                break;
        }
    }
    return str;
}

function ts_resortTable(lnk, clid) {
    var span;
    for (var ci=0;ci<lnk.childNodes.length;ci++) {
        if (lnk.childNodes[ci].tagName && lnk.childNodes[ci].tagName.toLowerCase() == 'span') span = lnk.childNodes[ci];
    }
    var spantext = ts_getInnerText(span);
    var td = lnk.parentNode;
    var column = clid || td.cellIndex;
    var t = getParent(td,'TABLE');
    // Work out a type for the column
    if (t.rows.length <= 1) return;
    var itm = "";
    var i = 0;
    while (itm == "" && i < t.tBodies[0].rows.length) {
        var itm = ts_getInnerText(t.tBodies[0].rows[i].cells[column]);
        itm = trim(itm);
        if (itm.substr(0,4) == "<!--" || itm.length == 0) {
            itm = "";
        }
        i++;
    }
    if (itm == "") return;
    sortfn = ts_sort_caseinsensitive;
    if (itm.match(/^\d\d[\/\.-][a-zA-z][a-zA-Z][a-zA-Z][\/\.-]\d\d\d\d$/)) sortfn = ts_sort_date;
    if (itm.match(/^\d\d[\/\.-]\d\d[\/\.-]\d\d\d{2}?$/)) sortfn = ts_sort_date;
    if (itm.match(/^-?[Â£$â‚¬Ã›Â¢Â´]\d/)) sortfn = ts_sort_numeric;
    if (itm.match(/^-?(\d+[,\.]?)+(E[-+][\d]+)?%?$/)) sortfn = ts_sort_numeric;
    SORT_COLUMN_INDEX = column;
    var firstRow = new Array();
    var newRows = new Array();
    for (k=0;k<t.tBodies.length;k++) {
        for (i=0;i<t.tBodies[k].rows[0].length;i++) {
            firstRow[i] = t.tBodies[k].rows[0][i];
        }
    }
    for (k=0;k<t.tBodies.length;k++) {
        if (!thead) {
            // Skip the first row
            for (j=1;j<t.tBodies[k].rows.length;j++) {
                newRows[j-1] = t.tBodies[k].rows[j];
            }
        } else {
            // Do NOT skip the first row
            for (j=0;j<t.tBodies[k].rows.length;j++) {
                newRows[j] = t.tBodies[k].rows[j];
            }
        }
    }
    newRows.sort(sortfn);
    if (span.getAttribute("sortdir") == 'down') {
            ARROW = '&nbsp;&nbsp;<img src="'+ image_path + image_down + '" alt="&darr;"/>';
            newRows.reverse();
            span.setAttribute('sortdir','up');
    } else {
            ARROW = '&nbsp;&nbsp;<img src="'+ image_path + image_up + '" alt="&uarr;"/>';
            span.setAttribute('sortdir','down');
    }
    // We appendChild rows that already exist to the tbody, so it moves them rather than creating new ones
    // don't do sortbottom rows
    for (i=0; i<newRows.length; i++) {
        if (!newRows[i].className || (newRows[i].className && (newRows[i].className.indexOf('sortbottom') == -1))) {
            t.tBodies[0].appendChild(newRows[i]);
        }
    }
    // do sortbottom rows only
    for (i=0; i<newRows.length; i++) {
        if (newRows[i].className && (newRows[i].className.indexOf('sortbottom') != -1))
            t.tBodies[0].appendChild(newRows[i]);
    }
    // Delete any other arrows there may be showing
    var allspans = document.getElementsByTagName("span");
    for (var ci=0;ci<allspans.length;ci++) {
        if (allspans[ci].className == 'sortarrow') {
            if (getParent(allspans[ci],"table") == getParent(lnk,"table")) { // in the same table as us?
                allspans[ci].innerHTML = '&nbsp;&nbsp;<img src="'+ image_path + image_none + '" alt="&darr;"/>';
            }
        }
    }
    span.innerHTML = ARROW;
    alternate(t);
}

function getParent(el, pTagName) {
    if (el == null) {
        return null;
    } else if (el.nodeType == 1 && el.tagName.toLowerCase() == pTagName.toLowerCase()) {
        return el;
    } else {
        return getParent(el.parentNode, pTagName);
    }
}

function sort_date(date) {
    // y2k notes: two digit years less than 50 are treated as 20XX, greater than 50 are treated as 19XX
    dt = "00000000";
    if (date.length == 11) {
        mtstr = date.substr(3,3);
        mtstr = mtstr.toLowerCase();
        switch(mtstr) {
            case "jan": var mt = "01"; break;
            case "feb": var mt = "02"; break;
            case "mar": var mt = "03"; break;
            case "apr": var mt = "04"; break;
            case "may": var mt = "05"; break;
            case "jun": var mt = "06"; break;
            case "jul": var mt = "07"; break;
            case "aug": var mt = "08"; break;
            case "sep": var mt = "09"; break;
            case "oct": var mt = "10"; break;
            case "nov": var mt = "11"; break;
            case "dec": var mt = "12"; break;
            // default: var mt = "00";
        }
        dt = date.substr(7,4)+mt+date.substr(0,2);
        return dt;
    } else if (date.length == 10) {
        if (europeandate == false) {
            dt = date.substr(6,4)+date.substr(0,2)+date.substr(3,2);
            return dt;
        } else {
            dt = date.substr(6,4)+date.substr(3,2)+date.substr(0,2);
            return dt;
        }
    } else if (date.length == 8) {
        yr = date.substr(6,2);
        if (parseInt(yr) < 50) {
            yr = '20'+yr;
        } else {
            yr = '19'+yr;
        }
        if (europeandate == true) {
            dt = yr+date.substr(3,2)+date.substr(0,2);
            return dt;
        } else {
            dt = yr+date.substr(0,2)+date.substr(3,2);
            return dt;
        }
    }
    return dt;
}

function ts_sort_date(a,b) {
    dt1 = sort_date(ts_getInnerText(a.cells[SORT_COLUMN_INDEX]));
    dt2 = sort_date(ts_getInnerText(b.cells[SORT_COLUMN_INDEX]));

    if (dt1==dt2) {
        return 0;
    }
    if (dt1<dt2) {
        return -1;
    }
    return 1;
}
function ts_sort_numeric(a,b) {
    var aa = ts_getInnerText(a.cells[SORT_COLUMN_INDEX]);
    aa = clean_num(aa);
    var bb = ts_getInnerText(b.cells[SORT_COLUMN_INDEX]);
    bb = clean_num(bb);
    return compare_numeric(aa,bb);
}
function compare_numeric(a,b) {
    var a = parseFloat(a);
    a = (isNaN(a) ? 0 : a);
    var b = parseFloat(b);
    b = (isNaN(b) ? 0 : b);
    return a - b;
}
function ts_sort_caseinsensitive(a,b) {
    aa = ts_getInnerText(a.cells[SORT_COLUMN_INDEX]).toLowerCase();
    bb = ts_getInnerText(b.cells[SORT_COLUMN_INDEX]).toLowerCase();
    if (aa==bb) {
        return 0;
    }
    if (aa<bb) {
        return -1;
    }
    return 1;
}
function ts_sort_default(a,b) {
    aa = ts_getInnerText(a.cells[SORT_COLUMN_INDEX]);
    bb = ts_getInnerText(b.cells[SORT_COLUMN_INDEX]);
    if (aa==bb) {
        return 0;
    }
    if (aa<bb) {
        return -1;
    }
    return 1;
}
function addEvent(elm, evType, fn, useCapture)
// addEvent and removeEvent
// cross-browser event handling for IE5+,    NS6 and Mozilla
// By Scott Andrew
{
    if (elm.addEventListener){
        elm.addEventListener(evType, fn, useCapture);
        return true;
    } else if (elm.attachEvent){
        var r = elm.attachEvent("on"+evType, fn);
        return r;
    } else {
        alert("Handler could not be removed");
    }
}
function clean_num(str) {
    str = str.replace(new RegExp(/[^-?0-9.]/g),"");
    return str;
}
function trim(s) {
    return s.replace(/^\s+|\s+$/g, "");
}
function alternate(table) {
    // Take object table and get all it's tbodies.
    var tableBodies = table.getElementsByTagName("tbody");
    // Loop through these tbodies
    for (var i = 0; i < tableBodies.length; i++) {
        // Take the tbody, and get all it's rows
        var tableRows = tableBodies[i].getElementsByTagName("tr");
        // Loop through these rows
        // Start at 1 because we want to leave the heading row untouched
        for (var j = 0; j < tableRows.length; j++) {
            // Check if j is even, and apply classes for both possible results
            if ( (j % 2) == 0  ) {
                if ( !(tableRows[j].className.indexOf('odd') == -1) ) {
                    tableRows[j].className = tableRows[j].className.replace('odd', 'even');
                } else {
                    if ( tableRows[j].className.indexOf('even') == -1 ) {
                        tableRows[j].className += " even";
                    }
                }
            } else {
                if ( !(tableRows[j].className.indexOf('even') == -1) ) {
                    tableRows[j].className = tableRows[j].className.replace('even', 'odd');
                } else {
                    if ( tableRows[j].className.indexOf('odd') == -1 ) {
                        tableRows[j].className += " odd";
                    }
                }
            }
        }
    }
}
"""

if __name__ == '__main__':
    main(sys.argv[1:])

