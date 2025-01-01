my_dict = {
    "Name" : "Parth",
    "Surname" : "Saxena",
    "Age" : "20"
}
x = my_dict.get('Name')#will return the value for the specified key.
print(x)

y = my_dict.keys()#returns a view object that displays a list of all the keys in the dictionary in order of insertion.
print(y)

z = my_dict.copy()#will create a copy of the original dictionary
print(z)

a = my_dict.items()# will return all the items.
print(a)
print(my_dict.values())#returns a view object that contains the dictionary's values as a list.

my_dict.pop('Age')#will remove the specified item from the dictionary.
print(my_dict)

my_dict.update({"City": "Ghaziabad"})#will insert the key: value pairs in the dictionary.
print(my_dict)

print(my_dict.clear())# remove all the elements from the dictionary.