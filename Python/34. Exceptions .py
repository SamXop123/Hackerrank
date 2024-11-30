for _ in range(int(input())):
    try:
        a, b = map(int, input().strip().split())
        div = a // b
        print(div)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)
