n, m = map(int, input().split())
m_p, m_pi = 1000, 1000
m_res = 100000000
for i in range(m):
    a, b = map(int, input().split())
    m_p = min(m_p, a)
    m_pi = min(m_pi, b)
cnt = n // 6 + 1
for i in range(cnt + 1):
    tmp = n
    res = 0
    tmp -= i * 6
    res += i * m_p
    if tmp > 0:
        res += tmp * m_pi
    m_res = min(m_res, res)
print(m_res)