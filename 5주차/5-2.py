class Solution:
  def longestValidParantheses(self, s):
    # dp[i]에 s[i]로 끝나는 가장 긴 부분 문자열의 길이를 기록
    
    # 업데이트 규칙:
    # 만약 s[i]가 "("이면 dp[i]=0
    # 만약 연이은 문자열이 "()"이면 dp[i] = dp[i-2] + 2
    # 만약 s[i]가 ")"이고 s[i-1]도 ")"이면 s[i-dp[i-1]-1]에서 가능한 짝을 찾고 앞에 덧붙임
    
    n = len(s)
    dp = [0 for i in range(n)]	# 입력 문자열 길이만큼 0으로 초기화
    
    if n < 2:	# 길이가 0이나 1이면 짝이 없으므로 0 리턴
      return 0
    
    # 처음 문자열이 "()"인 경우 초기화
    dp[1] = 2 if s[:2]=="()" else 0
    
    for i in range(2, n):
      if s[i] == ")":
        if s[i-1] == "(":	# 짝이 맞는 경우 유효한 부분 문자열의 길이에 2 더함
          dp[i] = dp[i-2] + 2
        else:	# ")"인 경우
          if i - dp[i-1]-1 >= 0:
            if s[i - dp[i-1]-1] == "(":	# 짝 찾으면 이전에 누적된 유효한 문자열 길이에 2와 이번에 찾은 문자열의 길이를 더함
              dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
    return max(dp)
  
# 실행 결과 확인
a = Solution()
ans = a.longestValidParantheses(")()())")
print("ans :", ans)