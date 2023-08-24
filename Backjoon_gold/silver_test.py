import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
min_set = 1000
min_one = 1000
for _ in range(m):
    set_price, one_price = map(int, input().split())
    min_set = min(min_set, set_price)
    min_one = min(min_one, one_price)

print(min(min_one*n, min_set*(n//6)+min_one*(n%6), min_set*(n//6+1)))