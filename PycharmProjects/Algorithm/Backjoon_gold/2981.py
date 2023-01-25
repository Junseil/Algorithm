# 검문

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
data = [arr[i+1] - arr[i] for i in range(n-1)]
data.sort()

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

m = data[0]
for i in range(1, n-1):
    m = gcd(m, data[i])

result = []
for i in range(1, int((m**(1/2) + 1))):
    if m % i == 0:
        result.append(i)
        result.append(m // i)
print(*sorted(list(set(result)))[1:])