# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name='Rehman Aziz Bhatti'
age=23
# String Formatting
print('Normal: My name is '+name+' and my age is '+str(age))
print('using format: My name is {n} and my age is {a}'.format(n=name,a=age))
print (f'using f: My name is {name} and my age is {age}')
# String Methods

print(name.upper())
s=name.split(' ')
print(s)