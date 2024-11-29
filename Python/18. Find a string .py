
def count_substring(string, sub_string):
    
    count = 0
    i = 0
    
    while True:
        i = string.find(sub_string, i)
        
        # If the substring is not found it returns -1, so we can break here
        if i == -1:
            break
        
        count += 1
        i += 1  
    
    return count
          
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
