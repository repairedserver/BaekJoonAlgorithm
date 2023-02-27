t = int(input())
ans = abs(100 - t)
m = int(input())
if m:
    b = set(input().split())
else:
    b = set()
for i in range(1000001): 
    for j in str(i):
        if j in b:
            break
    else:
        ans = min(ans, len(str(i)) + abs(i - t))
print(ans)