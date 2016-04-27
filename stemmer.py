from __future__ import unicode_literals
from gensim import models as md
import codecs

def threshold(word, model):
	number = 3
	similiarWords = model.most_similar(word, topn=number)
	distance = similiarWords[len(similiarWords)-1][1]
	while(distance > 0.51):
		number = number + 1
		similiarWords = model.most_similar(word, topn=number)
		distance = similiarWords[len(similiarWords)-1][1]
	for item in similiarWords:
		print item[0]
	print "-------"	
	return similiarWords

def largestSubstring(word, similiarWords):
	pointer = len(word);
	stem = word	
	maximum = 0
	current = 0
	position = 0
	substring = ""
	limit = 2	
	if len(word)<3:
		limit = len(word)-1
	for char in range(len(word),limit,-1):	
		for candidate in similiarWords:
			#print stem[0:pointer]
			if stem[0:pointer] == candidate[0][0:pointer]:
				current = current + 1
		if current > maximum:
			maximum = current
			position = pointer
		pointer = pointer -1
		current = 0
	substring = stem[0:position]
	if(len(substring) > 0):
		parser(similiarWords, substring)

def parser(similiarWords, substring):
	global stems
	global suffixes
	stems.append(substring)
	for candidate in similiarWords:
			if substring == candidate[0][0:len(substring)]:
				remaining = candidate[0][len(substring):]		
				if len(remaining) > 0:				
					suffixes.append(candidate[0][len(substring):])

def write(suffixes, stems):
	with codecs.open('parser/suffixes.txt', 'w', 'utf-8') as suf_file:
		for item in suffixes:
			try:	
        			suf_file.write("%s\n" % item)
			except Exception as e:
    				 print str(e)
				 pass
	with codecs.open('parser/stems.txt', 'w', 'utf-8') as suf_file2:
		for item in stems:
			try:
				suf_file2.write("%s\n" % item)
			except Exception as e:
    				print str(e)
				pass
	

stems = []
suffixes = []
f = codecs.open('parser/metusabanci_kelimeler_lowercase2.txt', encoding='utf-8')
for line in f:
    words = f.read().splitlines()
model = md.Word2Vec.load_word2vec_format('tvec.bin', binary=True)
c = 0
for word in words:
	try:
		c = c + 1
		print 'count: ', c	
		similiarWords = model.most_similar(word, topn=20)
		largestSubstring(word, similiarWords)
	except:
		pass

write(suffixes, stems)
print "done"
