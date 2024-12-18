'''  2nd Question
Sample Input 1 :
4 6 1
Sample Output 1 :
6
Explanation of Sample Input 1:
6 is the highest of amongst all.
Sample Input 2 :
-32 -23 -76
Sample Output 2 :
-23
Explanation of Sample Input 2:
-23 is the highest of amongst all.
Sample Input 3 :
-4 0 5
Sample Output 3 :
5
Explanation of Sample Input 2:
5 is the highest of amongst all. '''
from os import *
from sys import *
from collections import *
from math import *
def find_largest(a,b,c):
    return max(a,b,c)
numbers = input().split()
if len(numbers)==3:
    a,b,c = map(int, numbers)
    output = find_largest(a,b,c)
    print(output)