import sys
input = sys.stdin.readline

def bt(cnt):
    if cnt == len(w):
        print("".join(ans))
        return

    for k in visited:
        if visited[k]:
            visited[k] -= 1
            ans.append(k)
            bt(cnt+1)
            visited[k] += 1
            ans.pop()

for i in range(int(input())):
    w = sorted(list(map(str, input().strip())))
    visited = {}
    ans = []
    for i in w:
        if i in visited:
            visited[i] += 1
        else:
            visited[i] = 1

    bt(0)