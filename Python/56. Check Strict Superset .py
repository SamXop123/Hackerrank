
A = set(map(int, input().split()))

strict = True 

for _ in range(int(input())):
    other = set(map(int, input().split()))
    
    if not (A.issuperset(other) and len(A) > len(other)):
        strict = False  
        break  

print(strict)
