import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(sorted(a)[k-1])