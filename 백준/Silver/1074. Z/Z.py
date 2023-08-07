import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())
ans = 0

while n != 0:
	n -= 1
	if r < 2**n and c < 2**n:
		continue

	elif r < 2**n and c >= 2**n: 
		ans += (2**n)**2
		c -= 2**n
        
	elif r >= 2**n and c < 2**n: 
		ans += (2**n)**2 * 2
		r -= 2**n
            
	else:
		ans += ( 2**n )**2 * 3
		r -= 2**n
		c -= 2**n
    
print(ans)