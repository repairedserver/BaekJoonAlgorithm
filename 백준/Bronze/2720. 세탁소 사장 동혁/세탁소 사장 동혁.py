for i in range(int(input())):
	m = int(input())
	for j in [25, 10, 5, 1]:
		print(m // j, end=' ')
		m %= j