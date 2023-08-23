import os
from random import randint
import pickle
import re

cur_dir = os.path.dirname(__file__)

stop_words = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'stopwords.pkl'), 'rb'))

model = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'), 'rb'))
vect = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'vectorizer.pkl'), 'rb'))

aneks = []
with open(os.path.join(cur_dir, 'pkl_objects', 'anek.txt'), 'r') as data:
    for _ in range(10000):
        aneks.append(data.readline()[15:])
        data.readline()

def analysis(text, clf=model, vectorizer=vect):
    pred = clf.predict(vectorizer.transform([text]))[0]
    print(pred)
    return aneks[randint(0, 10000)] if pred < 0 else 'Рад за вас!'
