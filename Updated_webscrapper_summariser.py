# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 12:48:08 2019

@author: ibm
"""

import bs4 as bs  
import urllib.request  
import re
import nltk
from gensim.summarization import summarize

scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/IBM')  
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:  
    article_text += p.text

# Removing Square Brackets and Extra Spaces
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
article_text = re.sub(r'\s+', ' ', article_text)  

#print(article_text)

# Removing special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

#Now we have two objects article_text, which contains the original article and 
#formatted_article_text which contains the formatted article. We will use 
#formatted_article_text to create weighted frequency histograms for the words and
# will replace these weighted frequencies with the words in the article_text object.

#Converting Text To Sentences

#At this point we have preprocessed the data. Next, we need to tokenize the article 
#into sentences. We will use thearticle_text object for tokenizing the article to sentence since it contains full stops. The formatted_article_text does not contain any punctuation and therefore cannot be converted into sentences using the full stop as a parameter.

#The following script performs sentence tokenization:

#sentence_list = nltk.sent_tokenize(article_text)  

print (summarize(article_text, split=True))

#from gensim.summarization import keywords

#print(keywords(article_text))
























