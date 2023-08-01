# 곱하기 혹은 더하기

# 1이 연달아 나오는 경우 반영할 것 / 수정 예정

data = list(map(int, input().rstrip()))
result = 0

for x in data:
    if result == 0:
        result += x
    else:
        result *= x

print(result)