# Given a number N, print sum of all even numbers from 1 to N.
N = int(input())
sum = 0
for i in range(2, N+1, 2):
        sum += i
print(sum)
