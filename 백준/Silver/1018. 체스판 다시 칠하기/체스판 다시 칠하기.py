n, m = map(int, input().split())
org = []
count = []

for i in range(n):
    org.append(input())

for a in range(n-7):
    for b in range(m-7):
        in1 = 0
        in2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if org[i][j] != 'W':
                        in1 += 1
                    if org[i][j] != 'B':
                        in2 += 1
                else:
                    if org[i][j] != 'B':
                        in1 += 1
                    if org[i][j] != 'W':
                        in2 += 1
        count.append(min(in1, in2))

print(min(count))