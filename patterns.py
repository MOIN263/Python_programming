# python code for the basic patterns

#left aligned

def LPatnew(a): # 'a' implies no. of rows
    for i in range(a):
        print('*'*(2*i+1))


LPatnew(5)

# center aligned

def CPatnew(b):
    for i in range(b):
        print(' '*(b-i-1)+'*'*(2*i+1))


CPatnew(5)

# Right aligned

def RPatnew(c):
    for i in range(c):
        print('  '*(c-i-1)+'*'*(2*i+1))


RPatnew(5)
