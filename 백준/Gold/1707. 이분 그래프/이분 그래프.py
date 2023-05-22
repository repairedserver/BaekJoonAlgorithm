import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline
def dfs(node, c):
    visited[node] = c
    for i in a[node]:
        if not visited[i]:
            q = dfs(i, -c)
            if not q:
                return False
        elif visited[i] == visited[node]:
            return False
    return True

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [[] for i in range(n + 1)]
    visited = [False] * (n + 1)

    for i in range(m):
        x, y = map(int, input().split())
        a[x].append(y)
        a[y].append(x)

    for i in range(1, n + 1):
        if not visited[i]:
            ans = dfs(i, 1)
            if not ans:
                break
    print('YES' if ans else 'NO')