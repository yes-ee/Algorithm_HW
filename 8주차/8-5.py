from heapq import heappush, heappop
import sys

input = sys.stdin.readline
inf = 100000000
def dijkstra(start):
  heap = []
  heappush(heap, [0, start])	# 초기화
  dp = [inf for i in range(n+1)]
  dp[start] = 0
  while heap:
    we, nu = heappop(heap)
    for ne, nw in s[nu]:
      wei = we + nw # 비용 계산
      if dp[ne] > wei:	# wei가 최소비용이면 dp[ne] 갱신, heap에 푸시
        dp[ne] = wei
        heappush(heap, [wei, ne])
  return dp

t = int(input())	# 테스트 케이스 개수 입력받기
for _ in range(t):	# 테스트 케이스만큼 반복
  # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 개수 입력받음
  n, d, start = map(int, input().split())
  s = [[] for i in range(n+1)]
  for i in range(d):
    # 의존성 정보 입력받음
    a, b, c = map(int, input().split())
    s[b].append([a, c])
  dp = dijkstra(start)	# 컴퓨터 감염 관계 구하는 함수
  max_dp = 0
  cnt = 0
  for i in dp:
    if i != inf:	# 감염되었다면
      # 마지막 컴퓨터까지 감염되는데 걸리는 시간 중 가장 큰 값 구함
      if max_dp < i:
        max_dp = i
      cnt += 1	# 감염된 컴퓨터 수 세기
  print(cnt, max_dp)