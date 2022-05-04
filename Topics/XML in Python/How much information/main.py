from lxml import etree


root = etree.fromstring(input())
elements_num = len(root)
attributes_num = len(root.keys())
print(f'{elements_num} {attributes_num}')
