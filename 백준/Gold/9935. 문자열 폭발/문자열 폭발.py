import sys
input = sys.stdin.readline
st = []
n = input().rstrip()
boom = input().rstrip()
ex = len(boom)
for i in range(len(n)):
    st.append(n[i])
    if ''.join(st[-ex:]) == boom:
        for j in range(ex):
            st.pop()
if st:
    print(''.join(st))
else:
    print('FRULA')