a, b = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l1.extend(l2)
ans = ' '.join(map(str, sorted(l1)))
print(ans)