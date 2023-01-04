# 배열에서 k번째 큰 원소 반환, 퀵소트 이용

class Solution(object):
	def findKthLargest(self, nums, k):
		# k번째 큰 원소를 찾기 위해 뒤에서 k번째 까지만 고려함
		for i in range(len(nums), len(nums) - k, -1):
			# tmp가 피벗 역할
			tmp = 0
			for j in range(i):	# 이미 정렬된 부분 제외하고 그 앞까지만 탐색
				if nums[j] > nums[tmp]:	# 제일 큰 값으로 tmp 갱신
					tmp = j
			nums[j], nums[tmp] = nums[tmp], nums[j]	# swap
		return nums[len(nums) - k]

# 실행 결과 확인
a = Solution()
print("ans :", int(a.findKthLargest([3, 2, 1, 5, 6, 4], 2)))
