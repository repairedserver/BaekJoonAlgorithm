def solution(priorities, location):
    p = priorities.index(max(priorities))
    ans = 0
    while True:
        a = max(priorities)
        if priorities[p] == a:
            priorities[p] = 0
            ans += 1
            if p == location:
                break
        p += 1
        if p >= len(priorities):
            p = 0
    return ans