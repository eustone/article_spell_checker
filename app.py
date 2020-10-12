import newspaper
import enchant
from nltk import word_tokenize, download
import re

#download('punkt')
url = 'https://hackernoon.com/dilemmas-of-a-digital-lifestyle-27c044940157'

article = newspaper.Article(url, language='en')

article.download()
article.parse()

d = enchant.Dict("en_US")
non_dict_words = list(set([word.encode('ascii', 'ignore') for word in word_tokenize(article.text)
                           if d.check(word) is False and re.match('^[a-zA-Z]*$', word)]))

print(non_dict_words)

non_dict_words






