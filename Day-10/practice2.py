'''Problem statement:
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E), and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W into their corresponding Celsius values and print the table.
Note:
Print the floor of the Celsius values if they are non-negative else print its ceil value. '''
from os import *
from sys import *
from collections import *
from math import *
def fahrenheit_to_celsius(f):
    c = (f-32)*5/9
    return ceil(c) if c < 0 else floor(c)
s = int(input())
e = int(input())
w = int(input())
for fahrenheit in range(s , e+1, w):
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}\t{celsius}")