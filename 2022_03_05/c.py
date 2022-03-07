# 未完成
class cnt:
    ans = 0
    def count(self, digit, num):
        if (digit > 0):
            if (num == 1):
                for i in range(1, 3):
                    self.count(digit - 1, i)
                    self.ans += 1
            elif (num == 9):
                for i in range(8, 10):
                    self.count(digit - 1, i)
                    self.ans += 1
            else :
                for i in range(2, 9):
                    self.count(digit - 1, i)
                    self.ans += 1
        return

digits = int(input())
c = cnt()
for i in range(1, 10):
    c.count(digits - 1, i)

limit = 998244353
print(c.ans % limit)
