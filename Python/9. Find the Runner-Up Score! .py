if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
 
    arr = list(arr)
 
    # remove duplicates by creating set and sort the arr in descending order
    unique_arr = list(set(arr))
    unique_arr.sort(reverse=True)

    # the runner-up score is the second element in the sorted list of unique arr
    runner_up_score = unique_arr[1]
    
    print(runner_up_score)
