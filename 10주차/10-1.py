N = int(input())

inputMap = [[0 for col in range(0, N)] for row in range(0, N)]	# col, row 초기화

for i in range(N):
  for j, m in enumerate(map(int, input().split())) :
    inputMap[i][j] = m

for k in range(0, N):
  for i in range(0, N) :
    for j in range(0, N):
      if inputMap[i][k] and inputMap[k][j]:
        inputMap[i][j] = 1
        
for i in range(0, N):
  for j in range(0, N):
    print(inputMap[i][j], end=' ')
  print()