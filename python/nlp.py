#import dependencies
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import urllib.request

response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()
print(html)

soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
print(text)

tokens = [t for t in text.split()]
print(tokens)

#set a variable for the stop words
from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)