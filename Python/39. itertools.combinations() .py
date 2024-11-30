import itertools

def combination(s, k):
    # We are sorting to put the string into lexicographic order
    s = ''.join(sorted(s))
    
    result = []
    
    for size in range(1, k + 1):
        for combo in itertools.combinations(s, size):
            result.append(''.join(combo))
    
    for combination in result:
        print(combination)

input_line = input().strip()
s, k = input_line.split()
k = int(k)

combination(s, k)
