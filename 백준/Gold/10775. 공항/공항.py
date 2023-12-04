import sys
input = sys.stdin.readline
sys.setrecursionlimit(9999999)

def find_plane(plane):
    if gl[plane] == plane:
        return plane
    gl[plane] = find_plane(gl[plane])
    return find_plane(gl[plane])

g = int(input())
p = int(input())
cnt = 0
gl = [i for i in range(g+1)]
pl = []

for i in range(p):
    pl.append(int(input()))

for plane in pl:
    t = find_plane(plane)
    if t == 0:
        break
    gl[t] = gl[t-1]
    cnt += 1
    
print(cnt)