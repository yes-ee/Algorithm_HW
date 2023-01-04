class Solution(object):
  def majorityElement(self, nums):
    ans = []
    if not nums:
      return
    target = len(nums) / 3	# 몇 번 이상 나타나야 하는지 기준
    self.find(nums, target, ans)
    return ans
  
  def find(self, nums, target, ans):
    if not nums:
      return
    low1, low2 = self.partition(nums)
    if low2 - low1 - 1 > target:	# 기준보다 많이 나타나면 정답 배열에 추가
      ans.append(nums[low1+1])
    self.find(nums[:low1+1], target, ans)	# low1 왼편 비고
    self.find(nums[low2:], target, ans)	# low2 오른편 비교
    
  def partition(self, nums):
    high = len(nums) - 1
    key = nums[high]	# num의 가장 마지막 원소를 pivot으로
    j, l1, l2 = 0, -1, high + 1
    while j < l2:
      if nums[j] < key:	# pivot보다 작으면 l1 오른쪽으로 한 칸
        l1 += 1
        nums[j], nums[l1] = nums[l1], nums[j]
        j += 1
      elif nums[j] > key:	# pivot보다 크면 l2 왼쪽으로 한 칸
        l2 -= 1
        nums[j], nums[l2] = nums[l2], nums[j]
      else:
        j += 1
    return l1, l2
  
# 실행 결과 확인
a = Solution()
ans = a.majorityElement([3, 2, 3])
print("ans :", ans)