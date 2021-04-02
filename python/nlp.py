#import dependencies
import pandas as pd
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import urllib.request

# Output File (CSV)
output_data_file = "./output_data/words.csv"

response =  urllib.request.urlopen('https://data-bootcamp-036.s3.us-east-2.amazonaws.com/tweets.csv')
html = response.read()
print(html)

soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
print(text)

from nltk.tokenize import TweetTokenizer
tokened = TweetTokenizer()
tokens = tokened.tokenize(text)

# tokens = [t for t in text.split()]
# print(tokens)

#set a variable for the stop words
from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in sr:
        
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)


df = pd.DataFrame(clean_tokens)

df.to_csv(output_data_file)