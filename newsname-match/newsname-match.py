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

#map for name variations
name_map = {}

#list of main candidates
candidates = ["Woodrow Wilson","Charles E. Hughes","Allan L. Benson","Frank Hanly","Arthur E. Reimer"]

class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)

def performNameExtraction(text):
	#Returns a list of what NLTK defines as persons after processing the text passed into it.
	try:
		entity_names = []
		for sent in nltk.sent_tokenize(text):
			for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
				if hasattr(chunk, 'label') and chunk.label:
    					if chunk.label() == 'PERSON':
						name_value = ' '.join(child[0] for child in chunk.leaves())
						if name_value not in entity_names:
							entity_names.append(name_value)
	except:
		print "Unexpected error:", sys.exc_info()[0]
	return entity_names

def processFiles():
	#process every file in data folder
	data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'fixtures'))
	pathjoin = os.path.join
	for fn in os.listdir(data_dir):
   		if not fn.startswith('otherfiles'):
			with codecs.open(pathjoin(data_dir, fn), 'r',encoding='utf-8', errors='ignore') as text_file:
        			text = text_file.read()
        			entity_names = performNameExtraction(text)

	return entity_names

def normalize_field(value):
	#make text lowercase and strip white space
	
	return value.lower().replace(" ", "")

def fuzzblock(n1, n2, threshold):
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
	for e_name in entity_names:
		for c_name in candidates:
			if e_name not in name_map.values():
				if fuzzblock(c_name,e_name,85):
					name_map[c_name] = e_name

	for key,value in name_map.iteritems():
		print 'key:' + key,'value: ' + value
