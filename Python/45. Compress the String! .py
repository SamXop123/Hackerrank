
numbers = input()
char_count = 1
letters = ""

for i in range(1, len(numbers)):
    
    if numbers[i] == numbers[i - 1]: 
        char_count += 1  
    else:
        letters += f"({char_count}, {numbers[i - 1]}) "
        char_count = 1 
      
letters += f"({char_count}, {numbers[-1]}) "

print(letters)
