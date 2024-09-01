ERROR = "error"
n = int(input())
a = int(input())
for i in range(n):
    formula = input()
    if (len(formula) < 2):
        print(ERROR)
        break
    op, b = formula[0], int(formula[1:])
    result = 0

    if (op == "+"):
        result = a + b
    elif (op == "-"):
        result = a - b
    elif (op == "*"):
        result = a * b
    elif (op == "/"):
        if (b == 0):
            print(ERROR)
            break
        result = a // b
    else:
        print(ERROR)
        break

    print(f"{i + 1} {result}")
    a = result

