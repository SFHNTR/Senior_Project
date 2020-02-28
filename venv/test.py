import urllib.request
from bs4 import BeautifulSoup
import nltk
userUrl = "https://www.pcgamer.com/baldurs-gate-3-gameplay-preview/"
webUrl  = urllib.request.urlopen(userUrl)
article = BeautifulSoup(webUrl.read())
#finds all the paragraphs in the article, puts this data into an array
paragraphs = article.find_all('p')
articleText = ""
#for all the paragraphs in the array, put it into one string
for p in paragraphs:
    articleText += p.text +'\n'
##sentence_list = nltk.sent_tokenize(articleText)
file = open("data.txt", "w")
file.write(articleText)
file.close()
