k = int(input()) 
room_numbers = list(map(int, input().split())) 

unique_rooms = set(room_numbers)  # Creating set will help remove duplicate room numbers

captains_room = (sum(unique_rooms) * k - sum(room_numbers)) // (k - 1)

print(captains_room)
