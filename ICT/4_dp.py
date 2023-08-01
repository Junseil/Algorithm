# 간단한 피보나치 수열조차 단순 귀납적 (재귀함수) 으로 사용시 100번째항도 못구함
# 이전에 계산된 것이 다시 계산 안되도록 조절해주는 list 추가
# o(n) 의 시간복잡도를 가짐

# 탑다운 방식의 피보나치 / 보텀업이 재귀함수 오류는 없음 - 단순한 반복문으로 구현 (빈 list 활용)
# d = [0] * 100
#
# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     if d[n] != 0:
#         return d[n]
#     d[n] = fibo(n-2) + fibo(n-1)
#     return d[n]
#
# print(fibo(99))

# 1.
# n = int(input())
#
# d = [0] * 30000
#
# for i in range(2, n+1):
#     d[i] = d[i-1] + 1
#     if i % 5 == 0:
#         d[i] = min(d[i], d[int(i/5)] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[int(i/3)] + 1)
#     if i % 2 == 0:
#         d[i] = min(d[i], d[int(i/2)] + 1)
#
# print(d[n])

# 2.
# n = int(input())
# d = list(map(int, input().split()))
#
# for i in range(n):
#     if i >= 2 and d[0:i-1] != []:
#         d[i] = max(d[0:i-1]) + d[i]
#
# print(d)

# 3.
# n = int(input())
#
# d = [0] * 1001
# d[1] = 1
# d[2] = 3
#
# for i in range(3,n+1):
#     d[i] = 2 * d[i-2] + d[i-1]
#
# print(d[i])

# 4.
# n, m = map(int, input().split())
# coins = [int(input()) for _ in range(n)]
#
# d = [10001] * 10001
#
# for i in range(m+1):
#     if i in coins:
#         d[i] = 1
#
# for i in range(m+1):
#     for j in coins:
#         if d[i-j] != 10001:
#             d[i] = min(d[i], d[i-j]+1)
#
# print(d[m])