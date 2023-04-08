n = int(input())
a = input()
cnt = 0
for i in a:
    if i in ['a', 'e', 'i', 'o', 'u']:
        cnt += 1
print(cnt)