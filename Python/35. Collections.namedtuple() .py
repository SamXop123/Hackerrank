
n = int(input())
columns = input().split()
marks_index = columns.index("MARKS")

marks = []
for _ in range(n):
    data = input().split()
    marks.append(int(data[marks_index]))
    
average_marks = sum(marks) / n
print(f"{average_marks:.2f}")
