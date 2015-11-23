#!/usr/bin/env python

import re

#ex. 1
equal = re.compile(r"\s*\=\s*")
f = open("regex_ex1.txt", 'r')
info_dict = {}
for line in f.readlines():
	line = line.strip()
	key, val = equal.split(line)
	info_dict[key] = val
f.close()
print(info_dict)

#ex. 2
comma = re.compile(r"\s*\,\s*")
f = open("regex_ex2.txt", 'r')
info_list = []
for line in f.readlines():
	line = line.strip()
	fields = comma.split(line)
	info_list.append(fields)
f.close()
print(info_list)

#ex.3
comma = re.compile(r"\s*\,\s*")
f = open("regex_ex3.txt", 'r')
dict_list = []
lines = f.readlines()
names = comma.split(lines[0].strip())
for line in lines[1:]:
	fields = comma.split(line.strip())
	tmp_dict = {}
	for name, field in zip(names, fields):
		tmp_dict[name] = field
	dict_list.append(tmp_dict)
f.close()

whitespace = re.compile(r"\s+")

#ex. 4
def my_funct(fname):
	whitespace = re.compile(r"\s+")
	f = open(fname, "r")
	text = f.read()
	f.close()
	two_chars = set()
	words = whitespace.split(text)
	for word in words:
		if len(word) > 2:
			two_chars.add(word)
	return two_chars
print my_funct("austen-emma-excerpt.txt")

#ex. 5
time_of_day = re.compile(r"[0-9]+\:[0-9]+ *(am)|(pm)")
s = "In the morning, the clock sometimes reads 9:14 am, while in the evening it might read 11:20 pm"
print(len(time_of_day.findall(s)))


([a-z|A-Z]|[0-9]|\.|\_)+


#ex. 6
at = re.compile(r"\@")
dot = re.compile(r"\.")
unorthodox_punct = re.compile("\;|\,|\?|\=|\,|\:") # etc.
extensions = (".com", ".org", ".be", ".nl")
def validate_email(address=""):
	if len(dot.findall(address)) < 1:
		return False
	elif len(at.findall(address)) < 1:
		return False
	elif len(at.findall(address)) > 1:
		return False
	elif not address.endswith(extensions):
		return False
	elif unorthodox_punct.match(address):
		return False
	else:
		return True
print(validate_email("mike.kestemont@gmail.com"))
print(validate_email("mike.kestemont@gmail.xxx"))
print(validate_email("mike.kestemontgmail.com"))
print(validate_email("mikekestemont@gmailcom"))
print(validate_email("mike@kestemont@gmail.com"))