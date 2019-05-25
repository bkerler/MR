
import datetime, time, re
from datetime import timezone
from pathlib import PurePath, Path

class HTMLReport:
    TEMPLATE_DIR = "htmlreport-templates"
    TEXT_EN = {
        'unknown_value':        'N/A'
    }
    DEFAULT_TEXT = TEXT_EN

    def __init__(self, output_directory):
        # create project directory
        try:
            self.project_directory = Path(output_directory)
            self.project_directory.mkdir(parents=True, exist_ok=True)
        except:
            # this is a serious error
            raise

    def parse_template(self, template_name):
        #open and parse template
        template_file = Path(__file__).parent / HTMLReport.TEMPLATE_DIR / (template_name + ".html")
        if template_file.exists():
            template_source = template_file.read_text()
            return self.parse_template_content(template_source)

    def parse_template_content(self, template, template_var=None, next_item=None):
        if not template_var:
            template_var = []

        if not next_item:
            next_item ="content"
        
        try:
            tag_re = re.compile("<!-- (.+) -->|$")
            tag = tag_re.search(template).group(1)
            if not tag:
                template_var.append([next_item, template])
        except:
            pass
        else:
            try:
                block_start = template.index("<!-- {} -->".format(tag))
                block_end = template.index("<!-- {}-end -->".format(tag))
                snipet = template[block_start+len(tag)+9:block_end]
                rest = template[:block_start+len(tag)+9] + "{content}" + template[block_end:]
                template_var.append([next_item, rest])
                template_var = self.parse_template_content(snipet, template_var, tag)
            except:
                self.info_output("{0} entry not found in template.".format(tag), 1)
            
        return template_var

    def timestamp_converter(self, input_timestamp, timezone=None):
        #TODO: implement timezone correction
        output_timestamp = HTMLReport.DEFAULT_TEXT['unknown_value']
        try:
            timestamp = int(input_timestamp) / 1000
            output_timestamp = str(
                datetime.datetime
                .fromtimestamp(timestamp)
                .replace(microsecond=0)
                .replace(tzinfo=datetime.timezone.utc)
                .strftime('%Y-%m-%d %H:%M:%S %z')
                )
        except (TypeError, ValueError) as error:
            self.info_output('Timestamp {0} not parsable. {1}'.format(input_timestamp, error), 1)
        return output_timestamp

    def info_output(self, message, level=2, end="\n"):
        levels = ["Error", "Warning", "Info"]
        if level < 3:
            print("    " + levels[level] + (7-len(levels[level]))*" "+ ": " + str(message), end=end)
        else:
            print("**** " + str(message) + " ****", end=end)


