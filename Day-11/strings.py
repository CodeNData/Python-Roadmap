# Single Quotes: 'Hello, World!'
# Double Quotes: "Hello, World!"
# Triple Quotes: '''Hello, World!''' or """Hello, World!"""
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print(len(a))
print(a[1:4])  #slicing method is used to access a range of characters in the String.
print(a[2:10])
print(a[2:-1])
b = "I am a learner"
print(b)
for x in b:
    print(x)  #we can use a for loop to traverse through the characters in a string.
res = a.replace("Lorem", "Code")#Replace method is used to replace from string
print(res)
#Different Concatenation methods in String
c = a + b #first method
print(c)
d = " ".join([a,b]) #second method
print("% s % s" % (a,b)) #third method
e =  "{} {}".format(a, b) #fourth method
print(e)
print(a,b) #fifth method
f =  f'{a} {b}' #sixth method
print(f)
