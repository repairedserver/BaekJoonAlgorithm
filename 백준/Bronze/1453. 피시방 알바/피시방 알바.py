n = int(input())
s = list(map(int, input().split()))
s1 = len(list(set(s)))
print(n - s1)