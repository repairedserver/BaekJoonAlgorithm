import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
s1 = list(map(int, input().split()))
s1.sort()

s2 = [s1[i]-s1[i-1] for i in range(1, n)]
s2.sort()

print(sum(s2[:n-k]))