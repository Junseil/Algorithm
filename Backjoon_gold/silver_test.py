import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

a_b = [b[i] for i in range(n) if a[i] == 0]
x = c[::-1]
x.extend(a_b)

for _ in range(m):
    print(x.pop(), end=' ')