from os import *
from sys import *
from collections import *
from math import *
principal = float(input().strip())
rate = float(input().strip())
time = float(input().strip())
simple_interest = (principal * rate * time) / 100

floor_simple_interest = floor(simple_interest)

print(floor_simple_interest)