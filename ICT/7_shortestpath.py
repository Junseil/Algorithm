import sys
input = sys.stdin.readline
inf = int(1e9)

n, m = map(int, input().split())
start = int(input())
visited = [False] *(n+1)
distance = [inf] * (n+1)

graph = [list(map(int, input().split())) for _ in range(m)]

print(n, m, graph)

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''