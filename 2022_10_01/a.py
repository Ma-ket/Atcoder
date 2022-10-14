# 通りませんでしたw

n = int(input())

bit = [0]

for _ in range(8):
    binary = n % 2
    bit.insert(0, binary)
    n = n // 2

def operation(bits):
    num = 0
    for i in range(4):
        num += bits[3 - i] * (2 ** i)

    print(bits, num, "==")

    if (num == 10):
        return "A"
    elif (num == 11):
        return "B"
    elif (num == 12):
        return "C"
    elif (num == 13):
        return "D"
    elif (num == 14):
        return "E"
    elif (num == 15):
        return "F"

    return str(num)

print(operation(bit[0:4]), end="")
print(operation(bit[4:8]))
