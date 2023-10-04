def solution(people, limit):
    ans = 0
    cnt = 0
    st, end = 0, len(people)-1
    people.sort()
    while st <= end:
        cnt += 1
        if people[st]+people[end] <= limit:
            st += 1
            end -= 1
        else:
            end -= 1
    return cnt