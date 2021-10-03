
# Python Program to calculate GCD or HCF of numbers.
from math import gcd
from functools import reduce

ar = list(map(int, input("Enter the numbers :").split()))

x = reduce(gcd,ar)

print (x)
