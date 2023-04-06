import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for tc in range(t):
    query = input().rstrip()
    k = int(input())
    q = deque(input().rstrip()[1:-1].split(','))
    f = 0
    if k == 0:  
        q = []
    for c in query:
        if c == 'R':
            f += 1
        elif c == 'D':
            if len(q) == 0:
                print('error')
                break
            else:
                if f % 2 == 1:
                    q.pop()
                else:
                    q.popleft()           
    else:
        if f % 2 == 1:
            q.reverse()
        print('[' + ','.join(q)+']')