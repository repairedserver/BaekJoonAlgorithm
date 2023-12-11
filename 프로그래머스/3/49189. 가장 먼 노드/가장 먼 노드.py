from collections import deque
def solution(n, edge):
    ans = 0
    q = deque([1])
    graph = [[] for i in range(n+1)]
    dis = [-1] * (n+1)
    dis[1] = 0
    
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])  
    
    while q:
        a = q.popleft()
        for i in graph[a]:
            if dis[i] == -1:
                q.append(i)
                dis[i] = dis[a] + 1
                
    for i in dis:
        if i == max(dis):
            ans += 1
    return ans