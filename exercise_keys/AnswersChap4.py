#!usr/bin.env python

# Ex. 1: Define a sentence and split it into words along whitespace.
# Now fill a dictionary that holds the frequencies (value) for each word (key)
# in the sentence. You should first check whether a word is already#
# present in your dictionary. If it is, augment its frequency.
# Else, you should first initialize its frequency

sentence = "In principio erat Verbum et Verbum erat apud Deum et Deus erat Verbum Hoc erat in principio apud Deum Omnia per ipsum facta sunt et sine ipso factum est nihil quod factum est In ipso vita erat et vita erat lux hominum"
words = sentence.lower().split()
frequencies = {}
for word in words:
	if word in frequencies:
		frequencies[word]+=1
	else:
		frequencies[word]=1
print(frequencies)

print("======================================")

# Ex. 2: By now, you already know that Python has the len() function
# built-in, but can you write yourself a code block that prints
# the length of the string lengthy_word that you will define?
# First use a for loop; then try to achieve the same results
# with a while loop, but watch out that you don't get stuck an infinite loop!

count = 0
for char in lengthy_word:
	count+=1
print("Length (for-loop): "+str(count))
count, index = 0, 0

count = 0
while index < len(lengthy_word):
	count+=1
	index+=1 # don't forget to increment!
print("Length (while-loop): "+str(count))

print("======================================")

# Ex. 3: Have another look at the string variable lenghty_word
# that you defined in the previous exercices. Can you write a
# code block that fills a dictionary char_freqs containing the
# frequency of the different individual characters in length_word?

lengthy_word = "thisisthelongestwordontheplanet"
char_dict = {}
for char in lengthy_word:
	if char in char_dict:
		char_dict[char]+=1
	else:
		char_dict[char]=1
print(char_dict)

print("======================================")

# Ex. 4: Let's have yet another look at lengthy_word. Can you write code
# that creates the dictionary next_char that holds for each first
# occurence of a character (key) the next character in the word as
# value. If the character is already in the dictionary,
# do nothing and if you're dealing with the last character in the word,
# add "Last word!" as value to the dictionary for this character.
# Look up the use of pass in Python online and use it in this exercise.
# Use list indices and raise/catch exceptions to achieve this!

lengthy_word = "thisisthelongestwordontheplanet"
next_char = {}
for i, char in enumerate(lengthy_word):
	if i == (len(lengthy_word)-1):
		next_char[char] = "Last word!"
	else:
		# check whether the next letter is already in there:
		if char not in next_char:
			nc = lengthy_word[i+1]
			next_char[char] = nc
print(next_char)

print("======================================")

# Ex. 5: Write a code block that defines a list of integers and
# prints them as a histogram to the screen. For example, histogram = [4, 9, 7, 2, 16, 8, 3]) should print the following:

my_list = [4, 9, 7, 2, 16, 8, 3]
for item in my_list:
	print(item*"+")

print("======================================")

# Ex. 6: "99 Bottles of Beer" is a traditional song in the United States
# and Canada. It is popular to sing on long trips, as it has a very
# repetitive format which is easy to memorize, and can take a long time
# to sing. The song's simple lyrics are as follows: "99 bottles of beer
# on the wall, 99 bottles of beer. Take one down, pass it around, 98
# bottles of beer on the wall." The same verse is repeated, each time
# with one fewer bottle. The song is completed when the singer or singers
# reach zero. Your task here is write a Python code block capable of
# generating all the verses of the song. Use a counter integer variable
# and a while loop. Make sure that your loop will come to an end!

counter = 100
while counter > 0:
	print("* Strophe *")
	counter-=1
	if counter <= 1:
		print(str(counter)+" bottle of beer on the wall, "+str(counter)+" bottle of beer.")
	else:
		print(str(counter)+" bottles of beer on the wall, "+str(counter)+" bottles of beer.")
		print(str(counter-1)+" bottle of beer on the wall, "+str(counter-1)+" bottle of beer.")

print("======================================")

# Ex. 7: The third person singular verb form in English is
# distinguished by the suffix -s, which is added to the stem
# of the infinitive form: run -> runs. A simple set of
# rules can be given as follows: "If the verb ends in y,
# remove it and add ies. If the verb ends in o, ch, s, sh, x or z,
# add es. By default just add s."
# Your task in this exercise is to write a code block
# which given a verb in infinitive form, prints its third
# person singular form. Test your function with words like
# "try", "brush", "run" and "fix". Can you think of verbs for
# which your code doesn't work? Check out the string method
# .endswith() online!

verb = "justify"
if verb.endswith("y"):
	inflected = verb[:-1]+"ies"
	print(inflected)
elif verb[-1] in ["o", "s", "x", "z", "ch", "sh"]:
	inflected = verb+"es"
	print(inflected)
else:
	inflected = verb+"s"
	print(inflected)

print("======================================")

# Ex. 8: ROT13 is a way to encode secret messages in cryptography.
# The name comes from Julius Caesar, who used it to communicate with his generals.
# ROT13 ("rotate by 13 places") is a widely used example of a Caesar cipher.
# The idea is to rotate or augment the position of each character in the alphabet with thirteen places.
# Your task in this exercise is to implement an encoder/decoder of ROT-13.
# For this, you will need to create a list containing each letter in the (lowercase) roman alphabet
# as well as the whitespace character. Once you're done, you will be able to read
# the following secret message: "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"

lookup_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
decode_dict, encode_dict = {}, {}
for orig_char in lookup_alphabet:
	orig_index = lookup_alphabet.index(orig_char)
	new_index = orig_index+13
	if new_index >= len(lookup_alphabet):
		new_index -= len(lookup_alphabet)
	new_char = lookup_alphabet[new_index]
	encode_dict[orig_char] = new_char
	decode_dict[new_char] = orig_char
# add whitespace character for readability
encode_dict[' '] = ' '
decode_dict[' '] = ' '
# decode:
msg = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
msg = msg.lower()
decoded = ""
for char in msg:
	if char in decode_dict:
		decoded+=decode_dict[char]
print(decoded)
# encode
encoded = ""
for char in decoded:
	try:
		encoded+=encode_dict[char]
	except KeyError:
		pass
print(encoded)

print("======================================")


