n = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True)
for i in range(len(t)):
    t[i] = t[i] + 1 + i
print(max(t) + 1)