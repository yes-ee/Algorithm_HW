class Solution(object):
  def generateParenthesis(self, n):
    # (n+2) * (n+1) 행렬 생성
    dp = [[[] * (n+1) for j in range(n+1)] for i in range(n+2)]
    
    dp[1][1].append("(")	# 여는 괄호로 초기화하고 시작
    
    for i in range(1, len(dp)): # 행 만큼 반복
      for j in range(1, len(dp[0])):	# 열 만큼 반복
        # 잘못된 괄호 조합을 ㅁ나든 경우 패스
        if i-1 > j:
          continue
        # 이전 행의 원소를 보고 최근 cell에 닫는 괄호 추가
        for k in dp[i-1][j]:
          dp[i][j].append(k + ")")
        # 이전 열의 원소를 보고 최근 cell에 여는 괄호를 추가
        for k in dp[i][j-1]:
          dp[i][j].append(k+"(")
    
    return dp[len(dp) - 1][len(dp[0]) - 1]
  
a = Solution()
ans = a.generateParenthesis(3)
print("ans :", ans)