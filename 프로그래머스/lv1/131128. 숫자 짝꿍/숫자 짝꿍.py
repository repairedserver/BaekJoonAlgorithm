from collections import defaultdict
def solution(X, Y):
    x = defaultdict(int)
    y = defaultdict(int)
    for i in X:
        x[i] += 1
    for i in Y:
        y[i] += 1
    inter = set(x.keys()) & set(y.keys())
    s = ""
    for i in list(inter):
        cnt = min(x[i], y[i])
        s += i * cnt
    ans = sorted(s, reverse = True)
    if not ans:
        return "-1"
    if ans[0] == "0":
        return "0"
    return "".join(ans)