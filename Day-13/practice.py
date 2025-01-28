"""
Problem statement
Given an array ‘arr’ of size ‘n’ find the largest element in the array.
Example:
Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]
Output: 5
"""
from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    max_element = float('-inf')
    for num in arr:
        max_element = max(max_element, num)
    return max_element

if __name__ == "__main__":
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))
    stdout.write(str(largestElement(arr, n))+"\n")