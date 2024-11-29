
# Honestly I would just recommend you to skip this problem.
# But if you still want to do this then here is the solution from discussions section...

# Try any of the following:

#1
s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)

#2
' '.join(map(str.capitalize, string.split(' ')))

#3
def solve(s):
   s = s.split(" ")
   return(" ".join(i.capitalize() for i in s))

#4
print(' '.join([x.capitalize() for x in input().split(' ')]))


# Cannot be sure about the accuracy of these solutions. Just try all these. If works then good, else move on.
