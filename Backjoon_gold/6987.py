# 월드컵

import sys

input = sys.stdin.readline

def f(res):
    mid = 0
    for i in range(6):
        s = sum(res[3*i:3*(i+1)])
        mid += ((-1)**(i))*res[3*i+1]
        if s != 5:
            return 0
    if mid != 0:
        return 0
    return 1

sol = []
for _ in range(4):
    data = list(map(int, input().split()))
    sol.append(f(data))

print(*sol)