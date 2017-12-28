# data types in python
"""
print(type(2))
print(type(2.2))
print(type(20000000000000))
print(type('c'))
print(type('Hello world'))
print(type(True))
"""

# to clear the screen
'''
import os
clear = lambda: os.system('cls')
clear # for python file
clear() # for terminal
'''

# assign values to variables
'''
a = b = c = 1.5
print(a)
print(b)
print(c)

one, two, three = 1, 'two',3.0
print(one)
print(two)
print(three)

num = 1
str = 'string'
num = str

# prints keyword that are available in python
import keyword
keyword.kwlist
'''

# basic arithmetic
'''
print(2.0+5)
print(40.6*20.2)
print(2/2)
print(2**5 ) #power
print(2**10)
'''

# binary number manipulation
'''
print(5<<3)
print(8<<3)
print(256&255)
print(256|255)
print(60^13)
'''

# complex arithmetic
'''
a = 25 * 15 + 33
b = 2.0
print(a)
print(b)
print(a / b)
a = 16 - 2.0
b = 4 + 1
c = a / b
e = 8 + c
f = e / 2
g = 5.0 * f
h = g % 4

print(h)
print((5.0*(8 + (16 - 2.0) / (4 + 1)) / 2) % 4)
'''

# division
'''
print(23 // 5)  # for rounding the output
print(25.0 % 4)
'''


'''
operator precedence
()
**
*
/
%
+
-
'''

# strings
'''
string = 'i am a string in python'
print(string[7])
print(len(string))
print(string[-5])
print(string[7:13])
print(string[7:])

string2 = 'py' + 'thon'
print(string2)
string3 = (2 * 'py' + 'thon')
print(string3)

word = 'Ford'
word = 'L' + word[1:]  # replace a character
print(word)

# format method
print('Today i had {0} cups of {1}'.format(3, 'coffee'))
print('prices: ({x}, {y}, {z})'.format(x=2.0, y=1.5, z=5))
print('The {vehicle} had {0} crashes in {1} months'.format(5, 6, vehicle='car'))
print('{:>30}'.format("test")) #align the text

print('{:x}'.format(21)) # for hex
print('{:o}'.format(21)) # for octal
print('{:b}'.format(21)) # for binary

'''


# conditional statements
'''
str = 'hi'

if str == 'hello' or str == 'hi':
    print('Hi, how are you?')
else:
    print("Hey")

if 5 < 7:
    print("smaller")
    if 5 > 6:
        print('greater')
    elif 5 < 6:
        print('smaller')
else:
    print("greater")


me = 'Damn' if str == 'hi' or str == 'hello' else 'Hey'

print(me)
'''


# loops
string = 'string traversal'
'''
for i in range(1, 10, 2):
    print(i)


for i in range(len(string)):
    print(string[i])


for char in string:
    print(char)

for i in range(3):
    for j in range(2):
        print(j)


for i in range(1, 11):
    print('{:<3}'.format(i), end='')

    for j in range(1, 11):
        print('{:>4}'.format(i * j), end='')

    if i == 1:
        print('\n{:#^44}'.format(""),end='')

    print("")

i = 10

while i != 100:
    print(i)
    i = i + 1

    # infinite loop
while True:
    print('infy')
    break

for i in range(1,11):
    if i==5:
        continue
    print(i)
    '''

# functions
'''
def fxn():
    return 'Hello world',2

i = fxn()
print(i)


# passing arguments
def fxn(a, b):
    c = a + b
    return c

i = fxn(5, 4)

print(i)

# nested functions
def outer(a):
    def inner(b):
        return b * a
    a = inner(a)
    return a

print(outer(4))

# returning function
def f(a):
    def g(b):
        return a*b
    return g

print(f(5)(2))

# labda functions
a = lambda x,y: x*y

print(a(2,3))

# recursive


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(6))
'''

# exception handling
'''
try:
    n = int(input("Enter an integer: "))

except ValueError:
    print('That is not an integer')


try:
    sum = 0
    file = open('number.txt', 'r')
    for number in file:
        sum = sum + 1.0 / int(number)
    print(sum)
except ZeroDivisionError:
    print("Number in file = 0")
except IOError:
    print("File not found")

finally:
    print("I will print no matter what")

# throwing exceptions

a = 1

def RaiseEx(a):
    if type(a) != type('a'):
        raise ValueError('this is not a string')


try:
    RaiseEx(a)
except ValueError as e:
    print(e)


def testCase(a,b):
    assert a<b, "a is greater than b"

try:
    testCase(2,1)
except AssertionError as e:
    print(e)

'''

