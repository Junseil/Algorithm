# 거스름돈

money = int(input())
coins = [500, 100, 50, 10]
n = 0

for coin in coins:
    n += money // coin
    money %= coin

print(n)