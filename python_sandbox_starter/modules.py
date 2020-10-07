# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
import datetime
from datetime import date
import validator
import camelcase

my_date=date.today()
print(my_date)
myEmail='rehmanaziz20yahoo.com'
if validator.validate_email(myEmail):
    print('Valid Email')
else:
    print('invalid Email')

print(camelcase.CamelCase().hump('my name is rehman aziz'))