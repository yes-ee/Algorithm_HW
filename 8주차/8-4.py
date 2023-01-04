from sys import stdin
from heapq import heappush, heappop

input = stdin.readline
INF = 98765432100

n, m, k = map(int, input().split())

adj_list = [[] for _ in range(n)]	# 인접 리스트
for _ in range(m):	# 간선의 수만큼 반복, 정점과 간선의 가중치 저장하여 인접 리스트 구성
  a, b, c = map(int, input().split())	# a, b는 정점, c는 가중치
  adj_list[a-1].append((b-1, c))
  adj_list[b-1].append((a-1, c))
  
def solv():
  visited = [[INF] *(k+1) for _ in range(n)]	# 비용 저장할 배열
  pq = [(0, 0, 0)]	# heap 초기화
  visited[0][0] = 0
  while pq:
    total, cnt, now = heappop(pq)
    if total > visited[now][cnt]:	# 방문했던 노드는 continue
      continue
    if now == n-1:	# 모두 방문했으면 print하고 머춤
      print(total)
      return
    for nxt, cost in adj_list[now]:	# 인접 리스트의 원소만큼 반복
      nxt_total = total + cost	# 비용 계산
      # nxt_total이 최소 비용이면 visited[nxt][cnt] 갱신, heap에 푸시
      if visited[nxt][cnt] > nxt_total:
        visited[nxt][cnt] = nxt_total
        heappush(pq, (nxt_total, cnt, nxt))
      
      if cnt+1<= k and visited[nxt][cnt+1] > total:	# 도로를 포장하는 경우
        visited[nxt][cnt+1] = total
        heappush(pq, (total, cnt+1, nxt))

solv()