from sklearn.feature_extraction.text import TfidfVectorizer


vectorizer = TfidfVectorizer(input='file', use_idf=True, lowercase=True,
                             analyzer='word', ngram_range=(1, 1),
                             stop_words=None)
dataset = open('/Users/liudawei/Desktop/Key Terms Extraction/Topics/TF-IDF vectorizer/Old MacDonald Had A Farm/data/dataset/input.txt', 'r')
tfidf_matrix = vectorizer.fit_transform([dataset])
print(tfidf_matrix[(0, 10)])
