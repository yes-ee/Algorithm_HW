# 피보나치 수열
# 1) recursion으로 구현
# 2) 반복으로 구현

class Solution:
	def fib_recur(self, n):	# class 안에 선언하는 함수에는 self 전달
		if n == 0:	# 첫 번째 항 값 0
			return 0
		if n == 1:	# 두 번째 항 값 1
			return 1
		return self.fib_recur(n-1) + self.fib_recur(n-2)	# 이전 두 개 항의 값을 각각 재귀적으로 구함
	def fib_repeat(self, n):	# 반복적 방법
		a, b = 0, 1	# 첫 번째 항, 두 번째 항
		for i in range(n):	# n번 반복
			a, b = b, a+b	# 이전 두 개 항을 더한 값을 새로운 항의 값으로 취함
		return a

n = int(input())
a = Solution()
print("recur :", a.fib_recur(n))
print("repeat :" , a.fib_repeat(n))