n = int(input())
i = list(map(int, input().split()))
j = list(map(int, input().split()))
 
i.sort()
j.sort(reverse=True)
 
sum = 0
for a in range(n):
  sum += (i[a] * j[a])
print(sum)