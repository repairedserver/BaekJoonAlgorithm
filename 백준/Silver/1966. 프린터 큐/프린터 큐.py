t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    sr = [0 for i in range(n)]
    sr[m] = 1
    count = 0
    while True:
        if s[0] == max(s):
            count += 1
            if sr[0] == 1:
                print(count)
                break
            else:
                del s[0]
                del sr[0]
        else:
            s.append(s[0])
            del s[0]
            sr.append(sr[0])
            del sr[0]