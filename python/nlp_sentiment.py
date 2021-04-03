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

response =  urllib.request.urlopen('https://data-bootcamp-036.s3.us-east-2.amazonaws.com/tweets.csv')
html = response.read()
# print(html)

soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
# print(text)

from nltk.tokenize import TweetTokenizer
tokened = TweetTokenizer()
tokens = tokened.tokenize(text)


def remove_noise(tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

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
    return cleaned_tokens
    # print(cleaned_tokens)


def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token
        print(token)

def get_tweets_for_model(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tokens)


# print(tweet_tokens[0])
# print(pos_tag(tweet_tokens[0]))

if __name__ == "__main__":

    # positive_tweets = twitter_samples.strings('positive_tweets.json')
    # negative_tweets = twitter_samples.strings('negative_tweets.json')

    positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
    negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

    stop_words = stopwords.words('english')

    positive_cleaned_tokens_list = []
    negative_cleaned_tokens_list = []
 
    for tokens in positive_tweet_tokens:
        positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    for tokens in negative_tweet_tokens:
        negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    # all_pos_words = get_all_words(cleaned_tokens_list)

    freq_dist_pos = FreqDist(tokens)
    # print(freq_dist_pos.most_common(10))

    positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
    negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)
    cleaned_tokens_for_model = get_tweets_for_model(cleaned_tokens_list=tokens)

    positive_dataset = [(tweet_dict, "Positive")
                        for tweet_dict in positive_tokens_for_model]

    negative_dataset = [(tweet_dict, "Negative")
                        for tweet_dict in negative_tokens_for_model]

    undefined_dataset = [(tweet_dict, "undefined")
                        for tweet_dict in cleaned_tokens_for_model]

    dataset = positive_dataset + negative_dataset
    testset = undefined_dataset

    random.shuffle(dataset)

    train_data = dataset[:7000]
    test_data = testset[:7000]

    classifier = NaiveBayesClassifier.train(train_data)

    # print("Accuracy is:", classify.accuracy(classifier, test_data))

    # print(classifier.show_most_informative_features(10))

    # custom_tweet = "Thank you for sending my baggage to CityX and flying me to CityY at the same time. Brilliant service. #thanksGenericAirline"

    # custom_tokens = remove_noise(word_tokenize(custom_tweet))

    # print(classifier.classify(dict([token, True] for token in tokens)))

    
    # print(remove_noise(tokens, stop_words))
    
# print(positive_tweet_tokens[500])
# print(positive_cleaned_tokens_list[500])
