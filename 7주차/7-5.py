import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
# 방문 여부 배열 초기화
visited = [False]*(V+1)
Elist = [[] for _ in range(V+1)]	# 간선 리스트
heap = [[0, 1]]
# 간선 정보 저장
for _ in range(E):
	s, e, w = map(int, input().split())
	Elist[s].append([w, e])
	Elist[e].append([w, s])

answer = 0
cnt = 0

while heap:
	if cnt == V:	# 정점 개수만큼 다 방문했으면
		break
	w, s = heapq.heappop(heap)
	if not visited[s]:
		visited[s] = True
		answer += w	# 가중치 누적
		cnt += 1
		for i in Elist[s]:
			heapq.heappush(heap, i)

print(answer)