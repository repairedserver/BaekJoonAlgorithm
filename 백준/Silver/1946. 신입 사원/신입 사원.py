import sys
input = sys.stdin.readline
for i in range(int(input())):
    r = [list(map(int, input().split())) for j in range(int(input()))]
    r_sort = sorted(r)
    ans = 1
    t = 0
    for j in range(1, len(r_sort)):
        if r_sort[j][1] < r_sort[t][1]:
            t = j
            ans += 1
    print(ans)