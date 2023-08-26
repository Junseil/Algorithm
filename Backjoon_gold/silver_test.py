import sys
from collections import deque

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

a = 0
b = 0
def sol(data, size):
    global a, b
    
    for i in range(size):
        for j in range(size):
            data[i][j]