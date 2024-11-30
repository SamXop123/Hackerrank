
n = int(input())
english = set(map(int, input().split(" ")))

m = int(input())
french = set(map(int, input().split(" ")))

students = english.intersection(french)

print(len(students))

