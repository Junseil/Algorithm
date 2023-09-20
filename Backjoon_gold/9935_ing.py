# 문자열 폭발

import sys
from collections import deque
input = sys.stdin.readline

s = deque(enumerate(input().rstrip()))
bomb = deque(input().rstrip())

q = deque([])

print(s)

idx = 0
while idx != len(s)-1:
    print(s.popleft(), end='')