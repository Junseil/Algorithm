# 리모컨

import sys
input = sys.stdin.readline

target = int(input())
m = int(input())
if m:
    bk = set(input().rstrip().split())
else:
    bk = set()

ans = abs(target - 100)
for num in range(1000001):
    for x in str(num):
        if x in bk:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)