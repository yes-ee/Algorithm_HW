def merge_sort(array):
  if len(array) <= 1:	# 배열의 길이가 1보다 작으면 리턴
    return array
  mid = len(array) // 2	# 중간 값
  # left와 right로 나누어 다시 merge sort 실행
  left = merge_sort(array[:mid])
  right = merge_sort(array[mid:])
  i, j = 0, 0
  arr = []	# 결과 저장
  # left 리스트와 right 리스트의 원소를 한 개씩 비교하여 작은 원소를 arr에 추가
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      arr.append(left[i])
      i += 1
    else:
      arr.append(right[j])
      j += 1
  # left 혹은 right 배열에 남은 요소가 있다면 arr에 넣어주기
  arr += left[i:]
  arr += right[j:]
  return arr

# 실행 결과 확인
n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))
arr = merge_sort(arr)
print("ans :", end = " ")
for i in arr:
  print(i, end=" ")