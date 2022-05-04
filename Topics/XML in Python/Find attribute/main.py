from lxml import etree


xml_string, attr = input(), input()
root = etree.fromstring(xml_string)
print(root.get(attr))
