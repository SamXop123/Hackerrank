def is_subset(a, b):
    set_a = set(a)
    set_b = set(b)
    
    return set_a.issubset(set_b)

if __name__ == '__main__':
    T = int(input())
    
    for _ in range(T):
        nA = int(input())
        A = list(map(int, input().split()))
        
        nB = int(input())
        B = list(map(int, input().split()))
        
        if is_subset(A, B):
            print("True")
        else:
            print("False")
