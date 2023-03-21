h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))
t = 0
t += (h2 - h1) * 3600 + (m2 - m1) * 60 + s2 - s1
t %= 3600 * 24
print("%.2d:%.2d:%.2d" % (t // 3600, t % 3600 // 60, t % 60))