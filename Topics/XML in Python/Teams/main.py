from lxml import etree


tree = etree.parse("/Users/liudawei/Desktop/Key Terms Extraction/Topics/XML in Python/Teams/data/dataset/input.txt")
root = tree.getroot()
member_names = []
for member in root[0]:
    member_names.append(member.get("name"))
print(*member_names)



