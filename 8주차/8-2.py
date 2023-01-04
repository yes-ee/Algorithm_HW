import sys
import heapq
f = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, f().split())	# n, m, x 입력 받음
adjList = [[] for _ in range(n+1)]	# 인접 행렬

for i in range(m):
  a, b, c = map(int, f().split())
  adjList[a].append((b,c)) # 인접 행렬 구성
  
def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start)) # 큐 (0, start)로 초기화
  distance[start]=0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now]<dist: # 방문하지 않았던 노드만 다루기 위함
      continue
    for i in adjList[now]:
      cost = dist + i[1] # 비용 계산
      # 가장 작은 비용을 가진 노드를 찾아 distance[i[0]]값 갱신, heapq에 푸시
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  return distance

result = [[] ]
time_list =[]
for i in range(1, n+1): # 정점 수 만큼 반복
  distance = [INF]*(n+1) # 매번 distance 초기화
  result.append(dijkstra(i)) # 최단 시간 구함
for i in range(1, n+1):
  time_list.append(result[i][x] + result[x][i]) # 왕복 시간 계산
  
print(max(time_list))