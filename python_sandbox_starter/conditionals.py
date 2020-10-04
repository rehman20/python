# If/ Else conditions are used to decide to do something based on something being true or false
x=900
y=100

if x>y:
    print(f'{x} is greater than {y}')
else:
    print (f'{y} is greater than {x}')    

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
a=9
b=a

if a == b:
    print(f'a={a} is equal to b={b}')


# Logical operators (and, or, not) - Used to combine conditional statements
if a > 10 and a==b:
    print('a is equal to b')
elif a<10 or b<a:
    print('a is less than 10 or b is less than a')
else:
    print('whatever!!!')



# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

print(a not in [2,3,4,7])
    


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
mydict = dict(name='Rehman')
print(type(mydict) is dict)