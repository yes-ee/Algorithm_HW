# 파스칼 삼각형

class Solution:
	def generate(self, numRows):
		pascal = [[1] * (i + 1) for i in range(numRows)]	# 파스칼 삼각형 기본 구조 생성, 다 1로 채움
		for i in range(numRows):	# i번째 줄
			for j in range(1, i):	# range(1, 0)인 경우는 패스
				pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]	# 아랫 칸의 값 = 위 두 칸의 합
		return pascal

# 실행 결과 확인
n = int(input())
a = Solution();
print("ans :", a.generate(n))