def average(arr):
    arr = set(arr)
    
    sums = 0
    x = len(arr)
    
    for i in arr:
        sums += i 
        
    return sums/x

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
