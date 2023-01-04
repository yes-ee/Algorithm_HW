# 퀵소트로 배열 정렬

def quick_sort(array):
	if len(array) <= 1:	# 배열의 원소가 하나인 경우 종료
		return array
	
	pivot = array[0]	# 배열의 첫 번째 원소를 피벗으로 설정
	tail = array[1:]	# 피벗 제외 나머지 리스트

	left_array = [x for x in tail if x <= pivot]	# 피벗보다 작은 원소들 왼쪽 부분
	right_array = [x for x in tail if x > pivot]	# 피벗보다 큰 원소들 오른쪽 부분

	# 정렬된 배열들 모두 합쳐서 반환
	return quick_sort(left_array) + [pivot] + quick_sort(right_array)

numbers = list(map(int, input().split()))	# 띄어쓰기 기준으로 배열 나눠서 int형으로 저장
sorted = quick_sort(numbers)	# 정렬된 배열을 sorted에 저장
for i in sorted:
	print(i, end=' ')	# 배열 출력