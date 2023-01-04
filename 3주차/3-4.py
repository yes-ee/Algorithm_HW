n, r, c = map(int, input().split())
ans = 0	# 정답 저장

while n != 0:	# n번 반복하여 사분면으로 나눔
  n -= 1
  
  # 사분면 구한 후 이동 횟수 더하기
  # 1사분면
  if r < 2 ** n and c < 2 ** n:
    ans += (2 ** n) * (2 ** n) * 0
  # 2사분면
  elif r < 2 ** n and c >= 2 ** n:
    ans += (2 ** n) * (2 ** n) * 1	# 이동 횟수 더하기
    c -= (2**n)
  # 3사분면
  elif r >= 2 ** n and c < 2 ** n:
    ans += (2 ** n) * (2 ** n) * 2	# 이동 횟수 더하기
    r -= (2**n)
  # 4사분면
  else:
    ans += (2 ** n) * (2 ** n) * 3	# 이동 횟수 더하기
    r -= (2**n)
    c -= (2**n)
    
# 실행 결과 확인
print("ans :", ans)