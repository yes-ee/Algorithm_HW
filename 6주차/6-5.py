# 외판원 순환 문제

n = int(input())

INF = int(1e9)
dp = [[INF] *(1<<n) for i in range(n)]

def dfs(x, visited):
	# 모든 도시를 방문했다면
	if visited == (1 << n) - 1:
		if arr[x][0]:	# 출발점으로 가는 경로가 있을 때
			return arr[x][0]
		else:
			return INF

	# 이미 최소 비용이 계산되어 있다면
	if dp[x][visited] != INF:
		return dp[x][visited]
	
	# 최소 비용이 계산되어 있지 않을 때
	# 모든 도시를 돌면서 계산할 것
	for i in range(n):
		if arr[x][i] == 0:
			continue
		if visited & (1<<i):	# 이미 방문한 도시라면
			continue

		dp[x][visited] = min(dp[x][visited], arr[x][i] + dfs(i, visited | (1 << i)))

	return dp[x][visited]


arr = []	# 초기 입력 비용
for i in range(n):
	arr.append(list(map(int, input().split())))

print(dfs(0, 1))	# 순회에 필요한 최소 비용 출력