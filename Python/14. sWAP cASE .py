
def swap_case(s):
    
    lists = list(s)

    for i in range(0, len(lists)):
        if lists[i].islower():
            lists[i] = lists[i].upper()
        elif lists[i].isupper():
            lists[i] = lists[i].lower()
    new_string = ''.join(lists)
    return new_string      

# OR SIMPLY USE str.swapcase() function
# def swap_case(s):
#     return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
