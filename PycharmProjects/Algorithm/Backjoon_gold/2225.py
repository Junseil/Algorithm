# 합분해

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
result_q = 1
result_p = 1
result = 1

for i in range(1, k):
    result_q *= n+k-i
    result_p *= i
    result = result_q // result_p

print(result % 1000000000)