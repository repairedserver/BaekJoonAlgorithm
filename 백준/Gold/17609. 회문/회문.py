def two(l, r):
    while l < r:
        if a[l] == a[r]:
            l += 1
            r -= 1
        else:
            if cnt(l + 1, r) or cnt(l, r - 1):
                return 1
            return 2
    return 0
def cnt(l, r):
    while l < r:
        if a[l] == a[r]:
            l += 1
            r -= 1
        else:
            return False
    return True
n = int(input())
for i in range(n):
    a = input()
    print(two(0, len(a)-1))