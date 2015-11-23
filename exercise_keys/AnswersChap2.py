#!usr/bin.env python

# Ex. 1: Consider the following strings `sentence1 = "Mike and Lars kick the bucket"` and `sentence2 = "Bonny and Clyde are really famous"`.
# Split these strings into words and create the following strings via list manipulation:
# `sentence3 = "Mike and Lars are really famous"` and `sentence4="Bonny+and+Clyde+kick+the+bucket"`.
# Can you print the middle letter of the fourth sentence? How can you calculate the middle letters position using the modulus operator?

sentence1 = "Mike and Lars kick the bucket"
sentence2 = "Bonny and Clyde are really famous"
s1_splitted = sentence1.split()
s2_splitted = sentence2.split()

sentence3 = s1_splitted[:3]+s2_splitted[-3:]
sentence3 = " ".join(sentence3)
sentence4 = s2_splitted[:3]+s1_splitted[-3:]
sentence4 = "+".join(sentence4)
print(sentence3)
print(sentence4)


print("======================================")

# Ex. 2: Consider the `lookup` dictionary below. The following letters are still missing from it: 'k':'kilo', 'l':'lima', 'm':'mike'.
# Add them to `lookup`! Could you spell the word "marvellous" in code language now? Collect these codes into the list object `msg`.
# Next, join the items in this list together with a comma and print the spelled out version!

lookup = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 'z':'zulu'}

lookup["k"] = "kilo"
lookup["l"] = "lima"
lookup["m"] = "mike"
msg = []
msg.append(lookup["m"])
msg.append(lookup["a"])
msg.append(lookup["r"])
msg.append(lookup["v"])
msg.append(lookup["e"])
msg.append(lookup["l"])
msg.append(lookup["l"])
msg.append(lookup["o"])
msg.append(lookup["u"])
msg.append(lookup["s"])
with_comma = ",".join(msg)
print(with_comma)


print("======================================")

# -  Ex. 3: Collect the code terms in the lookup dict (`alpha`, `bravo`, ...) from the previous exercise into a list called `code_words`.
# Is this list alphabetically sorted? No? Then make sure that this list is sorted alphabetically. Now remove the items `victor`, `india` and `papa`.
# Append the words `pigeon` and `potato` at the end of this list. Combine this new list of items into a single string, using a semicolon as a delimiter and print this string. 

code_words = lookup.values()
print(code_words)
code_words.sort()
print(code_words)
code_words.remove("victor")
code_words.remove("india")
code_words.remove("papa")
print(code_words)
code_words.append("pigeon")
code_words.append("patato")
print(code_words)
single_string = ";".join(code_words)
print(single_string)


print("======================================")

