A = int(input())

elements_A = set(map(int, input().split(" ")))

N = int(input())

for _ in range(N):
    command = input().split(" ")
    
    task = command[0]

    if task == "intersection_update":
        new_Set = set(map(int, input().split(" ")))
        elements_A.intersection_update(new_Set)
    elif task == "update":
        new_Set = set(map(int, input().split(" ")))
        elements_A.update(new_Set)
    elif task == "symmetric_difference_update":
        new_Set = set(map(int, input().split(" ")))
        elements_A.symmetric_difference_update(new_Set)
    elif task == "difference_update":
        new_Set = set(map(int, input().split(" ")))
        elements_A.difference_update(new_Set)
        
sum_elements_A = sum(elements_A)
print(sum_elements_A)
