from collections import Counter

if __name__ == '__main__':
    shoes = int(input())
    shoe_sizes = list(map(int, input().split()))
    inventory = Counter(shoe_sizes)
    num_customers = int(input())
    
    earnings = 0
    
    for _ in range(num_customers):
        size, price = map(int, input().split())
        # If requested size is in inventory, then:
        if inventory[size] > 0:
            earnings += price 
            inventory[size] -= 1   #Decrease the inventory count for that size
    
    print(earnings)
