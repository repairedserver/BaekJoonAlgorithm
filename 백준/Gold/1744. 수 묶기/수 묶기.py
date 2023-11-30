import sys
input = sys.stdin.readline

nums = [int(input()) for i in range(int(input()))]
l1 = []
l2 = []
ans = 0

for i in nums:
    if i > 0:
        l1.append(i)
    else:
        l2.append(i)

l1.sort()
l2.sort(reverse=True)

while len(l1) > 1:
    one = l1.pop()
    two = l1.pop()
    if one == 1 or two == 1:
        ans += one+two
    else:
        ans += one*two
        
if l1:
    ans += l1.pop()
    
while len(l2) > 1:
    one = l2.pop()
    two = l2.pop()
    ans += one*two
    
if l2:
    ans += l2.pop()
    
print(ans)