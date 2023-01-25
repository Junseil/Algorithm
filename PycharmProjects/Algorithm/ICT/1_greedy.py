# money = int(input())
# coins = [500, 100, 50, 10]
# n = 0
#
# for coin in coins:
#     n += money // coin
#     money %= coin
#
# print(n)

# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort(reverse=1)
# result = data[0] * m - (m // k) * (data[0]-data[1])
# print(result)

# n, m = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
# result = 0
#
# for i in range(n):
#     a = data[i][:]
#     a.sort()
#     if result < a[0]:
#         result = a[0]
#     else:
#         continue
#
# print(result)

# n, k = map(int, input().split())
# count = 0
#
# while n != 1:
#     if n % k == 0:
#         n = n / k
#         count += 1
#     else:
#         n -= 1
#         count += 1
#
# print(count)
