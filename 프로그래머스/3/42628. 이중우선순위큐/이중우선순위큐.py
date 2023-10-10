import heapq as hq
def solution(operations):
    h = []
    for i in operations:
        a, b = i.split()
        if a == 'I':
            hq.heappush(h, int(b))
        elif h:
            if b == "1":
                h = hq.nlargest(len(h), h)[1:]
                hq.heapify(h)
            elif b == '-1':
                hq.heappop(h)
    if h:
        m = h[0]
        return [hq.nlargest(1, h)[0], m]
    else:
        return [0, 0]