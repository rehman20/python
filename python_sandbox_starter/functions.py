# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

def sum(num1,num2):
    total=num1+num2
    return total

print('Sum is '+str(sum(34,35)))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

sqr= lambda value : value*value 
product= lambda val1,val2 : val1*val2
print('square : '+str(sqr(4)))
print('product : '+str(product(5,8)))
