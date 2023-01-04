a = 1000 - int(input())	# 거스름돈 구함
b = [500, 100, 50, 10, 5, 1]	# 돈 단위 배열
count = 0;
for i in b:
  count += a // i	# 잔돈 개수 누적
  a %= i	# 남은 거스름돈 계산
print(count)	# 잔돈의 개수 출력