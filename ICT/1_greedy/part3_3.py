# 문자열 뒤집기

s = input().rstrip()
com = []

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        com.append(s[i])
if s[-1] != s[-2]:
    com.append(s[-1])

print(min(com.count('0'), com.count('1')))