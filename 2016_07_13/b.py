n, l = map(int, input().split())
string = []

for i in range(n):
    string.append(input())

print("".join(sorted(string)))
