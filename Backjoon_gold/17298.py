# 오큰수

import sys
from collections import deque

n = int(input())
data = list(map(int, input().split()))
result = [-1] * n
arr = []

for i in range(n):
    while arr and arr[-1][1] < data[i]:
        tmp_i = arr.pop()[0]
        result[tmp_i] = data[i]
    arr.append([i, data[i]])

print(*result)