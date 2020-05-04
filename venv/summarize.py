import urllib.request
from bs4 import BeautifulSoup
import nltk
import re
import heapq

def summarizetext(userUrl):
    webUrl  = urllib.request.urlopen(userUrl)
    article = BeautifulSoup(webUrl.read())
    #finds all the paragraphs in the article, puts this data into an array
    paragraphs = article.find_all('p')
    articleText = ""
    #for all the paragraphs in the array, put it into one string
    for p in paragraphs:
        articleText += p.text
    #removes numbers and special characters before proccessing
    articleText = re.sub(r'\[[0-9]*\]', ' ', articleText)
    articleText = re.sub(r'\s+', ' ', articleText)
    #removes numbers from processing, not needed for summerization
    #formatted text used specifically for word frequency analysis
    formatedText = re.sub('[^a-zA-Z]', ' ', articleText)
    formatedText = re.sub(r'\s+', ' ', articleText)

    #tokenizes the sentences
    sentenceArray = nltk.sent_tokenize(articleText)

    stopWords = nltk.corpus.stopwords.words('english')

    wordFrequency = {}
    for word in nltk.word_tokenize(formatedText):
        if word not in stopWords:
            if word not in wordFrequency.keys():
                wordFrequency[word] = 1
            else:
                wordFrequency[word] += 1

    maximumFrequency = max(wordFrequency.values())

    for word in wordFrequency.keys():
        wordFrequency[word] = wordFrequency[word]/maximumFrequency

    sentenceScores = {}
    for sent in sentenceArray:
        for word in nltk.word_tokenize(sent.lower()):
            if word in wordFrequency.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentenceScores.keys():
                        sentenceScores[sent] = wordFrequency[word]
                    else:
                        sentenceScores[sent] += wordFrequency[word]

    summary = heapq.nlargest(7, sentenceScores, key=sentenceScores.get)
    summary = '\n'.join(summary)
    return summary
