# 연속합 2

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

if n == 1:
    print(data[0])
else:
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = data[0]
    dp[1][0] = data[0]
    for i in range(n-1):
        dp[0][i+1] = max(data[i+1], dp[0][i] + data[i+1])
    for i in range(n-1):
        dp[1][i+1] = max(dp[0][i], dp[1][i] + data[i+1])
    print(max(max(dp[0]), max(dp[1])))

# 이중 리스트에서의 max는 각 리스트의 첫번째 항만 보고 정함
# ex. print(max(max(dp))) 주의할 것