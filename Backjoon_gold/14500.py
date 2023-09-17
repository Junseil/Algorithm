# 테트로미노

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split)) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_val = 0
visited = set()
