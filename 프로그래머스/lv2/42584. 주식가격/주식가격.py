def solution(prices):
    ans = [0] * len(prices)
    st = []
    for i, j in enumerate(prices):
        while st and j < prices[st[-1]]:
            k = st.pop()
            ans[k] = i-k
        st.append(i)
        
    for i in range(len(st)):
        a = st.pop()
        ans[a] = len(prices)-a-1
    return ans