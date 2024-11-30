
M = int(input())
a = map(int, input().split(" "))
N = int(input())
b = map(int, input().split(" "))

a = set(a)
b = set(b)

unionSet = a.union(b)
interSet = a.intersection(b)

result = unionSet - interSet

lists = []
for i in result:
    lists.append(i)
    lists.sort()

for z in lists:
    print(z)
