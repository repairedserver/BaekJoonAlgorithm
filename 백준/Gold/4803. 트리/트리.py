import sys
input = sys.stdin.readline
def cycle(node):
    for adj_node in graph[node]:
        if p[node] == adj_node:
            continue
        if visited[adj_node]:
            return True
        
        p[adj_node] = node
        visited[adj_node] = 1
        if cycle(adj_node):
            return True
    return False

n, m = map(int, input().split())
case = 1

while n != 0 or m != 0:
    graph = [[] for i in range(n+1)]
    p = [-1] * (n + 1)
    visited = [0] * (n + 1)
    cnt = 0
    
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    for node in range(1, n + 1):
        if visited[node] == 0:
            p[node] = node
            visited[node] = 1
            if not cycle(node):
                cnt += 1
    
    if cnt == 0:
        print(f'Case {case}: No trees.')
    elif cnt == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {cnt} trees.')
    
    case += 1
    n, m = map(int, input().split()) 