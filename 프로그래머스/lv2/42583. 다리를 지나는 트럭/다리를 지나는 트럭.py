from collections import deque
def solution(bridge_length, weight, truck_weights):
    ans = 0
    b = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    c = 0
    while len(truck_weights)!=0:
        ans += 1
        c -= b.popleft()
        if c + truck_weights[0] <= weight:
            c += truck_weights[0]
            b.append(truck_weights.popleft())
        else: 
            b.append(0)
    ans += bridge_length
    return ans