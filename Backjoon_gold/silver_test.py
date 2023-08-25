import sys
from collections import deque
input = sys.stdin.readline

basket = set()

m = int(input())

for _ in range(m):
    s = input().rstrip().split()
    if s[0] == 'add' and int(s[1]) not in basket:
        basket.add(int(s[1]))
    elif s[0] == 'remove' and int(s[1]) in basket:
        basket.remove(int(s[1]))
    elif s[0] == 'check':
        if int(s[1]) in basket:
            print(1)
        else:
            print(0)
    elif s[0] == 'toggle':
        if int(s[1]) in basket:
            basket.remove(int(s[1]))
        else:
            basket.add(int(s[1]))
    elif s[0] == 'all':
        basket = set([i for i in range(1, 21)])
    elif s[0] == 'empty':
        basket = set()