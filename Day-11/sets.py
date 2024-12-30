# it is an unordered collection, and it does not allow duplicates. Similar to the dictionary, sets are also mutable, i.e., we can add or remove the elements after the declaration, but the elements inside the sets are immutable, i.e., once inserted, we can't modify it.
my_set = {'Parth', 'Saxena', '20'}# {} are used to define sets
print(my_set)
my_set.add('Student') #adding element
print(my_set)
my_set.remove('20') #removes element
print(my_set)
print(len(my_set)) #tells length of string
for element in my_set: # for accessing elements in set
    print(element)
# Duplicate elements are not allowed in sets