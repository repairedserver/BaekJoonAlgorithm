n, m = input().split()
m1 = int(n.replace('6', '5')) + int(m.replace('6', '5'))
m2 = int(n.replace('5', '6')) + int(m.replace('5', '6'))
print(m1, m2)