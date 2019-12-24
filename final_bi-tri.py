import re
import nltk
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder

def preprocess(self):
	with open(self, 'r', encoding="utf8", errors='ignore') as source:
		for reflections in source:
			entry = reflections.rstrip()
			case = entry.casefold() 
			punct = re.sub(r'[^\w\s]', '', case)
			numb = ''.join([i for i in punct if not i.isdigit()])
			tokens = nltk.wordpunct_tokenize(numb)
			return tokens

def bigram_process(path:str):
	stop_w = set(stopwords.words('english'))
	diction = []
	text = preprocess(path)
	for words in text:
		if words not in stop_w:
			diction.append(words)
	results = nltk.bigrams(diction)
	fdist = nltk.FreqDist(results)
	tmp = list()
	for k, v in fdist.items():
		newt = (v, k)
		tmp.append(newt)
	tmp = sorted(tmp, reverse=True)
	for v, k in tmp[:225]:
		print(k, v)

def trigram_process(path:str):
	stop_w = set(stopwords.words('english'))
	diction = []
	text = preprocess(path)
	for words in text:
		if words not in stop_w:
			diction.append(words)
	results = nltk.trigrams(diction)
	fdist = nltk.FreqDist(results)
	tmp = list()
	for k, v in fdist.items():
		newt = (v, k)
		tmp.append(newt)
	tmp = sorted(tmp, reverse=True)
	for v, k in tmp[:115]:
		print(k, v)

print(len(preprocess('ywp-1.txt')))
print(len(preprocess('ywp-2.txt')))
bigram_process('ywp-1.txt')
trigram_process('ywp-1.txt')
bigram_process('ywp-2.txt')
trigram_process('ywp-2.txt')
