
# Check the python version you are using

''' just run this command python3 --version
 in the terminal like ubuntu you will know the version'''

'''check the data types of the following data:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
Your name
Your family name
Your country'''

'''10 is an integer.
9.8 is a float.
3.14 is a float.
4 - 4j is a complex number.
['Asabeneh', 'Python', 'Finland'] is a list.
"Your name" is a string.
"Your family name" is a string.
"Your country" is a string.'''


# Find an Euclidian distance between (2, 3) and (10, 8)
import math
x1, y1 = 2, 3
x2, y2 = 10, 8
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(distance)