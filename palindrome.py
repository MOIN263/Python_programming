
# write a program to specify whether the given sequence is a palindrome or not
# palindrome is a sequence which reads the same backward as forward.
#for example MADAM

seq = input('enter any sequence :').upper()
revseq = seq[::-1]

if seq == revseq :
    print('It is a palindrome sequence ')

else :
    print('it is not a palindrome sequence ')
    
# examples for the palindrome sequences are level ,radar ,civic ,Aibohphobia etc..
