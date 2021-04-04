#import dependencies
import os
import json
from nltk.corpus.reader import twitter
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.tokenize import TweetTokenizer, word_tokenize
from nltk.corpus import stopwords, twitter_samples
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
import re, string, random
from nltk import FreqDist, classify, NaiveBayesClassifier

# Output File (CSV)
output_data_file = "./output_data/words.csv"

response =  urllib.request.urlopen('https://data-bootcamp-036.s3.us-east-2.amazonaws.com/tweets.csv')
html = response.read()
# print(html)

soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
# print(text)

from nltk.tokenize import TweetTokenizer
tokened = TweetTokenizer()
tokens = tokened.tokenize(text)

# def remove_noise(tokens, stop_words = ()):
stop_words = stopwords.words('english')+['0','1','2','3','4','5','6','7','8','9','¦','�','€','[0-9]']
cleaned_tokens = []

for token, tag in pos_tag(tokens):
    token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                    '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
    token = re.sub("(@[A-Za-z0-9_]+)","", token)

    token = re.sub("0,1,2,3,4,5,6,7,8,9,¦,�,€","",token)

    if tag.startswith("NN"):
        pos = 'n'
    elif tag.startswith('VB'):
        pos = 'v'
    else:
        pos = 'a'

    lemmatizer = WordNetLemmatizer()
    token = lemmatizer.lemmatize(token, pos)

    if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
        cleaned_tokens.append(token.lower())

    # print(cleaned_tokens)

freq_dist_all = FreqDist(cleaned_tokens)
print(freq_dist_all.most_common(20))

df = pd.DataFrame(cleaned_tokens)

df.to_csv(output_data_file)