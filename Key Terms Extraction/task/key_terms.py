import nltk
from lxml import etree
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string


tree = etree.parse("news.xml")
root = tree.getroot()
lemmatizer = WordNetLemmatizer()
for news in root[0]:
    for value in news:
        if value.get("name") == "head":
            title = value.text
        if value.get("name") == "text":
            content = value.text
    word_freq = {}
    for word in word_tokenize(content.lower()):
        word = lemmatizer.lemmatize(word)
        if word not in stopwords.words('english') and word not in list(string.punctuation) and nltk.pos_tag([word])[0][1] == 'NN':
            word_freq.setdefault(word, 0)
            word_freq[word] += 1
    sorted_word_freq = sorted(word_freq.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    print(f'{title}:')
    print(*[x[0] for x in sorted_word_freq[:5]])
