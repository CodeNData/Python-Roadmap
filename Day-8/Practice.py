''' 1st Question
Write a program that takes a character as input and prints 1, 0, or -1 according to the following rules.
1, if the character is an uppercase alphabet (A - Z).
0, if the character is a lowercase alphabet (a - z).
-1, if the character is not an alphabet.
Example:
Input: The character is 'a'.
Output: 0
Explanation: The input character is lowercase, so our answer is 0.'''
def character_check(char):
    if 'A' <= char <= 'Z':
        return 1
    elif 'a' <= char <= 'z':
        return 0
    else:
        return -1
character = input()
if len(character) == 1:
    result = character_check(character)
    print(result)