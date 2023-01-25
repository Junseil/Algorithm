# RGB 거리 2

import sys
import copy
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp_0 = copy.deepcopy(data)
dp_1 = copy.deepcopy(data)
dp_2 = copy.deepcopy(data)
dp_0[0][1] = dp_0[0][2] = dp_0[-1][0] = 1001
dp_1[0][0] = dp_1[0][2] = dp_1[-1][1] = 1001
dp_2[0][0] = dp_2[0][1] = dp_2[-1][2] = 1001

for i in range(1, n):
    dp_0[i][0] = min(dp_0[i-1][1], dp_0[i-1][2]) + dp_0[i][0]
    dp_0[i][1] = min(dp_0[i-1][0], dp_0[i-1][2]) + dp_0[i][1]
    dp_0[i][2] = min(dp_0[i-1][0], dp_0[i-1][1]) + dp_0[i][2]
    dp_1[i][0] = min(dp_1[i-1][1], dp_1[i-1][2]) + dp_1[i][0]
    dp_1[i][1] = min(dp_1[i-1][0], dp_1[i-1][2]) + dp_1[i][1]
    dp_1[i][2] = min(dp_1[i-1][0], dp_1[i-1][1]) + dp_1[i][2]
    dp_2[i][0] = min(dp_2[i-1][1], dp_2[i-1][2]) + dp_2[i][0]
    dp_2[i][1] = min(dp_2[i-1][0], dp_2[i-1][2]) + dp_2[i][1]
    dp_2[i][2] = min(dp_2[i-1][0], dp_2[i-1][1]) + dp_2[i][2]

print(min(min(dp_0[-1]), min(dp_1[-1]), min(dp_2[-1])))

# 얕은 복사와 깊은 복사를 공부하기 좋음