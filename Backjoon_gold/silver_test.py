import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
data = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)

for i in range(n+1):
    data[i].sort(reverse=True)
    
def dfs(x):
    stack = [x]
    visited = [0 for _ in range(n+1)]
    cnt = 1
    while stack:
        tmp_x = stack.pop()

        if visited[tmp_x] == 0:
            visited[tmp_x] = cnt
            stack.extend(data[tmp_x])
    return visited        
        
    
for i in range(n):
    print(dfs(i))