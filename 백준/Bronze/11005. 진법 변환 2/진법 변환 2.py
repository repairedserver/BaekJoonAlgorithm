from sys import stdin
jin = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, stdin.readline().split())
ans =''

while n != 0:
    ans += str(jin[n%b])
    n = n // b
    
print(ans[::-1])