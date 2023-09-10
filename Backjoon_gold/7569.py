# 토마토 23.09.10

import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

data = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited_1 = deque()
visited_2 = deque()

for k_1 in range(h):
    for j_1 in range(n):
        for i_1 in range(m):
            if data[k_1][j_1][i_1] == 1:
                visited_2.append((k_1, j_1, i_1))

direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
cnt = 0

while visited_2:
    tmp_k, tmp_j, tmp_i = visited_2.popleft()
    for dk, dj, di in direction:
        nk, nj, ni = tmp_k+dk, tmp_j+dj, tmp_i+di
        if nk in range(h) and nj in range(n) and ni in range(m) and data[nk][nj][ni] == 0:
            data[nk][nj][ni] = 1
            visited_1.append((nk, nj, ni))
    if not visited_2:
        if not visited_1:
            break
        else:
            visited_2 = visited_1
            visited_1 = deque()
            cnt += 1
                
res = cnt
for k_2 in range(h):
    for j_2 in range(n):
        for i_2 in range(m):
            if data[k_2][j_2][i_2] == 0:
                res = -1
                break
print(res)