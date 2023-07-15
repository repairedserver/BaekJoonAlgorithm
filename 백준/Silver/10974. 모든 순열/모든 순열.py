def dfs():
	if len(s) == n:
		print(*s)
		return
	for i in range(1,n+1):
		if not v[i]:
			s.append(i)
			v[i] = True
			dfs()
			s.pop()
			v[i] = False
n = int(input())
v = [False] * (n+1)
s = []
dfs()