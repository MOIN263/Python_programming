
first_name = 'smuf'
last_name = 'codes'

# the can be represented by double quotes and  single qoutes and ''' ''' is for the multiline comment called as the docstring 

# string has many inbuilt methods 
# to check whether the value is in uppercase 
print(first_name.isupper())
# to convert the value to the uppercase
print(first_name.upper())
# to concatenate one variable to the other  with space 
print(' '.join([first_name,last_name]))
# gives you the index of the letter given
print(first_name.index('f'))
# to check whether the character is present in the string 
print(first_name .find('u')) # remember that it gives first index of the letter 
# for example 
name = 'rutherford'
print(name.find('r')) # 0