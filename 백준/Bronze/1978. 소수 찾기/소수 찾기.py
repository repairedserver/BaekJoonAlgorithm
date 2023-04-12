def isprime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if isprime(i):
        cnt += 1
print(cnt)