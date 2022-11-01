n = input()
c = len(n) - 1
ans = 0
for i in range(c):
    ans += 9*(10 ** i)*(i + 1)
    i += 1
ans += ((int(n) - (10 ** c)) + 1) * (c + 1)

print(ans)