my_dict = {
    "Name" : "Parth",
    "Surname" : "Saxena",
    "Age" : "20"
} #we use {} for creating dictionary else we can Use dict() keyword for creating dictionary
print(my_dict)
print(my_dict["Name"])#for accessing an element
my_dict.update({"Course" : "CSE(AI&ML)"})# to add new key : value pair
print(my_dict)
del(my_dict["Course"]) #this is used to remove an item
print(my_dict)
print(len(my_dict)) #used to find number of keys
new = {'a': 'A',
       'b' : 'B',
       'c' : {'d':'D','e':'E'}
       } #nested dictionary
print(new)