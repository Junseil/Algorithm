# 1이 될 때까지

n, k = map(int, input().split())

result = 0

while n != 0:
    m = n % k
    if m == 0:
        n = n // k
        result += 1
    else:
        result += m
        n -= m
        
print(result - 1)