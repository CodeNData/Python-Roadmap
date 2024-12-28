import array as arr
a = arr.array('i', [1, 2, 3])
print(a[0])#accessing element of array
a.append(5)#adding element to array
print(a)
a.remove(3)#removes element from array
print(a)
a.reverse()#reverses the elements of array
print(a)
a.pop(2)#pops element at particular index
print(a)
b = a.index(2)# tells position of the element
print(b)
a.append(5)
print(a)
c = a.count(5)#used to count given item in array
print(c)
a.extend([6,7,8,9])#this method is used to add an array of values to the end of a given or existing array
print(a)