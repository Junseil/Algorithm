# 약수의 합

import sys

input = sys.stdin.readline

data = [0 for _ in range(int(1e6+1))]
res = [0 for _ in range(int(1e6+1))]

for i in range(1, int(1e6+1)):
    for j in range(i, int(1e6+1), i):
        data[j] += i
    res[i] = res[i-1] + data[i]

t = int(input())
ans = []
for _ in range(t):
    ans.append(res[int(input())])

print('\n'.join(map(str, ans))+'\n')

# python으로 제출시 시간초과... pypy3로 제출