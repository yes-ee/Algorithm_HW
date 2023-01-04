class Solution(object):
  def sortColors(self, nums):
    def quickSort(start, end):
      if (start >= end):	# 종료조건
        return
      pivot, p = nums[end], start	# end 인덱스에 해당하는 애를 pivot으로 지정
      for i in range(start, end):
        if (nums[i]<pivot):	# 숫자가 pivot보다 작으면 swap
          nums[p], nums[i] = nums[i], nums[p]
          p+=1	# pivot보다 작은 값 개수 세기
      nums[p], nums[end] = nums[end], nums[p]	# pivot 값 중간으로 보내기
      quickSort(start, p-1)	# 새 피봇 전달, 원래 pivot 왼쪽 재귀적으로 정렬
      quickSort(p+1, end)	# 새 피봇 전달, 원래 pivot 오른쪽 재귀적으로 정렬
    quickSort(0, len(nums) - 1)
    return nums
  
# 실행 결과 확인
a = Solution()
ans = a.sortColors([2, 0, 2, 1, 1, 0])
print("ans :", ans)