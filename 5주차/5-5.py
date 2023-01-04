# 플로이드 워샬 알고리즘 - 모든 노드 간의 최단 경로 계산 프로그램

# 무한 값 설정 - 10의 9제곱 = 10억으로 설정
INF = int(1e9)

num_node = int(input("노드 개수를 입력: "))
num_edge = int(input("간선 개수를 입력: "))

# 최단 거리를 위한 2차원 리스트 생성, 값 INF로 초기화
min_dist = [[INF] * (num_node + 1) for i in range(num_node + 1)]

# 자기 자신으로 가는 거리는 0으로 초기화
for a in range(1, num_node + 1):
	for b in range(1, num_node + 1):
		if a == b:
			min_dist[a][b] = 0

# 간선의 정보를 입력 받아 최단 거리 테이블 초기화
for i in range(num_edge):
	a, b, cost = map(int, input("[간선 정보 입력] 출발 노드, 도착 노드, 비용 순서로 입력: ").split())
	min_dist[a][b] = cost

# 플로이드 워셜 알고리즘 수행
for k in range(1, num_node + 1):
	for a in range(1, num_node + 1):
		for b in range(1, num_node + 1):
			min_dist[a][b] = min(min_dist[a][b], min_dist[a][k] + min_dist[k][b])

# 결과 출력
for a in range(1, num_node + 1):
	for b in range(1, num_node+1):
		# 값이 INF인 경우 INF 출력
		if min_dist[a][b] == INF:
			print("INF", end = ' ')
		else:
			print(min_dist[a][b], end = ' ')
	print()	# 개행