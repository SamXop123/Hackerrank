
n = int(input()) 
elements = set(map(int, input().split()))  
num_commands = int(input())  

for _ in range(num_commands):
    command = input().split()
    action = command[0]
    
    if action == 'pop':
        if elements: 
            elements.pop()
    elif action == 'remove':
        value = int(command[1])
        if value in elements:
            elements.remove(value)
    elif action == 'discard':
        value = int(command[1])
        elements.discard(value)

print(sum(elements))
