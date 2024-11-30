
from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)
s = ''.join(sorted(s))

cwr = list(combinations_with_replacement(s,k))
cwr.sort()

for i in cwr:
    result = "".join(i)
    print(result)
