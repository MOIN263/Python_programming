
# to take an input from a person we use the  inbuilt function 'input'

name = input(' enter your name :')
print(name)

# string concatenation 
print('hello ' + name )

# write a code to take an input from the user and return him his age 

# birth_year = input('enter your birth year :')
# age = 2023 - birth_year
# print(age )
# In the above code you will have an error TypeError: unsupported operand type(s) for -: 'int' and 'str beacause input gives you the 
# output in string format to rectify it you need to type cast (type conversion) it 

birth_year = int(input('enter your birth year :'))
age = 2023 - birth_year
print(age )

# write a code to  take two numbers as input and give there sum as the output 

first_num = int(input('enter the first number :'))
second_num = int(input('enter the second number :'))
sum = first_num + second_num
print('The sum of the two numbers is :',sum)



