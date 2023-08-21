import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
idx_data = deque([i for i in range(1, n+1)])
val_data = deque(map(int, input().split()))

while val_data:
    print(idx_data.pop())
    x = val_data.pop()
    for i in range(x):
        