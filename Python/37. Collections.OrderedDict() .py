from collections import OrderedDict

items = OrderedDict()

n = int(input())

for _ in range(n):
    *item_name, net_price = input().split()
    item_name = ' '.join(item_name) 
    net_price = int(net_price)
    
    if item_name in items:
        items[item_name] += net_price  
    else:
        items[item_name] = net_price
        
for item_name, net_price in items.items():
    print(item_name, net_price)
