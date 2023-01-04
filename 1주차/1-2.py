class Solution(object):
  def searchInsert(self, nums, target):
    l, r = 0, len(nums) - 1	# 왼쪽 인덱스, 오른쪽 인덱스 초기화
    while l <= r:
      mid = (l + r) // 2	# 중간 인덱스 계산
      if nums[mid] == target:	# target을 찾으면 리턴
        return mid
      elif nums[mid] < target:	# target보다 중간 값이 작으면
        l = mid + 1
      else:	# target보다 중간 값이 크면
        r = mid - 1
    return l

# 실행 결과 확인
a = Solution()
ans = a.searchInsert([1, 3, 5, 6], 5)
print("ans : ", ans)