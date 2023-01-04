class Solution(object):
  def longestPalindrome(self, s):
    res = ""	# 결과 배열
    for i in range(len(s)):	# 문자열 길이만큼 반복
      # 문자열 길이가 홀수인 경우
      tmp = self.helper(s, i, i)
      if len(tmp) > len(res):	# 지금까지 구한 문자열의 길이보다 길면 갱신
        res = tmp
      # 문자열 길이가 짝수인 경우
      tmp = self.helper(s, i, i+1)
      if len(tmp) > len(res):	# 지금까지 구한 문자열의 길이보다 길면 갱신
        res = tmp
    return res
  
  # 가장 긴 palindrome을 구하는 함수
  def helper(self, s, l, r):
    # 배열의 범위를 넘어가지 않고, l과 r이 가리키는 값이 같으면 인덱스 한 칸씩 넓힘
    while l >= 0 and r < len(s) and s[l] == s[r]:
      l -= 1
      r += 1
    return s[l+1:r]
  
# 실행 결과 확인
a = Solution()
ans = a.longestPalindrome("cbbd")
print("ans :", ans)