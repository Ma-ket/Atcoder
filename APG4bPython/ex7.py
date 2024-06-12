a, b, c = map(int, list(input()))
a, b, c = map(bool, (a, b, c))


# ここから先は変更しないこと

assert (a is True) or (a is False)
assert (b is True) or (b is False)
assert (c is True) or (c is False)

if a:
    print("At", end="")
else:
    print("Yo", end="")

if not a and b:
    print("Bo", end="")
else:
    print("Co", end="")

if a and b and c:
    print("foo!", end="")
elif True and False:
    print("year!", end="")
elif not a or c:
    print("der", end="")

print("")
