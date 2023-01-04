class Solution():
  def maxSubArray(self, nums):
    m=nums	# 복사
    for i in range(1, len(nums)):
      # m[i]를 현재 원소를 이전 원소 + 현재 원소와 비교하여 더 큰 값으로 갱신
      m[i] = max(m[i], m[i-1]+nums[i])
      
    return max(nums)	# 최대값 리턴
  
# 실행 결과 확인
a = Solution()
ans = a.maxSubArray([5, 4, -1, 7, 8])
print("ans :", ans)