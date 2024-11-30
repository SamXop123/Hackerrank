from itertools import product

K, M = map(int, input().split())
lists = []

for _ in range(K):
    data = list(map(int, input().split()))
    lst = data[1:]  
    lists.append(lst)

def find_max_sum(K, M, lists):
    
    combinations = product(*lists)  
    # Used itertools.product above, which made this problem a hell lot easier
    
    max_sum = 0  
    
    for y in combinations:
        sum_of_squares = sum(x**2 for x in y) % M
        max_sum = max(max_sum, sum_of_squares)
    
    return max_sum

result = find_max_sum(K, M, lists)
print(result)