class HTMLReportMessaging(HTMLReport):
    # default text english
    TEXT_EN = {
        'unknown_value':        'N/A',
        'chats':                'Chats for Account: {0}',
        'thumb_only':           'Only thumbnail available.',
        'no_media':             'Original media file missing.',
        'caption':              'Caption',
        'size':                 'Size',
        'duration':             'Duration',
        'seconds':              'seconds',
        'latitude':             'Latitude',
        'longitude':            'Longitude',
        'url':                  'URL',
        'name':                 'Title'
    }
    DEFAULT_TEXT = TEXT_EN

    DEFAULT_FILES = {
        'file_avatar_thumb': Path(__file__).parent / HTMLReport.TEMPLATE_DIR / "data" / "avatar_thumb.png",
        'file_avatar': Path(__file__).parent / HTMLReport.TEMPLATE_DIR / "data" / "avatar.png"
    }

    def __init__(self, output_directory, messaging):
        self.info_output("Generating HTML-Report files ...",3)
        super().__init__(output_directory)
        
        self.messaging = messaging

        #create directories & copy css
        self.output_dir_avatar = self.project_directory / "avatar"
        self.output_dir_avatar.mkdir(parents=True, exist_ok=True)
        self.output_dir_media = self.project_directory / "media"
        self.output_dir_media.mkdir(parents=True, exist_ok=True)
        self.output_dir_thumb = self.project_directory / "thumbnail"
        self.output_dir_thumb.mkdir(parents=True, exist_ok=True)
        self.output_dir_data = self.project_directory / "data"
        self.output_dir_data.mkdir(parents=True, exist_ok=True)
        file_input_css = Path(__file__).parent / HTMLReport.TEMPLATE_DIR / "data" / "style.css"
        file_output_css = self.output_dir_data / "style.css"
        file_output_css.write_text(file_input_css.read_text(), encoding='utf-8')
        file_input_css = Path(__file__).parent / HTMLReport.TEMPLATE_DIR / "data" / "bubble.css"
        file_output_css = self.output_dir_data / "bubble.css"
        file_output_css.write_text(file_input_css.read_text(), encoding='utf-8')

        self.chats = []
        self.owner = messaging.owner
        self.meta = {}
        insert_pos = 0

        messages_template = self.parse_template("messages")
        messages_bubble_template = self.parse_template("messages-bubble")
        memberlist_template = self.parse_template("memberlist")
        memberlist_all_template = self.parse_template("memberlist-all")

        # generate reports
        for platform_id in messaging:
            self.chat = messaging.get_chat(platform_id)
            self.messages = self.chat.messages
            # reload messages for bubble view
            self.chat_bubble = messaging.get_chat(platform_id)
            self.messages_bubble = self.chat_bubble.messages

            # if we have a memberlist extract some details
            if self.chat.memberlist:
                members_alltimes = self.chat.memberlist.get_allmembers()
                members_current = self.chat.memberlist.get_state()
                self.members = {
                    "list_alltimes": members_alltimes,
                    "count_alltimes": len(members_alltimes) if members_alltimes else 0,
                    "list_current": members_current,
                    "count_current": len(members_current) if members_current else 0
                }
                self.info_output('Writing memberlist ...')

                # write list of all members
                self.member = []
                if members_alltimes:
                    for member in members_alltimes:
                            self.member.append(messaging.get_contact(member))
                    output_file = self.project_directory / (str(platform_id) + "-all-memberlist.html")
                    output_file.write_text(self.process_template(memberlist_all_template), encoding='utf-8')

                # write memberlist for every change
                for e in self.chat.memberlist:
                    timestamp, memberlist = e
                    self.meta = {"timestamp": timestamp}
                    self.member = []
                    for member in memberlist:
                        self.member.append(messaging.get_contact(member))
                    output_file = self.project_directory / (str(platform_id) + "-" + str(
                        datetime.datetime
                        .fromtimestamp(timestamp/1000)
                        .replace(tzinfo=datetime.timezone.utc)
                        .strftime('%Y%m%d-%H%M%S-%f')
                        ) + "-memberlist.html")
                    output_file.write_text(self.process_template(memberlist_template), encoding='utf-8')
                    self.info_output('    {0}'.format(timestamp))
            else:
                self.members = {
                    "list_alltimes": None,
                    "count_alltimes": 2,
                    "list_current": None,
                    "count_current": 2
                }

            # generate message pages only if we have messages
            if self.chat.count_msg:
                # insert chats with messages on top
                self.chats.insert(insert_pos, self.chat)
                insert_pos = insert_pos + 1
                output_file = self.project_directory / (str(platform_id) + "-messages.html")
                output_file.write_text(self.process_template(messages_template), encoding='utf-8')
                output_file = self.project_directory / (str(platform_id) + "-messages-bubble.html")
                output_file.write_text(self.process_template(messages_bubble_template), encoding='utf-8')
            else:
                self.chats.append(self.chat)
                

            #else:
            #    self.memberlist = None

        # finally write chatlist overview
        output_file = self.project_directory / ("index.html")
        output_file.write_text(self.process_template(self.parse_template("index")), encoding='utf-8')

        self.info_output("... finished.",3)

    def process_template(self, template_blocks):
        content = "{content}"
        block = ""
        d = dict()
        d["generator"] = {"product":self.messaging.PRODUCT, "version":self.messaging.VERSION, "timestamp_report":datetime.datetime.now()}
        d["chat"] = self.parse_content_data(self.chat.__dict__)
        d["meta"] = self.parse_content_data(self.meta)
        d["contact"] = self.parse_content_data(self.chat.contact.__dict__)
        d["messages"] = self.chat.messages
        d["messages_bubble"] = self.chat_bubble.messages
        d["owner"] = self.parse_content_data(self.owner.__dict__)
        d["members"] = self.parse_content_data(self.members)
        for template_block in template_blocks:
            data = dict()
            template_block_name = template_block[0]
            template_block_content = template_block[1]
            # simply replace content
            if template_block_name == "content":
                template_block_content = template_block_content.format(
                    **d, content="{content}")
                content = content.format(content=template_block_content)
            # iterate over 
            else:
                if template_block_name:
                    data = self.__dict__[template_block_name]  
                    for d in data:
                        d = data=self.parse_content_data(d.__dict__)
                        block = block + template_block_content.format(
                            **d, content="{content}")
                    content = content.format(content=block)    
        return content
       

    def parse_content_data(self, data):
        """
        Parse and convert data from database entrys into content.

        This function will convert data depending on the name of the field.
        The following start of fieldnames are implemented:

        timestamp_  -> timestamps will be transformed into readable date/times
        file_   -> copy file to output directory

        Other fieldnames will be checked if the are empty. If this is the case
        they are set to some default value.

            :param data: dict with non processed data
            :param content: dict with data fields for template
            :return: dict with data fields for the template
        """   
        content = {}

        # loop over data and process them
        for k, e in data.items():

            # dont touch platform_id and lists
            if k == "platform_id":
                content.update({k:e})
            
            elif k == "contact_id" or k == "sender_id" or k == "receiver_id":
                try:
                    contact = self.messaging.get_contact(e)
                    contact = self.parse_content_data(contact.__dict__)
                    content.update({k:contact})
                except Exception as error:
                    self.info_output(error, 1)

            # convert timestamp fields
            elif k.startswith("timestamp"):
                # if we hava a timestamps field skip buildig it
                if not "timestamps" in data:
                    timestamps = ""
                    for kk, ee in data.items():
                        if kk.startswith("timestamp"):
                            if ee:
                                # add new line if already timestamps in var
                                timestamps = timestamps + "<br />" if timestamps else ""
                                timestamps = timestamps + '<b>' + kk[10:].capitalize() + '</b>: <span class="timestamp">' + self.timestamp_converter(ee) + '</span>'
                    content.update({"timestamps":timestamps})
                if e:
                    content.update({k:self.timestamp_converter(data.get(k, 0))})
                else:
                    content.update({k:HTMLReport.DEFAULT_TEXT['unknown_value']})

            # build message content
            elif k == "content_message":
                content["details"] = ""
                # parse all fields
                e = self.parse_content_data(e.__dict__)

                # build link to media file & show thumb if available
                if e["file_media"] and e["file_thumbnail"]:
                    e["data"] = '<a href="{}" class="clickable"><img src="{}" class="{}" /></a>'.format(e["file_media"], e["file_thumbnail"], e["media_type"])
                elif e["file_thumbnail"]:
                    e["data"] = '<img src="{}" title="{}" class="{}" />'.format(e["file_thumbnail"], HTMLReportMessaging.DEFAULT_TEXT['thumb_only'], e["media_type"])
                elif e["file_media"]:
                    if e["media_type"] == "STICKER":
                        e["data"] = '<img src="{}" class="{}" />'.format(e["file_media"], e["media_type"])
                    elif e["name"]:
                        e["data"] = '<a href="{}">{}</a>'.format(e["file_media"], e["name"])
                    else:
                        e["data"] = '<a href="{}">{}</a>'.format(e["file_media"], e["media_type"])
                else:
                    pass

                # add additional fields and details
                if e["caption"]:
                    if e["data"] == None:
                        e["data"] = ""
                    e["data"] = e["data"] + '<br />{0}'.format(e["caption"])
                if e["latitude"] and e["longitude"]:
                    e["data"] = e["data"] + '<br /><a href="https://www.openstreetmap.org/?mlat={0}&mlon={1}&zoom=17">Show on OpenStreetMap</a>'.format(e["latitude"], e["longitude"])
                    content["details"] = content.get("details", "") + '<br /><b>{0}:</b> {1}'.format(HTMLReportMessaging.DEFAULT_TEXT['latitude'], e["latitude"])
                    content["details"] = content.get("details", "") + '<br /><b>{0}:</b> {1}'.format(HTMLReportMessaging.DEFAULT_TEXT['longitude'], e["longitude"])
                if e["url"]:
                    content["details"] = content.get("details", "") + '<br /><b>{0}:</b> <a href="{1}">{1}</a>'.format(HTMLReportMessaging.DEFAULT_TEXT['url'], e["url"])
                if e["name"]:
                    content["details"] = content.get("details", "") + '<br /><b>{0}:</b> {1}'.format(HTMLReportMessaging.DEFAULT_TEXT['name'], e["name"])
                if e["size"]:
                    content["details"] = content.get("details", "") + '<br /><b>{0}:</b> {1} bytes'.format(HTMLReportMessaging.DEFAULT_TEXT['size'], e["size"])
                if e["duration"]:
                    content["details"] = content.get("details", "") + '<br /><b>{0}:</b> {1} {2}'.format(HTMLReportMessaging.DEFAULT_TEXT['duration'], e["duration"], HTMLReportMessaging.DEFAULT_TEXT['seconds'])

                # finally check for data, else show error
                if e["data"]:
                    # let's show single emojis bigger
                    if len(e["data"]) == 1 and len(bytes(e["data"], 'utf-8')) >2:
                        e["data"] = '<span class="emoji">{}</span>'.format(e["data"])
                else:
                    e["data"] = '<span class="note">{}</span>'.format(HTMLReportMessaging.DEFAULT_TEXT['unknown_value'])

                content.update({k:e})

            # copy files and set path to relative
            elif k.startswith("file_"):
                if k.startswith("file_avatar"):
                    input_file = e
                    if input_file == None:
                        input_file = HTMLReportMessaging.DEFAULT_FILES[k]
                    output_file = self.output_dir_avatar / input_file.name
                    if not output_file.exists():
                            output_file.write_bytes(input_file.read_bytes())
                    content.update({k:output_file.relative_to(self.project_directory)})
                else:
                    if e:
                        if k == "file_thumbnail":
                            output_file = self.output_dir_thumb / e.name
                        else:
                            output_file = self.output_dir_media / e.name

                        if not output_file.exists():
                            output_file.write_bytes(e.read_bytes())
                        content.update({k:output_file.relative_to(self.project_directory)})
                    else:
                        content.update({k:None})

            elif k == "list_contacts":
                if e:
                    for contact in e:
                        contact = contact.__dict__
                    content.update({k:contact})
                else:
                    content.update({k:HTMLReport.DEFAULT_TEXT['unknown_value']})
                    pass
            # convert lists into <li> elements
            elif k.startswith("list_"):
                if e:
                    nl = "\n"
                    content.update({k:"<ul>" + nl.join(map(lambda x: "<li>" + x + "</li>", e)) + "</ul>"})
                    pass
                else:
                    content.update({k:HTMLReport.DEFAULT_TEXT['unknown_value']})
            else:
                content.update({k:data.get(k, HTMLReport.DEFAULT_TEXT['unknown_value'])})
        return content
