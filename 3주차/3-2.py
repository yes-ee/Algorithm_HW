import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def check(i, j, d):
  global paper
  pick = table[i][j]	# 현재 종이의 값 저장
  for it in range(i, i+d):
    for jt in range(j, j+d):
      if table[it][jt] != pick:	# 종이에서 다른 값이 발견되면
        newd = d // 3	# 9조각으로 나눈 뒤 다시 check 호출하여 값 확인
        for mi in range(0, 3):
          for mj in range(0, 3):
            check(i + mi * newd, j + mj * newd, newd)
        return
  paper[pick] += 1
  
# 실행 결과 확인
n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
paper = [0, 0, 0]	# 0, 1, -1의 갯수 저장
check(0, 0, n)
print("ans :", end = " ")
for i in range(-1, 2):
  print(paper[i], end = " ")