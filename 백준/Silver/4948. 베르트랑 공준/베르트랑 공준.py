def s(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True	

n = int(input())
a = [i for i in range(2, 246912)]
m = []

for i in a:					
    if s(i):	
        m.append(i)

while True:
    cnt = 0
    if n == 0 :
            break
    for i in m:
        if n < i <= 2 * n:
            cnt += 1
    n = int(input())
    print(cnt)
