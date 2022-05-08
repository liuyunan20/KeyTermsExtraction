import nltk
from lxml import etree
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from sklearn.feature_extraction.text import TfidfVectorizer


tree = etree.parse("news.xml")
root = tree.getroot()
lemmatizer = WordNetLemmatizer()
vectorizer = TfidfVectorizer()
news_text = []
titles = []
# arrange titles and news text for all news
for news in root[0]:
    for value in news:
        if value.get("name") == "head":
            titles.append(value.text)
        if value.get("name") == "text":
            content = value.text
    news_words = ''

    for word in word_tokenize(content.lower()):
        word = lemmatizer.lemmatize(word)
        if word not in stopwords.words('english') and word not in list(string.punctuation) and nltk.pos_tag([word])[0][1] == 'NN':
            news_words += word + ' '
            # print(news_words)
    news_text.append(news_words)

vectorizer.fit(news_text)
# print(vectorizer.vocabulary_)

for title, news in zip(titles, news_text):
    word_score = {}
    scores = vectorizer.transform([news]).toarray()
    # print(scores)
    for i, word in enumerate(news.split()):
        word_score[word] = scores[0][i]
    sorted_word_freq = sorted(word_score.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    print(f'{title}:')
    print(*[x[0] for x in sorted_word_freq[:5]])
