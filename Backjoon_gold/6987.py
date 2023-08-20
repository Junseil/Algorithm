# 월드컵_시뮬레이션 x 백트래킹으로 다시 시도

import sys

input = sys.stdin.readline

global cnt
def f(data):
    if cnt == 15:
        return 1
    

sol = []
for _ in range(4):
    data = list(map(int, input().split()))
    sol.append(f(data))

print(*sol)