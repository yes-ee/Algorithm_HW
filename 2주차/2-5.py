class Solution(object):
  def combination(self, candidates, target):
    ret = []
    self.dfs(candidates, target, [], ret)
    return ret
  
  def dfs(self, nums, target, path, ret):
    if target < 0:	# target이 음수 -> 지금까지 구한 경로가 유효하지 않으므로 리턴
      return
    if target == 0:	# target == 0 -> 지금까지 구한 경로가 유효함
      ret.append(path)
      return
    # target은 i번째 원소 뺀 값, path에는 i번째 원소 추가한 값으로 설정 후 재귀 탐색
    for i in range(len(nums)):
      self.dfs(nums[i:], target - nums[i], path+[nums[i]], ret)
      
# 실행 결과 확인
a = Solution()
ans = a.combination([2, 3, 6, 7], 7)
print("ans :", ans)