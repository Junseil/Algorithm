import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
data = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)
    
for x in range(n+1):
    data[x].sort()
    
q = deque([])
q.extend(data[1])
visited = [0 for _ in range(n+1)]
visited[x] = 1

while q:
    x = q.popleft()
    if not visited[x]:
        visited[x] = 1
        visi