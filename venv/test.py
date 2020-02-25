import urllib.request
from bs4 import BeautifulSoup
import nltk
userUrl = "https://www.cnbc.com/2020/02/25/apple-and-johnson-johnson-launch-study-to-predict-stroke-risk-with-apple-watch.html"
webUrl  = urllib.request.urlopen(userUrl)
article = BeautifulSoup(webUrl.read())
#finds all the paragraphs in the article, puts this data into an array
paragraphs = article.find_all('p')
articleText = ""
#for all the paragraphs in the array, put it into one string
for p in paragraphs:
    articleText += p.text
sentence_list = nltk.sent_tokenize(articleText)
