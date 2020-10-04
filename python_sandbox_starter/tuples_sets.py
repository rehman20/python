# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
vegetables=('cauliflower','brinjle','cucumber','potato','pumpkin')
fruits=('apple',) #single value needs a trailing comma 
print (vegetables)
print(vegetables[3])
print(fruits)
#del fruits
print(fruits)
# A Set is a collection which is unordered and unindexed. No duplicate members.
prime_number_set={2,3,5,7,11,15,17,19,23,27}
print(prime_number_set)
prime_number_set.add(31)
print(prime_number_set)
prime_number_set.remove(17)
print(prime_number_set)
prime_number_set.clear()
print(prime_number_set)
# check if in set
fruits_set={'Apples','Mangoes','Bananas'}
print('Mangoes' in fruits_set)