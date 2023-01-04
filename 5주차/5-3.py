class Solution(object):
  def climbStairs(self, n):
    dp = [1, 1] + [0]*n	# 처음 2칸은 1로 초기화, n만큼 공간 할당
    for i in range(2, n+1):
      # i번째 칸을 오르는 방법의 가짓수 = i-1번째 칸을 오르는 방법의 가짓수 + i-2번째 칸을 오르는 방법의 가짓수
      dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
  
# 실행 결과 확인
a = Solution()
ans = a.climbStairs(3)
print("ans :", ans)