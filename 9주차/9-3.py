import sys
input = sys.stdin.readline

n, k = map(int, input().split())	# 최대 공부 시간 n, 과목 수 k
dp = [[0] * (n+1) for _ in range(k+1)]
times = []
grades = []
for _ in range(k):	# 각 과목에 대해 반복해서 입력받음
  i, t = map(int, input().split())	# 중요도 i, 필요한 공부 시간 t
  times.append(t)
  grades.append(i)
  
for class_no in range(1, k+1):
  for now_time in range(1, n+1):
    if times[class_no - 1] > now_time:
      dp[class_no][now_time] = dp[class_no - 1][now_time]
    
    else:
      # 다음 중 높은 값 취함
      # 1. 지금 시간에서 추가하는 과목의 소요 시간만큼 뺐을 때의 누적 가치 + 그 과목의 점수
      # 2. 추가 안 했을 때 점수
      dp[class_no][now_time] = max(grades[class_no-1]\
        + dp[class_no - 1][now_time-times[class_no - 1]], \
          dp[class_no - 1][now_time])
      
print(dp[k][n])