rate = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
t = 0
res = 0
for i in range(20) :
    s, p, g = input().split()
    p = float(p)
    if g != 'P' :
        t += p
        res += p * grade[rate.index(g)]
print('%.6f' % (res / t))