import sys

input = sys.stdin.readline

s = input().rstrip()
t = int(input())
data = [[0 for _ in range(len(s))] for _ in range(ord('a'), ord('z') + 1)]

data[ord(s[0])-ord('a')][0] = 1
for i in range(1, len(s)):
    for j in range(26):
        if ord(s[i]) - ord('a') == j:
            data[j][i] = data[j][i-1] + 1
        else:
            data[j][i] = data[j][i-1]
            
for _ in range(t):
    alphabet, l, r = map(str, input().split())
    l, r = int(l), int(r)
    if l == 0:
        print(data[ord(alphabet)-ord('a')][r])
    else:
        print(data[ord(alphabet)-ord('a')][r]-data[ord(alphabet)-ord('a')][l-1])
        
        
# 면접 진행