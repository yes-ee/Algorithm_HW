# 사분면 문제
# 위에서부터 아래로 x
# 왼쪽에서 오른쪽으로 y

from multiprocessing.connection import answer_challenge


def find(n1, n2, m1, m2, idx):
	if idx == len(number):
		return n1, m1
	if number[idx] == '1':	# 1사분면
		return find(n1, (n1 + n2)//2, (m1 + m2)//2, m2, idx+1)
	elif number[idx] == '2': # 2사분면
		return find(n1, (n1+n2)//2, m1, (m1+m2)//2, idx+1)
	elif number[idx] == '3':	# 3사분면
		return find((n1+n2)//2, n2, m1, (m1+m2)//2, idx+1)
	elif number[idx] == '4': # 4사분면
		return find((n1+n2)//2, n2, (m1+m2)//2, m2, idx+1)

def check(n1, n2, m1, m2):
	global answer	# 도착한 사분면의 번호 저장
	
	if len(answer) == int(d):	# 입력 자릿수와 answer에 누적된 글자수가 일치하면 리턴
		return answer
	
	if n1 <= nx < (n1+n2)//2 and (m1+m2)//2 <= ny < m2:
		answer += '1'
		return check(n1, (n1+n2)//2, (m1+m2)//2, m2)

	elif n1 <= nx < (n1+n2)//2 and m1 <= ny < (m1+m2)//2:
		answer += '2'
		return check(n1, (n1+n2)//2, m1, (m1+m2)//2)
	
	elif (n1+n2)//2 <= nx < n2 and m1 <= ny < (m1+m2)//2:
		answer += '3'
		return check((n1+n2)//2, n2,  m1, (m1+m2)//2)
	
	elif (n1+n2)//2 <= nx < n2 and (m1+m2)//2 <= ny < m2:
		answer += '4'
		return check((n1+n2)//2, n2, (m1+m2)//2, m2)


d, number = input().split()	# 자릿수, 번호 입력받음, 입력받은 문자를 공백을 기준으로 구분해서 저장
x, y = map(int, input().split())	# 이동할 좌표 입력받기

n, m = 2**int(d), 2**int(d)	# 사분면 조각 개수 계산

dx, dy = find(0, n, 0, m, 0)	# 처음 사분면 조각 좌표
nx, ny = dx + (-1) * y, dy + x # 새로운 사분면 조각 좌표

answer = ''


if 0 <= nx < n and 0 <= ny < m:
	print(int(check(0, n, 0, m)))
else:
	print(-1)