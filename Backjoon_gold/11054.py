# 가장 긴 바이토닉 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
data_1 = list(map(int, input().split()))
data_2 = data_1[::-1]
dp_1 = [1] * n
dp_2 = [1] * n

for i in range(n):
    for j in range(i):
        if data_1[i] > data_1[j]:
            dp_1[i] = max(dp_1[i], dp_1[j] + 1)
        if data_2[i] > data_2[j]:
            dp_2[i] = max(dp_2[i], dp_2[j] + 1)

dp = []
dp_2 = dp_2[::-1]
for i in range(n):
    dp.append(dp_1[i] + dp_2[i])

print(max(dp)-1)