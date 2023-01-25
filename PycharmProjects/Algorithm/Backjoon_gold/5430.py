# AC

import sys
import collections
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    order = input().rstrip()
    n = int(input())

    q = collections.deque()
    temp = input().rstrip()[1:-1]
    if temp:
        temp = temp.split(',')
        for x in temp:
            q.append(x)

    rot = False
    flag = 0
    for x in order:
        if x == 'R':
            if rot:
                rot = False
            else:
                rot = True
        else:
            if not q:
                flag = 1
                break
            elif rot:
                q.pop()
            else:
                q.popleft()
    if not q and flag == 1:
        print('error')
    else:
        if rot:
            q = list(q)[::-1]
        else:
            q = list(q)
        print('['+','.join(q)+']')