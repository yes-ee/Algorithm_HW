import sys
from collections import deque

input = sys.stdin.readline
cnt = 0
while (1):
  # 동굴 크기 n
  n = int(input().rstrip())
  cnt+=1
  if n == 0:
    break
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  # 도둑 루피 배열
  cave = [[0 for _ in range(n)] for _ in range(n)]
  # 각 위치에 따라 가장 적게 잃을 수 있는 루피 값을 비교해 넣을 배열
  theif = [[99999 for _ in range(n)] for _ in range(n)]
  # 방문 여부 체크할 배열
  visited = [[False for _ in range(n)] for _ in range(n)]
  # 한 줄씩 입력받으면서 공백 제거하여 cave 구성
  for i in range(n):
    row = (input().rstrip()).replace(' ', '')
    for j, char in enumerate(row):
      if char != " ":
        cave[i][j] = int(char)
        
  # dequeue 이용해 모든 위치 방문 체크를 해가면서 비교
  q = deque()
  q.append((0, 0))
  theif[0][0] = cave[0][0]
  while q:
    i, j = q.popleft()
    visited[0][0] = True
    
    for k in range(4):
      nx = i + dx[k]
      ny = j + dy[k]
      if 0 <= nx < n and 0 <= ny < n:
        # 현재 위치의 상하좌우 중 방문 안 한 곳이 있으면 이동
        if not visited[nx][ny]:
          # 만약 theif[이동할 좌표] 값이
          # theif[현재 좌표] 값 + 도둑루피[이동할 좌표]의 합보다 크면
          # 더 작은 값으로 갱신, 그리고 q에 이동할 좌표를 넣음
          if theif[nx][ny] > theif[i][j] + cave[nx][ny]:
            theif[nx][ny] = theif[i][j] + cave[nx][ny]
            q.append((nx, ny))
            
  print("Problem {0}: {1}".format(cnt, theif[n-1][n-1]))