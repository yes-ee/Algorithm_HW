T = int(input())

for t in range(T):
	N = int(input())	# 동전의 가짓수
	coin = list(map(int, input().split()))	# 동전 각각의 가치
	m = int(input())	# 목표 금액
	
	dp = [0] * (m + 1)

	for n in range(N):
		if (coin[n] > m):	# 동전의 금액이 목표 금액보다 크면 패스
			continue
		
		dp[coin[n]] += 1	# 동전 금액이 v일 때 v를 가지고 목표 금액 v를 만드는 방법 1가지

		for i in range(coin[n] + 1, m + 1):
			# a라는 금액을 만드는 방법이 x개 있으면
			# a를 만드는 방법 x개에 금액 b짜리 동전을 더해서 a+b 금액을 만들 수 있음
			# (x가지 방법 추가)
			dp[i] += dp[i - coin[n]]

	print(dp[m])
