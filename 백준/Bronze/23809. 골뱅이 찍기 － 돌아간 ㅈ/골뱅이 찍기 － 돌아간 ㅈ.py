n = int(input())
ans = ['' for i in range(n * 5)]    
for i in range(n * 5):
    if 2 * n - 1 < i < 2 * n + n:
        ans[i] = "@" * (n * 3)
    elif i < 2 * n:
        ans[i] = f"{'@' * n}{((3-(i // n)) * n) * ' '}{'@' * (n)}"
    else:
        ans[i] = f"{'@' * n}{((i // n) * n - n ) * ' '}{'@' * (n)}"
print("\n".join(ans))
