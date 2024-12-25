list1 = ['My','name','is','Parth','Saxena'] #list created
print(list1)
list1.append('😎') #append function is used to add a new element to the list's end
print(list1)#it will print updated list
newList = list1.copy() #copy function is used tocopy one list to another
list1.clear()#All elements in List are removed
print(list1,newList)
list2 = ['I','am','a','Student.']
newList.extend(list2) #Extend function is used to add another list to current list
print(newList)
index = newList.index('Parth') #Index function is used to return index of specified value.
print(index)
newList.pop(5)#Pop function is used to pop an element out of the list.
print(newList)
newList.reverse()#The list is reordered reversely
print(newList)
newList.sort()#Sorts the list
print(newList)
