player = []
res = []
for i in range(int(input())):
    p = input()
    player.append(p[0])

fplayer = set(player)
for i in fplayer:
    if player.count(i) >= 5:
        res.append(i)

if len(res) > 0:
    print(''.join(sorted(res)))
else:
    print("PREDAJA")