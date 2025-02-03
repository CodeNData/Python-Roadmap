import sys
def check(a, b):
    print("a = ", a)
    print("b = ", b)
    if id(a) == id(b):
        print("a and b refer to the same object")
    else:
        print("a and b dont refer to the same object")
a = [1, 2, 3]
print("Count of references = ", sys.getrefcount(a))
print()
b = a
check(a, b)
print("Count of references = ", sys.getrefcount(a))
print()
b = 5
check(a, b)
print("Count of references = ", sys.getrefcount(a))
print()
