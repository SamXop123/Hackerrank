
from itertools import permutations

s, k = input().split()
k = int(k)

permut = list(permutations(s, k))

permut.sort()

for i in permut:
    print(''.join(i))
