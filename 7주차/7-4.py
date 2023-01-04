n, m = map(int, input().split())	# 책의 수, 한번에 들 수 있는 책의 수 입력
book = list(map(int, input().split()))	# 책의 좌표

# 음수, 양수 나누기
left = []
right = []
for item in book:
  if item < 0:
    left.append(item)
  elif item > 0:
    right.append(item)

distance = []
left.sort()
for i in range(len(left)//m):	# 한번에 m권만 옮길 수 있음
  distance.append(abs(left[m*i]))	# 책 가지고 가는 거리 추가, 절대값이 가장 큰 수만큼 움직이면 됨
if len(left) % m > 0:
  distance.append(abs(left[(len(left)//m)*m]))	# 나머지 있으면 책 가지고 가는 거리 추가

right.sort(reverse=True)	# 절대값이 작은 거부터 m개씩 묶는 게 유리함 -> reverse
for i in range(len(right)//m):	# 한번에 m권만 옮길 수 있음
  distance.append(abs(right[m*i]))	# 책 가지고 가는 거리 추가, 절대값이 가장 큰 수만큼 움직이면 됨
if len(right) % m > 0:
  distance.append(abs(right[(len(right)//m)*m]))	# 나머지 있으면 책 가지고 가는 거리 추가

distance.sort()
res = distance.pop()
res += 2*sum(distance)	# 왕복거리 계산
print(res)