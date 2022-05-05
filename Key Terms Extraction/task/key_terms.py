from lxml import etree
from nltk.tokenize import word_tokenize


tree = etree.parse("news.xml")
root = tree.getroot()
for news in root[0]:
    for value in news:
        if value.get("name") == "head":
            title = value.text
        if value.get("name") == "text":
            content = value.text
    word_freq = {}
    for word in word_tokenize(content.lower()):
        word_freq.setdefault(word, 0)
        word_freq[word] += 1
    sorted_word_freq = sorted(word_freq.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    print(f'{title}:')
    print(*[x[0] for x in sorted_word_freq[:5]])
