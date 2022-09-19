a, b = map(int, input().split())
result = (str(a//b)+".")
a = (a % b) * 10

for i in range(1000):
    result += str(a // b)
    a = (a % b) * 10
    
print(result)