import xml.dom.minidom
import fileinput

uglyxml = ''

for line in fileinput.input():
    uglyxml= uglyxml + line

xml = xml.dom.minidom.parseString(uglyxml)
xml_pretty_str = xml.toprettyxml()
print xml_pretty_str