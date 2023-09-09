# 적록색약 23.09.09

import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

def bfs(x, y, data, visited):
    
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    color = data[x][y]
    
    q = deque()
    q.append([x, y])
    while q:
        [tmp_x, tmp_y] = q.popleft()
        for (dx, dy) in direction:
            nx = tmp_x + dx
            ny = tmp_y + dy
            if nx in range(n) and ny in range(n):
                if not visited[nx][ny] and data[nx][ny] == color:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
            
    return visited

n = int(input())
data_1 = [list(input().rstrip()) for _ in range(n)]
visited_1 = [[0 for _ in range(n)] for _ in range(n)]
data_2 = deepcopy(data_1)
for i in range(n):
    for j in range(n):
        if data_2[i][j] == 'G':
            data_2[i][j] = 'R'
visited_2 = [[0 for _ in range(n)] for _ in range(n)]

cnt_1 = 0
cnt_2 = 0

for x in range(n):
    for y in range(n):
        if not visited_1[x][y]:
            cnt_1 += 1
            bfs(x, y, data_1, visited_1)
        if not visited_2[x][y]:
            cnt_2 += 1
            bfs(x, y, data_2, visited_2)

print(cnt_1, cnt_2)