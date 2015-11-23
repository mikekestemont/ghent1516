#!usr/bin.env python

# Ex. 1: Can you implement the following grading scheme in Python?

score = 46
grade = 'X'
if score >= 80:
	grade = 'A'
elif score >= 65:
	grade = 'B'
elif score >= 50:
	grade = 'C'
else:
	grade = 'D'
print('You score was '+str(score)+', so you the grade: '+grade+'.')



print("======================================")

# Ex. 2: Write Python code that defines two numbers and prints the largest of
# them. Use an if-then-else tree.


nr1 = 3
nr2 = 4

if nr1 > nr2:
	print(str(nr1))
elif nr1 == nr2:
	print("There equal!")
else:
	print(str(nr2))

print("======================================")