# A List is a collection which is ordered and changeable. Allows duplicate members.
names=['rehman','sunny','bhatti','aziz']
ages=[16,18,20,23]

print(names)
print(ages)

names.insert(2,'revenger')
print('After insertion: '+str(names))

ages.append(24)
print('ages after append'+str(ages))

names.pop(2)
print('After pop: '+str(names))

ages.remove(24)
print('after remove'+str(ages))

names.sort()
print('After Sort: '+str(names))

names.reverse()
print('After Reverse'+str(names))

ages.sort(reverse=True)
print('After Reverse Sort: '+str(ages))
