import math

#Ryan Chen
# 1005983884
# LEC0101


#This code prints a number of statements
print('Hello World of ESC180 Lab 0.') #replaced a ending parenthases with a single quotation mark

a = 15 #removed @ symbol
b = 144
c = a + b

print('a = {}, b = {}'.format(a, b))
print('Also b = {1} and a = {0}'.format(a, b)) #removed percent symbol from end line
print('a + b = {answer}'.format(answer=c))

some_number, other_number = 1.80, 1.03
print('Division gives:')
print('{division:.3f}'.format(division=some_number/other_number))
print('But int version is just {floor_division}'.format(floor_division=int(some_number/other_number)))

print('Pi is a very long number, so let\'s print it programmatically! Just set num_decimals to whatever you want')
p = math.pi
num_decimals = 3
print('Here is a long version of pi: {}'.format(p))
print('But pi to {n} decimal places is {pi:.{n}f}'.format(n=num_decimals, pi=p))

x = 2 #removed comment before line
print(x)
