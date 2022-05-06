import nltk


sent = ['The', 'horse', 'that', 'was', 'raced', 'past', 'the', 'barn', 'fell', 'down', '.']
for word in nltk.pos_tag(sent):
    if word[0] == 'raced':
        print(word[1])
