# 가장 긴 증가하는 부분 수열 4

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = [1 for _ in range(n)]
ref_index = [0 for _ in range(n)]

for i in range(n):
    x = 0
    for j in range(i):
        if data[i] > data[j]:
            if dp[i] != max(dp[i], dp[j]+1):
                dp[i] = dp[j]+1
                x = j
    ref_index[i] = x
max_dp = max(dp)

print(max_dp)

result = []
series = dp.index(max_dp)
for _ in range(max_dp):
    result.append(data[series])
    series = ref_index[series]
print(*result[::-1])