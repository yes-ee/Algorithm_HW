# 하노이탑 옮기기
# recursion 이용

def hanoi_tower(n, start, end):
	if n == 1:	# 남은 원판이 한 개일 경우 시작 지점에서 도착 지점으로 바로 옮김
		print(start, end)
		return
	
	# n개의 원판을 옮기기 위해 n-1개의 원판을 먼저 경유지로 옮김
	hanoi_tower(n-1, start, 6-start-end)
	# n번째 원판을 목적지로 옮김
	print(start, end)
	#경유지에 있는 n-1개의 원판을 목적지로 옮김
	hanoi_tower(n-1, 6-start-end, end)

# 실행 결과 확인
n = int(input())	# 원판 개수 입력 받음
print(2**	n-1)	# 옮긴 횟수 출력
hanoi_tower(n, 1, 3)