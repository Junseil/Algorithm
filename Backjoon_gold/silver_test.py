import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def dis(data_three):
    tmp = {'E':0, 'I':0, 'S':0, 'N':0, 'T':0, 'F':0, 'J':0, 'P':0}
    for i in range(3):
        for j in range(4):
            tmp[data_three[i][j]] += 1
    return tmp['E']*tmp['I']+tmp['S']*tmp['N']+tmp['T']*tmp['F']+tmp['J']*tmp['P']

for _ in range(t):
    n = int(input())
    data = list(map(str, input().split()))
    