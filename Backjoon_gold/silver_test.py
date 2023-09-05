import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
direction = [(+1, 0), (-1, 0), (0, -1), (0, +1)]

for i in range(n):
    for j in range(m):
        if data[i][j] == 'I':
            start_x = i
            start_y = j
            break

cnt = 0
q = deque()
q.append((start_x, start_y))

while q:
    (x, y) = q.popleft()
    print(x, y)
    if not visited[x][y]:
        visited[x][y] = 1
        for (dx, dy) in direction:
            nx = x+dx
            ny = y+dy
            if nx in range(n) and ny in range(m):
                if data[nx][ny] == 'O':
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif data[nx][ny] == 'P':
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    cnt += 1

print(cnt)