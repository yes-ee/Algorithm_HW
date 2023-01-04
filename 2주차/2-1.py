class Solution(object):
  def permute(self, nums):
    if len(nums) == 1:	# 원소가 한 가지인 경우
      return [nums]
    result = []	# 결과 배열
    for i in range(len(nums)):	# 원소의 개수만큼 반복
      others = nums[:i] + nums[i+1:]	# i번째 원소 제외하고 배열 생성
      other_permutations = self.permute(others)	# i번째 원소 제외하고 순열 생성
      for permutation in other_permutations:	# i번째 원소를 생성한 순열 앞에 붙임
        result.append([nums[i]] + permutation)
    return result

# 실행 결과 확인
a = Solution()
ans = a.permute([1, 2, 3])
print("ans :" , ans)