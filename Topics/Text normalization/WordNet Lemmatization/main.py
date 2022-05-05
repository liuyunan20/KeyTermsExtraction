from nltk.stem import WordNetLemmatizer


word = input()
lemmatizer = WordNetLemmatizer()
for tag in ['n', 'a', 'v']:
    print(lemmatizer.lemmatize(word, pos=tag))
