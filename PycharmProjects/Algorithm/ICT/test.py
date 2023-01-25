import sys
import copy
input = sys.stdin.readline

n = int(input())
tmp = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

def queen(i, j, k):
    for _ in range(n):
        tmp[i][_] = k
        tmp[_][j] = k
        if i+j-_ in range(n):
            tmp[_][i+j-_] = k
        if j-i+_ in range(n):
            tmp[_][j-i+_] = k
    return tmp

cnt = 0
def back():
    print(1)
    global result
    global tmp
    global cnt
    global visited
    if cnt == n:
        result += 1
        return
    else:
        for i in range(n):
            for j in range(n):
                if tmp[i][j] == 0 and visited[i][j] == 0:
                    visited[i][j] = 1
                    cnt += 1
                    pre = copy.deepcopy(tmp)
                    queen(i, j, 1)
                    back()
                    cnt -= 1
                    tmp = pre
result = 0
back()
print(result)