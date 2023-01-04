class Solution(object):
  def permuteUnique(self, nums):
    res = []	# 결과 배열
    nums.sort()	# 배열 오름차순 정렬
    self.dfs(nums, [], res)
    return res
  
  def dfs(self, nums, path, res):
    if not nums:	# nums가 없으면 빈 배열 추가 후 리턴
      res.append(path)
    for i in range(len(nums)):
      if i > 0 and nums[i] == nums[i-1]:	# 이전에 구한 배열과 같음 -> 스킵
        continue
      self.dfs(nums[:i]+nums[i+1:], path + [nums[i]], res)	# i를 제외한 원소에 대해 순열을 구하고 i를 덧붙임
      
# 실행 결과 확인
a = Solution()
ans = a.permuteUnique([1, 1, 2])
print("ans :", ans)