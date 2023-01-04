class Solution(object):
  def mySqrt(self, x):
    l, r = 0, x	# 제일 왼쪽 값, 오른쪽 값 초기화
    while l <= r:
      mid = (l + r) // 2	# 중간 값 계산
      if mid * mid <= x and x < (mid + 1) * (mid + 1):	# 제곱근 찾으면 리턴
        return mid
      elif x < mid * mid:	# 제곱근 값보다 mid가 큰 경우
        r = mid - 1	# 범위를 왼쪽 반으로 줄임
      else:	# 제곱근 값보다 mid가 작은 경우
        l = mid + 1	# 범위를 오른쪽 반으로 줄임
        
# 실행 결과 확인
a = Solution()
ans = a.mySqrt(8)
print("sqrt : " , ans)