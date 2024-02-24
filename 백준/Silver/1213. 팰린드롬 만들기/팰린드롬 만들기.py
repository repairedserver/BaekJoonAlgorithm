from collections import Counter
import sys
input = sys.stdin.readline

word = input().rstrip()
word_c = Counter(word)
ans = ''
m = ''
cnt = 0
for k, v in list(word_c.items()):
    if v % 2 == 1:
        cnt += 1
        m = k
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            sys.exit()

for k, v in sorted(word_c.items()):
    ans += k*(v//2)

print(ans+m+ans[::-1])