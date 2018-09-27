"""
Problem

Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.
"""

# odd numbers -> impares, el resto debe ser 1

a = 100
b = 200

odds = [i for i in range (a,b) if i % 2 == 1]

print (sum(odds))


