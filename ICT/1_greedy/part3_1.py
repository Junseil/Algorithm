# 모험가 길드

n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
cnt = 0
bkp = 0

while data:
    for _ in range(data[-1]):
        data.pop()
        if not data:
            bkp = 1
            break
    if bkp == 1:
        break
    else:
        cnt += 1

print(cnt)