# 오등큰수

import sys
from collections import deque
from collections import Counter

n = int(input())
data = list(map(int, input().split()))
data_cnt = Counter(data)
result = [-1] * n
arr = []

for i in range(n):
    while arr and arr[-1][1] < data_cnt[data[i]]:
        tmp_i = arr.pop()[0]
        result[tmp_i] = data[i]
    arr.append([i, data_cnt[data[i]]])

print(*result)