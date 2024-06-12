formula = input()
ops = ["+", "-", "*", "/"]

result = "error"
for op in ops:
    index = formula.find(op)
    if (index == -1):
        continue
    a = int(formula[:index])
    b = int(formula[index + 1:])
    if (op == "+"):
        result = a + b
    elif (op == "-"):
        result = a - b
    elif (op == "*"):
        result = a * b
    elif (op == "/"):
        if (b != 0):
            result = a // b
    else:
        break
print(result)
