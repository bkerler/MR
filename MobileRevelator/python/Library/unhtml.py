from html.parser import HTMLParser
from html.entities import name2codepoint
import re

class _DeHTMLParser(HTMLParser):
    def __init__(self):
         HTMLParser.__init__(self)
         self.__text = []
         self.hide_output = False

    def handle_starttag(self, tag, attrs):
         if tag in ('p', 'br') and not self.hide_output:
            self.__text.append('\n')
         elif tag in ('script', 'style'):
            self.hide_output = True

    def handle_startendtag(self, tag, attrs):
         if tag == 'br':
            self.__text.append('\n')

    def handle_endtag(self, tag):
         if tag == 'p':
            self.__text.append('\n')
         elif tag in ('script', 'style'):
            self.hide_output = False

    def handle_data(self,text):
         if text and not self.hide_output:
            self.__text.append(re.sub(r'\s+', ' ', text))

    def handle_entityref(self,name):
         if name in name2codepoint and not self.hide_output:
            c = chr(name2codepoint[name])
            self.__text.append(c)

    def handle_charref(self,name):
         if not self.hide_output:
            n = int(name[1:], 16) if name.startswith('x') else int(name)
            self.__text.append(chr(n))

    def get_text(self):
         return re.sub(r' +', ' ', ''.join(self.__text))

def html_to_text(html):
    parser = _DeHTMLParser()
    try:
      parser.feed(str(html))
      parser.close()
    except:
      pass
    return parser.get_text()