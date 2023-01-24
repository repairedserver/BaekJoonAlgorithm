import sys
input = sys.stdin.read
n = input()
a = 'abcdefghijklmnopqrstuvwxyz'
ans = []
for i in a:
    ans.append(n.count(i))
m = max(ans)
for i in range(len(ans)):
    if m == ans[i]:
        print(chr(i+97), end='')