
# Indentation 
# indentation is a white space in the text 
# python uses indentation to create blocks of codes 
# it is one of the common bugs when trying to write a python code 

# single line comments are usually denoted by '#' .it helps in better readabilty of code 

# And multiline code is denoted by """ A -------- """

'''hello world 
how are you guys 
this is an example of multiline comment '''

# INTRODUCTION TO THE DATATYPES IN PYTHON

# 1. NUMBERS
'''number includes integers ,float numbers and complex numbers
Integer: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
Float: Decimal number Example ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
Complex Example 1 + j, 2 + 4j  '''

# 'type' is an inbuilt function to knuw the type of the datatype

a=2
print(a)
print(type(a))

b = 23.32
print(b)
print(type(b))

c = 2 + 4j 
print(c)
print(type(c))

'''String
A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.'''
'''for example "smufcodes" '''

name = 'smufcodes'
age = 23
py = "python"


'''print(name)
print(age)
print(py)'''

print(name,age,py)
print(type(name))  #str

'''Booleans
A boolean data type is either a True or False value. T and F should be always uppercase'''

print(23<25)  # True

a=2 
b=8
print(b/a==5) #False 

'''list 
it is a ordered collection of different kinds of datatypes 
it is denoted by the square brackets'''

a = [1,2,3,4]  # 'a' (list) contain single type of datatype which is numbers
print(type(a))

# lets try giving it different datatypes

qwa = [123,'smuf',True,False,23.4]
# qwa is a list which have different types of datatypes in it 

# Dictionary

'''one of the most important datatypre in python programming language.A
 dictionary object is an unordered collection of data in a key value pair format. 
 And it is denoted with "{}" 
 
 dict = { key : value } => perfect representation of the dictionary'''

dictionary = {'name':'smufcodes','age':20,'favproglang':'Python'}

print(dictionary)
print(type(dictionary))

# Tuple 
'''
A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable .tuple is generally denoted by normal brackets " () "'''

tup = (1,2,3,4,5)
tup2 = ('name','smuf','codes',23,43,12,3.33)

print(tup)
print(type(tup))

print(tup2)
print(type(tup2))

'''Set
A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.set doesnot allow duplicates 
it is also denoted by " {} " but the diffrence between dict and set is that set is not in key value where as a dictionary is '''

set1 = {1,1,23,53,45,44,1} # i have knowingly included 1 three times to show set doesnot allow duplicates 

print(set1)
# most probable output {1,44,45,53,23}
print(type(set1))
