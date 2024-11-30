import re
n = int(input());

for i in range(n):
    key = input();
    try:
        re.compile(key)
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid);
