def snum(n):
    ans = 0
    for i in n:
        if i.isdigit():
            ans += int(i)
    return ans
arr = []
for i in range(int(input())):
    a = input()
    arr.append(a)
arr.sort(key = lambda x:(len(x), snum(x), x))
for i in arr:
    print(i)