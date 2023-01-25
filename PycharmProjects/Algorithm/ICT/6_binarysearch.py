# 정렬된 데이터가 기본

# def binary_search(list, target, start, end):
#     if list[0] > target:
#         print('aaa')
#     half = (start + end) // 2
#     if list[half] == target:
#         return half + 1
#     if list[half] < target:
#         return binary_search(list, target, half, end)
#     if list[half] > target:
#         return binary_search(list, target, start, half)
#
# data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#
# print(binary_search(data, 9, 0, 10))

# 이진탐색트리는 큰 데이터에서 주로 활용됨
# input 보다 속도면에서 유리한 sys 라이브러리 활용

# import sys
# input_data = sys.stdin.readline().rstrip()
#
# print(input_data)

# # 1.
# n = int(input())
# nlist = list(map(int, input().split()))
# m = int(input())
# mlist = list(map(int, input().split()))
#
# nset = set(nlist)
#
# for x in mlist:
#     if x in nset:
#         print('yes', end=" ")
#     else:
#         print('no', end=' ')

# # 2.
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# start = 0
# end = max(data)
#
# def binary_search(data, target, start, end):
#     mid = (end+start) // 2
#     sum = 0
#     for x in data:
#         if (x - mid) >= 0:
#             sum += x - mid
#     if sum == m:
#         return mid
#     if sum > m:
#         return binary_search(data, target, mid, end)
#     if sum < m:
#         return binary_search(data, target, start, mid)
#
# print(binary_search(data, m, start, end))
