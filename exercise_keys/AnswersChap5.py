#!usr/bin.env python3

# Ex. 1: Two words are anagrams if you can rearrange the letters from one
# to spell the other. Write a function called is_anagram that takes two
# strings and returns True if they are anagrams.


def is_anagram(w1, w2):
	if sorted(w1) == sorted(w2):
		return True
	else:
		return False

print is_anagram("pup", "upp")
print is_anagram("pup", "uppt")

print("======================================")

# Ex. 2:  Go to Project Gutenberg (http://www.gutenberg.org) and download
# your favorite out- of-copyright book in plain text format. Make a frequency
# dictionary of the words in the novel. Sort the words in the dictionary
# by frequency and write it to a text file called frequencies.txt.
# Make sure your program ignores capitalization as well as punctuation
# (hint: check out string.punctuation online!). Search the web in order
# to find out how you can sort a dictionary -- this is not easy, because
# you might have to import another module.

import string
from operator import itemgetter
textF = open("../data/austen-emma.txt", 'rt')
text_with_P = textF.read()
textF.close()
text = ""
for char in text_with_P:
	if char not in string.punctuation:
		text+=char.lower()
words = text.split()
#print words[:50]
freqs = {}
for w in words:
	try:
		freqs[w]+=1
	except KeyError:
		freqs[w]=1
f = open("frequencies.txt", "wt")
for item in sorted(freqs.iteritems(), key=itemgetter(1), reverse=True):
	f.write(item[0]+" >>> "+str(item[1])+"\n")
f.close()

print("======================================")

# Ex. 3: Rewrite the novel in the previous exercise, by replacing
# the name of the principal character in the novel by your own name. 
# (Use the replace() function for this.) Write the new version of
# novel to a file called starring_me.txt.

import string
from operator import itemgetter
textF = open("../data/austen-emma.txt", 'rt')
text_with_P = textF.read()
textF.close()
text = ""
for char in text_with_P:
	if char not in string.punctuation:
		text+=char.lower()
my_novel = string.replace(text, "emma", "mike")
f = open("test.txt", "w")
f.write(my_novel)
f.close()
words = my_novel.split()
print words[:50]
freqs = {}
for w in words:
	try:
		freqs[w]+=1
	except KeyError:
		freqs[w]=1
f = open("starring_me.txt", "wt")
for item in sorted(freqs.iteritems(), key=itemgetter(1), reverse=True):
	f.write(item[0]+" >>> "+str(item[1])+"\n")
f.close()


print("======================================")

# Ex. 4: Define a function sum() and a function multiply()
# that sums and multiplies (respectively) all the numbers in a
# list of numbers. For example, sum([1, 2, 3, 4]) should return 10,
# and multiply([1, 2, 3, 4]) should return 24.

def sum(nums):
	total = 0
	for n in nums:
		total+=n
	return total

def multiply(nums):
	total = 1
	for n in nums:
		total*=n
	return total

l = [1,2,3,4]
print(sum(l))
print(multiply(l))

print("======================================")

# Ex. 5: A hapax legomenon (often abbreviated to hapax) is a 
# word which occurs only once in either the written record
# of a language, the works of an author, or in a single text.
# Define a function that given the file name of a text will
# return all its hapaxes. Make sure your program ignores capitalization
# as well as punctuation (hint: check out string.punctuation online!).
# Try out the function on your Gutenberg book.

def get_hapaxes(f):
	textF = open(f, 'rt')
	text_with_P = textF.read()
	textF.close()
	text = ""
	for char in text_with_P:
		if char not in string.punctuation:
			text+=char.lower()
	words = text.split()
	#print words[:50]
	freqs = {}
	for w in words:
		try:
			freqs[w]+=1
		except KeyError:
			freqs[w]=1
	hapaxes = []
	for w in freqs:
		if freqs[w] == 1:
			hapaxes.append(w)
	return hapaxes

print(get_hapaxes("../data/austen-emma.txt"))

print("==========================")

# Ex. 6: Inside the same module as the previous exercise (i.e.
# a file that ends in .py), create two additional functions:
# one that spots 'hapaxes dislegomena' (words occuring only
# twice) and one that spots 'hapaxes trislegomena' (words
# occuring only three times) in a text file. Now import these
# functions in another, standalone script and call all three
# functions from there. Again, try them out on your Gutenberg-file.

import hapax
print(hapax.legomena("../data/austen-emma.txt"))
print(hapax.dislegomena("../data/austen-emma.txt"))
print(hapax.trislegomena("../data/austen-emma.txt"))


print("==========================")

# Ex. 7: Write a program that given a text file will create
# a new text file in which all the lines from the original
# file are numbered from 1 to n (where n is the number of lines in the file).

def convert2NumberedFormat(f):
	fOldF = open(f, "rt")
	lines = fOldF.readlines()
	fOldF.close()
	fNewF = open("numb_"+f, "wt")
	counter = 1
	for line in lines:
		fNewF.write((counter)+line)
		counter+=1
	fNewF.close()
	return

convert2NumberedFormat(f="frequencies.txt")


print("==========================")

# Ex. 8: Write a script that rolls a dice everytime 
# you run it by generating a random integer between 1 and 6!
# You can import functionality for doing this via random.randint().
# (Google this!)

from random import randint

def roll_dice():
	return randint(1,6)

print(roll_dice())
print(roll_dice())
print(roll_dice())
print(roll_dice())

print("==========================")

# Ex. 9: A sentence splitter is a program capable of splitting a text
# into sentences. The standard set of heuristics for sentence splitting
#includes (but isn't limited to) the following rules:
# Sentence boundaries occur at one of "." (periods), "?" or "!", except that: [...]

fixed_expressions = ["Mr.", "Mrs.", "i.e.", "Jr."]
sentence_boundaries = [".", "!", "?"]

def sentence_splitter(oldFile, newFile):
	newF = open(oldFile, 'rt')
	text = newF.read()
	newF.close()
	sentences = []
	sentence = "" # tmp container
	# text = "Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."
	text = text.strip()
	i = 0
	while i < len(text)-1:
		char = text[i]
		if char not in sentence_boundaries:
			sentence+=char
		else:
			sentence+=char
			if text[i+1] == " " and text[i+2].isupper():
				expression_used = False
				for expression in fixed_expressions:
					if sentence.endswith(expression):
						expression_used = True
				if not expression_used:
					if len(sentence) > 0:
						sentences.append(sentence.strip())
						sentence = ""
		i+=1
		# check for leftover at the end:
		if i == len(text)-1:
			char=text[i]
			sentence+=char
			if len(sentence.strip()) > 0:
				sentences.append(sentence.strip())
	tokenF = open(newFile, 'wt')
	for s in sentences:
		print(s+"\n")
	tokenF.close()
	return sentences

sentence_splitter(oldFile="../data/austen-emma.txt", newFile="tokenized.txt")