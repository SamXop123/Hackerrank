
from itertools import product

a = map(int, input().split(" "))
b = map(int, input().split(" "))

A = list(a)
B = list(b)

prod = list(product(A, B))

for i in prod:
    print(i, end = " ")


