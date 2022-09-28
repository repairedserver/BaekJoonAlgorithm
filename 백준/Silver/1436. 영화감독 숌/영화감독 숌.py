n = int(input())
count = 0
s = 666
while True:
    if '666' in str(s):
        count += 1
    if count == n:
        print(s)
        break
    s += 1