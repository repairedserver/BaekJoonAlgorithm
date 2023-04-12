m, n = map(int, input().split())
def find_p(n, m):
    s = [True] * (m + 1)
    s[0] = s[1] = False

    for i in range(2, int(m ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, m + 1, i):
                s[j] = False

    return [j for j in range(n, m + 1) if s[j]]

p = find_p(m, n)
for i in range(len(p)):
    print(p[i])