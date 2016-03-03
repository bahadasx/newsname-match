#Title:         NewsName Matcher
#Version:       1.0
#Author:        Sasan Bahadaran
#Date:          2/23/16
#Organization:  District Data Labs

##############################################
#   IMPORTS
##############################################
import os,sys
import nltk, re, pprint
import codecs
from fuzzywuzzy import fuzz

#list of main candidates
candidates = ["Woodrow Wilson","Charles E. Hughes","Allan L. Benson","Frank Hanly","Arthur E. Reimer"]

def performNameExtraction(text):
	#Returns a list of what NLTK defines as persons after processing the text passed into it.
	try:
		entity_names = []
		for sent in nltk.sent_tokenize(text):
			for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
				if hasattr(chunk, 'label') and chunk.label:
    					if chunk.label() == 'PERSON':
						entity_names.append(' '.join(child[0] for child in chunk.leaves()))
	except:
		print "Unexpected error:", sys.exc_info()[0]
	return entity_names

def processFiles():
	#process every file in data folder
	DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures'))
	pathjoin = os.path.join
	for fn in os.listdir(DATA_DIR):
   		with codecs.open(pathjoin(DATA_DIR, fn), 'r',encoding='utf-8', errors='ignore') as text_file:
        		text = text_file.read()
        		entity_names = performNameExtraction(text)

	return entity_names

def normalize_field(value):
	#make text lowercase and strip white space
	
	return value.lower().replace(" ", "")

def fuzzblock(n1, n2, threshold=85):
	"""
	Returns True if the similarity of n1 and n2 is above the threshold.
	"""

	return similarity(n1, n2) > threshold

def similarity(n1, n2):
	"""
	Returns the mean of the partial_ratio score for each field in the two
	entities. Note that if they don't have fields that match, the score will
	be zero.
	"""

	scores = [
		fuzz.partial_ratio(n1, n2)
    	]

	return float(sum(s for s in scores)) / float(len(scores))

if __name__ == '__main__':
	entity_names = processFiles()
	print entity_names
	for e_name in entity_names:
		for c_name in candidates:
			if fuzzblock(c_name,e_name):
				print c_name
				print e_name

