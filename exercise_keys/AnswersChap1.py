#!usr/bin/env python

# Ex. 1:
# Suppose the cover price of a book is 24.95 EUR, but bookstores get a 40 percent discount.
# Shipping costs 3 EUR for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?
# Print the result in a pretty fashion, using casting where necessary!

cover_price = 24.95
store_price = cover_price/100*60
price_first_book = store_price+3
price_rest_books = (store_price+0.75)*59
wholesale = price_first_book+price_rest_books
print("The wholesale price is: "+str(wholesale))

print "=========================================="

# Ex. 2: Can you identify and explain the errors in the following lines of code? Correct them please!

# print("A message"). > the dot at the end doesn't serve a function
# print("A message') > the quotation marks that enclose the string don't match (single vs. double)
# print('A message"') > nothing is actually wrong with this: you can use double quotes inside single quotes and vice versa.

print "=========================================="

# Ex. 3: When something is wrong with your code, Python will raise errors. [...]
# A good example is the `ZeroDivisionError`. Try to make Python throw such a ZeroDivisionError!

# Note that 0/5 doesn't raise an error, but 5/0 does!

print "=========================================="

# Ex. 4: Write a program that assigns the result of `9.5 * 4.5 - 2.5 * 345.5 - 3.5` to a variable.
# Print this variable. Use round brackets to indicate 'operator precedence'
# and make sure that subtractions are performed before multiplications.
# When you convert the outcome to a string, how many characters does it count?

number = 9.5 * (4.5 - 2.5) * (345.5 - 3.5)
print(number)
str_number = str(number)
print(len(str_number))

print "=========================================="

# Ex. 5: Define the variables `a=2`, b=`20007` and c=`5`. Using only the operations you learned about above,
# can you now print the following numbers: `2005`, `252525252`, `2510`, `-60025` and `2002507`?

a = 2
b = 20007
c = 5

print(str(a)+str(b)[1:3]+str(c))
print(((str(a)+str(c))*4)+str(a))
print(str(a)+str(c)+str(a*c))
print(b-b*4-2*a)
print(str(b)[:3]+str(a)+str(c)+(str(b)[-2:]))

print "=========================================="

# Ex. 6: Define three variables names `var1`, `var2` and `var3`. 
# Calculate the average of these variables and assign it to `average`.
# Print the result in a fancy manner. Add three comments to this piece of code using three different ways.

var1 = 3
var2 = 6 # here, we define var2
var3 = 7
"""
Now we are going to calculate
the actual
average:
"""
average = (var1+var2+var3)/3
print("The average is: "+str(average))
'''Done!'''

print "=========================================="

# Ex. 7: Write a little program that can compute the surface of circle,
# using the variables `radius` and `pi=3.14159`. The formula is of course radius,
# multiplied by radius, multiplied by `pi`.
# Print the outcome of your program as follows: 'The surface area of a circle with radius ... is: ...'.

radius = 6
pi = 3.14159
surface = radius*radius*pi
print("The surface area of a circle with radius "+str(radius)+" is: "+str(surface)+".")

print "=========================================="

# Ex. 8: There is one operator (like the ones for multiplication and subtraction)
# that we did not mention yet, namely the modulus operator `%`. Could you figure by yourself
# what it does when you place it between two numbers (e.g. 113 % 9)? (PS: It's OK to get help online...)
# You don't need this operator all that often, but when you do, it comes in really handy!

print(10%3) # this gives you the so-called 'rest' of the integer division between two whole numbers
print(4%5)

print "=========================================="

# Ex. 9: Write a code block that classifies a given amount of money into smaller monetary units.
# Set the `amount` variable to 11.56. You code should outputs a report listing the monetary equivalent in dollars, quarters, dimes, nickels, and pennies.
# Your program should report the maximum number of dollars, then the number of quarters, dimes, nickels, and pennies, in this order, to result in the minimum number of coins.
# Here are the steps in developing the program:
# * Convert the amount (11.56) into cents (1156).
# * Divide the cents by 100 to find the number of dollars, but first subtract the rest using the modulus operator!
# * Divide the remaining cents by 25 to find the number of quarters, but first subtract the rest using the modulus operator!
# * Divide the remaining cents by 10 to find the number of dimes etc.
# * Divide the remaining cents by 5 to find the number of nickels etc.
# * The remaining cents are the pennies. Now display the result for your cashier!

dollars = 0.0
quarters = 0.0
dimes = 0.0
nickels = 0.0
pennies = 0.0

amount = 11.56
cents = 100*amount

# dollars:
cents_for_quarters_and_smaller = cents%100
dollars = (cents-cents_for_quarters_and_smaller)/100

# quarters:
cents_for_dimes_and_smaller = cents_for_quarters_and_smaller%25
quarters = (cents_for_quarters_and_smaller-cents_for_dimes_and_smaller)/25

# dimes: 
cents_for_nickels_and_smaller = cents_for_dimes_and_smaller%10
dimes = (cents_for_dimes_and_smaller-cents_for_nickels_and_smaller)/10

# nickels (and pennies):
pennies = cents_for_dimes_and_smaller%5
nickels = (cents_for_dimes_and_smaller-pennies)/5


print("Dollars: "+str(dollars))
print("Quarters: "+str(quarters))
print("Dimes: "+str(dimes))
print("Nickels: "+str(nickels))
print("Pennies: "+str(pennies))
