#Break Statement in for loop
list1 = ['I','am', 'Parth', 'Saxena', 'I', 'am','a','student']
i = 0
for i in range (len(list1)):
    print(list1[i])
    if (list1[i]== 'Parth'):
        print('\n Break \n')
        break #Break Statement Skips upcoming iterations
        print('\n after break statement \n')
    i += 1
print('\n It is an example of break statement in for loop \n')
#continue statement
for word in list1:
    if word == 'Saxena':  # Skip 'Saxena'
        continue #Skips current iteration
    print(word)  # Print each word only once, except 'Saxena'

#Pass Statement: Pass statement is a null statement. But the difference between pass and comment is that comment is ignored by the interpreter whereas pass is not ignored.
li =['a', 'b', 'c', 'd']

for i in li:
	if(i =='a'):
		pass
	else:
		print(i)
