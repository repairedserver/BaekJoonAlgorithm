def valid(r):
    for i in range(r):
        if row[i] == row[r]:
            return False
        if abs(r-i) == abs(row[r]-row[i]):
            return False
    return True

def queen(r):
    global ans
    if r == n:
        ans += 1
        return
    for i in range(n):
        row[r] = i
        if valid(r):
            queen(r + 1)
            
n = int(input())
ans = 0
row = [0]*n   
queen(0)
print(ans)