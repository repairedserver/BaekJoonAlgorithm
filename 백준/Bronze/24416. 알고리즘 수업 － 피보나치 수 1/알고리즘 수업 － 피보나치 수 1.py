f = [0] * 50
f[1] = f[2] = 1
n = int(input())
def fibonacci(n):
    for i in range(3, n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]
print(fibonacci(n), n - 2)