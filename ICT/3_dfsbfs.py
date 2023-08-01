from collections import deque

# data = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
# visited = [False] * 9

# def dfs(data, v, visited):
#     visited[v] = True
#     print(v, end=" ")
#     for i in data[v]:
#         if visited[i] is not True:
#             visited[i] = True
#             dfs(data, i, visited)
# dfs(data, 1, visited)

# def bfs(data, start, visited):
#     q = deque([start])
#     while q:
#         v = q.popleft()
#         visited[v] = True
#         print(v, end=" ")
#         for i in data[v]:
#             if visited[i] != True:
#                 q.append(i)
#                 visited[i] = True
# bfs(data, 1, visited)

'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''

# n, m = map(int, input().split())
# data = [list(map(int, input())) for _ in range(n)]
#
# cnt = 0
#
# def dfs(x, y):
#     if x in range(0, n) and y in range(0, m):
#         if data[x][y] == 0:
#             data[x][y] = 1
#             dfs(x-1, y)
#             dfs(x+1, y)
#             dfs(x, y-1)
#             dfs(x, y+1)
#             return True
#         else:
#             return False
#     else:
#         return False
#
# for i in range(0, n):
#     for j in range(0, m):
#         if dfs(i, j) is True:
#             cnt += 1
#
# print(cnt)


'''
5 6
101010
111111
000001
111111
111111
'''

# n, m = map(int, input().split())
# data = [list(map(int, input())) for _ in range(n)]
# visited = [[False] * m for _ in range(n)]
# dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
# def search(x, y):
#     for d in dxy:
#         nx = x + d[0]
#         ny = y + d[1]
#         if nx in range(n) and ny in range(m) and visited[nx][ny] == False:
#             visited[nx][ny] = True
#             data[nx][ny] = data[x][y]+1
#
# for i in range(n):
#     for j in range(m):
#         search(i, j)
# print(data[n-1][m-1])