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

# # Output File (CSV)
# output_data_file = "./output_data/words.csv"

# scrape the data(tweets) from the the S3 bucket after it's called in
response =  urllib.request.urlopen('https://data-bootcamp-036.s3.us-east-2.amazonaws.com/april_tweets.csv')
html = response.read()
# print(html)

# pull data out of the html response and strip all html tags
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
# print(text)



# removes noise and cleans out symbols and numbers not needed for our use
def remove_noise(tokens, stop_words=()):

    cleaned_tokens = []
    for token, tag in pos_tag(tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                        '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        token = re.sub("0,1,2,3,4,5,6,7,8,9,¦,�,€,™","",token)

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

    return(cleaned_tokens)


def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token

def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)

if __name__ == "__main__":

    # tokenize the data (split into separate words)

    tokened = TweetTokenizer()
    tokens = tokened.tokenize(text)

    stop_words = stopwords.words('english')+['0','1','2','3','4','5','6','7','8','9','¦','�','€','[0-9]']

    positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
    negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

    positive_cleaned_tokens_list = []
    negative_cleaned_tokens_list = []
    april_cleaned_tokens_list = []

    for tokens in positive_tweet_tokens:
        positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    for tokens in negative_tweet_tokens:
        negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    for token in tokens:
        april_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
    negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)
    monday_tokens_for_model = get_tweets_for_model(april_cleaned_tokens_list)

    positive_dataset = [(tweet_dict, "Positive")
                            for tweet_dict in positive_tokens_for_model]

    negative_dataset = [(tweet_dict, "Negative")
                            for tweet_dict in negative_tokens_for_model]

    test_dataset = [(tweet_dict, "")
                            for tweet_dict in monday_tokens_for_model]

    dataset = positive_dataset + negative_dataset

    random.shuffle(dataset)

    train_data = dataset
    testdata = test_dataset

    classifier = NaiveBayesClassifier.train(train_data)

    # returns a list of the most frequent words used
    print(classifier.classify(dict([token, True] for token in tokens)))

    print(classifier.show_most_informative_features(10))