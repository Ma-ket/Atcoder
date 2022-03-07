money = int(input())
cake = int(input())
donuts = int(input())

ans = (money - cake) - ((money - cake) // donuts) * donuts

print(ans)
