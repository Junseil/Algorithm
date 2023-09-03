import sys
from collections import deque

sys.setrecursionlimit(3000)
input = sys.stdin.readline
n, m = map(int, input().split())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

for tmp_i in range(n):
    for tmp_j in range(m):
        if data[tmp_i][tmp_j] == 2:
            i = tmp_i
            j = tmp_j
            
res = [[0 for _ in range(m)] for _ in range(n)]
diff = [(0, 1), (1, 0), (-1, 0), (0, -1)]

data[i][j] = -1
bfs_q = deque()
bfs_q.append([i, j])

while bfs_q:
    [x, y] = bfs_q.popleft()
    
    for dx, dy in diff:
        nx, ny = x+dx, y+dy
        
        if nx in range(n) and ny in range(m) and data[nx][ny] == 1:
            bfs_q.append([nx, ny])
            data[nx][ny] = -1
            res[nx][ny] = res[x][y] + 1
            
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            res[i][j] = -1
        print(res[i][j], end=' ')
    print()