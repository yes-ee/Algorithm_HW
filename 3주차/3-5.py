import sys
sys.setrecursionlimit(10**6)

def paint_star(len):
  div3 = len // 3
  if len == 3:	# 3*3일 때 모양 정의
    g[1] = ['*', ' ', '*']
    g[0][:3] = g[2][:3] = ['*']*3
    return
  
  paint_star(div3)	# 9구간으로 나눈 후 재귀 호출
  
  for i in range(0, len, div3):	# 행, 열 반복
    for j in range(0, len, div3):
      if i != div3 or j != div3:	# 가운데 칸이 아니면
        for k in range(div3):
          g[i+k][j:j+div3] = g[k][:div3]	# div3 크기만큼 붙여넣기
          
n = int(sys.stdin.readline().strip())
g = [[' ' for _ in range(n)] for _ in range(n)]	# 공백으로 이루어진 n * n 배열 생성

paint_star(n)

# 실행 결과 확인
for i in range(n):
  for j in range(n):
    print(g[i][j], end='')
  print()