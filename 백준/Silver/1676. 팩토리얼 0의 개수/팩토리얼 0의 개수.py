n = int(input())
def five(n):
    count = 0
    while n != 0:
        n //= 5
        count += n
    return count
    
print(five(n))