# 1.
# N = int(input())
# data = list(map(str, input().split()))
# four = ["L", "R", "U", "D"]
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# x = 1
# y = 1
#
# for i in data:
#     nx = x + dx[four.index(i)]
#     ny = y + dy[four.index(i)]
#     if nx in range(1, N+1) and ny in range(1, N+1):
#         x = nx
#         y = ny
#     else:
#         continue
#
# print(x, y)
# 2.
# n = int(input())
# cnt = 0
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if "3" in list(str(i)+str(j)+str(k)):
#                 cnt += 1
# print(cnt)
# 3.
# eng, num = list(input())
# eng = ord(eng)-ord('a')+1
# num = int(num)
# cnt = 0
# steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
#
# for step in steps:
#     if eng + step[0] in range(1, 9) and num + step[1] in range(1, 9):
#         cnt += 1
# print(cnt)
# 4.
# n, m = map(int, input().split())
# x, y, four = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
# fours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# # 북 동 남 서
# cnt = 0
# bkp = 0
#
# def turn():
#     global four
#     four -= 1
#     if four == -1:
#         four = 3
#     return four
#
# while True:
#     d = fours[turn()]
#     dx = x + d[0]
#     dy = y + d[1]
#
#     if data[dx][dy] == 0:
#         data[x][y] = 2
#         data[dx][dy] = 2
#         x = dx
#         y = dy
#         cnt += 1
#     else:
#         d = fours[turn()]
#         bkp += 1
#
#     if bkp == 4:
#         dx = x - d[0]
#         dy = y - d[1]
#         if data[dx][dy] == 1:
#             break
#         else:
#             x = dx
#             y = dy
#         bkp = 0
#     print(data)
#
# # 4 4
# # 1 1 0
# # 1 1 1 1
# # 1 0 0 1
# # 1 1 0 1
# # 1 1 1 1