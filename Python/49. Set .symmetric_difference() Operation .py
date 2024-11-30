
n = int(input())
english = set(map(int, input().split(" ")))

m = int(input())
french = set(map(int, input().split(" ")))

students = english.symmetric_difference(french)

print(len(students))

