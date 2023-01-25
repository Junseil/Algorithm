# data = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# # 선택 정렬
# # 뒤쪽 살펴가며 가장 작은것을 앞쪽으로 보내는 식
# # n^2
#
# for i in range(len(data)):
#     min_index = i
#     for j in range(i+1, len(data)):
#         if data[min_index] > data[j]:
#             min_index = j
#     data[i], data[min_index] = data[min_index], data[i]
#
# print(data)


# 삽입 정렬
# 뒤에 하나를 앞쪽 어느 위치에 넣을 것인지 결정하는 방식
# n^2 이나 정렬이 어느정도 되어있을 경우 퀵정렬보다도 빠를 수 있음

# for i in range(1, len(data)):
#     for j in range(i, 0, -1):
#         if data[j] < data[j-1]:
#             data[j], data[j-1] = data[j-1], data[j]
# print(data)


# 퀵 정렬
# 피벗을 기준으로 작은 부분 큰 부분 분할을 반복
# 기본적으로 n log n 이나 삽입정렬과 반대로 정렬이 잘 되어있을 경우 n^2 까지 증가할 수도 있음

# def quick(list):
#     if len(list) <= 1:
#         return list
#     pivot = list[0]
#     tail = list[1:]
#     l = [x for x in tail if x <= pivot]
#     r = [x for x in tail if x > pivot]
#     return quick(l) + [pivot] + quick(r)
# print(quick(data))


# 계수 정렬
# 데이터가 정수로 이루어져있으면서, 최대 최소 차이가 크지않을 경우 효율적
# 동일 데이터 처리도 좋음
# n+k (k 는 최대정수값)
# 0~k 의 list를 선언후 카운트한 것을 나열

# data = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# list = [0] * (len(data)+1)
#
# for i in data:
#     list[i] += 1
#
# for i in range(len(list)):
#     if list[i] != 0:
#         for j in range(list[i]):
#             print(i, end=" ")

# # 1.
# n = int(input())
# data = [int(input()) for _ in range(n)]
# data.sort()
# data.reverse()
# print(data)

# 2.
# n = int(input())
# data = []
#
# for i in range(n):
#     input_data = input().split()
#     data.append((input_data[0], int(input_data[1])))
#
# data = sorted(data, key=lambda x: x[1])
#
# for x in data:
#     print(x[0], end=" ")

# 3.
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
#
# a.sort()
# b.sort(reverse=True)
#
# for i in range(k):
#     if a[i] < b[i]:
#         a[i], b[i] = b[i], a[i]
#     else:
#         break

