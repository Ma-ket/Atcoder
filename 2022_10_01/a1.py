# 通りましたw

n = int(input())

bit = []

for _ in range(2):
    binary = n % 16
    bit.insert(0, binary)
    n = n // 16

def operation(bits):
    num = bits
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

print(operation(bit[0]), end="")
print(operation(bit[1]))
