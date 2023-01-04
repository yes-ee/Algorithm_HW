n, k = map(int, input().split());	# 물건 개수, 무게 입력받음

# 각 물건의 무게와 가치 입력받을 배열
thing = [[0, 0]]
# 무게와 아이템 수에 따라 최적 이익을 계산해줄 수 있는 이차원 배열 생성
p = [[0] * (k + 1) for _ in range(n+1)]

for i in range(n):
	thing.append(list(map(int, input().split())))

for i in range(1, n + 1):
	for j in range(1, k + 1):
		w = thing[i][0]
		v = thing[i][1]

		# 현재 배낭의 무게보다 넣으려고 하는 물건의 무게가 크다면
		# p의 값은 그 전 물건까지의 p와 같음
		if w > j:
			p[i][j] = p[i-1][j]
		# 현재 배낭의 무게가 넣으려고 하는 물건의 무게보다 같거나 크면
		# 그 전 물건까지의 p와
		# 현재 배낭에서 넣으려고 하는 물건 무게를 뺐을 때의 p에 현재 물건의 가치를 더한 것
		# 둘 중 큰 값을 넣음 
		else:
			p[i][j] = max(p[i-1][j], p[i-1][j-w] + v)

print(p[n][k])