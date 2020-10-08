# Python has functions for creating, reading, updating, and deleting files.
myFile=open('name.txt','w')

print('Name of File: '+myFile.name)
print('Mode of Operation: '+myFile.mode)

myFile.write('My name is Rehman Aziz.\n')
myFile.write('I am 23 years old.')

myFile.close()

myFile=open('name.txt','a')

myFile.write('\nI like python and djando\n')

myFile.close()

myFile=open('name.txt','r')

strContent=myFile.read(100)

print(strContent)

myFile.close()