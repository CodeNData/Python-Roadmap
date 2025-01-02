'''
() 	Parentheses (3 + 4) * 2 = 14
** Exponentiation 3 ** 2 = 9
*,/,%,// Multiplication, Division, Modulus, Floor division 4 * 3 = 12, 12 / 3 = 4, 12 % 2 = 0, 12 // 5 = 2
+,- Addition, Subtraction 4 + 3 = 7, 4 - 3 = 1
'''
# Left-to-right associativity
result = 10 - 5 - 3  # Equivalent to (10 - 5) - 3
print(result)  # Output: 2

# Right-to-left associativity
result1 = 2 ** 3 ** 2  # Equivalent to 2 ** (3 ** 2)
print(result1)  # Output: 512

# Non-associativity
result2 = 3 < 4 < 5  # Equivalent to (3 < 4) and (4 < 5)
print(result2)  # Output: True