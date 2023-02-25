n, l = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
cnt = 1

st = s[0]
end = s[0] + l
for i in range(n):
    if st <= s[i] < end:
        continue
    else:
        st = s[i]
        end = s[i] + l
        cnt += 1
print(cnt)