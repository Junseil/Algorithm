# 문자열 폭발

import sys
input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()

stack = []

for i in range(len(s)):
    stack.append(s[i])
    print(stack)