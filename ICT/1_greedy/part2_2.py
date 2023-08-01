# 큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

print(data[-1] * m - (data[-1]-data[-2]) * (m // k))