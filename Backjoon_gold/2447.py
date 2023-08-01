# 별찍기

import sys
input = sys.stdin.readline

n = int(input())
m = 3
stars = ['***', '* *', '***']
new_stars = []
cnt = 0

while n % 3 == 0:
    n = n // 3
    cnt += 1

for _ in range(cnt-1):
    for i in range(m):
        new_stars.append(stars[i] * 3)
    for j in range(m, 2*m):
        new_stars.append(stars[j-m] + " "*m + stars[j-m])
    for k in range(2*m, 3*m):
        new_stars.append(stars[k-2*m] * 3)
    m *= 3
    stars = new_stars
    new_stars = []
for i in range(len(stars)):
    print(stars[i])

# 처음으로 푼 골드문제,,,