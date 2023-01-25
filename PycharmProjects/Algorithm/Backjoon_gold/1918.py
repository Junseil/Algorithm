# 후위 표기식

import sys
input = sys.stdin.readline

s = input().rstrip()
arr = []

for x in s:
    if x.isalpha():
        print(x, end='')
    elif x == '(':
        arr.append(x)
    elif x in ['*', '/']:
        while arr and (arr[-1] in ['*', '/']):
            print(arr.pop(), end='')
        arr.append(x)
    elif x in ['+', '-']:
        while arr and (arr[-1] != '('):
            print(arr.pop(), end='')
        arr.append(x)
    elif x == ')':
        while arr and (arr[-1] != '('):
            print(arr.pop(), end='')
        arr.pop()
while arr:
    print(arr.pop(), end='')