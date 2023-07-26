
# understanding the if elif and else with a single code

# syntax 
# if condition :
    # block of code 
    
# elif condition :
   # block of code 
   
# else : # else doesn't require any condition 
    

temprature = int(input('enter the temperature'))

if temprature>35 :
    print('it is a hot day ')
    
elif temprature>=20 and temprature<=30:
    print('it is moderate outside')
    
else :
    print('it is cold outside')
    
