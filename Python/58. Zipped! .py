N, X = map(int, input().split())  
student = []

for i in range(X):
    marks = list(map(float, input().split()))  
    student.append(marks)  

for i in range(N):
    total = 0  
    for j in range(X):
        total += student[j][i]  
        
    avg = total / X 
    print(f"{avg:.1f}")  

# Done without using zip (Sorry)
