import sys
input = sys.stdin.readline

b = []
n = int(input())

for i in range(n) :
    b.append(list(map(int, input().split())))
    
q = [[0,0]]
dx = [1,0]
dy = [0,1]
visited = [[0] * n for i in range(n)]

while q:
    x = q[0][0]
    y = q[0][1]
    del q[0]

    if b[x][y] == -1:
        print("HaruHaru")
        exit(0)
        
    j = b[x][y]
    for i in range(2):
        nx = x + dx[i]*j
        ny = y + dy[i]*j
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            q.append([nx,ny])
print("Hing")