import sys

input = sys.stdin.readline
n, m = map(int, input().split())

data = []

for _ in range(m):
    data.append(sorted(list(map(int, input().split()))))

data.sort(key=lambda x: (x[0], x[1]))

print(data)