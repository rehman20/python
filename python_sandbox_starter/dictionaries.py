# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
car={
    'name':'Toyota Vitz',
    'max-speed': 180,
    'color':'black',
    'model-year':2016
}
# using dict constructor
name=dict(fname='Rehman',lname='Aziz',age=23,university='G.C University')

print (car)
print(name)

#accessing value
print(car['model-year'])
print(name['university'])

#adding pair
name['semester']=7
car['mileage']=10
print (name)
print (car)

#removing pair
name.pop('semester')
del car['mileage']

print(name)
print(car)

#copy a dict
newcar=car.copy()
print(newcar)

print(newcar.keys())
print(car.values())
print(name.items())