import sys
input = sys.stdin.readline

def buy_triple(idx):
  global cost
  k = min(arr[idx:idx+3])	# 첫 번째, 두 번째, 세 번째 지점에서 동시에 살 수 있는 개수 구함
  arr[idx] -= k	# 구매한 개수 빼기
  arr[idx+1] -= k	# 구매한 개수 빼기
  arr[idx+2] -= k	# 구매한 개수 빼기
  cost += 7 * k	# 비용 누적

def buy_double(idx):
  global cost
  k = min(arr[idx:idx+2])	# 첫 번째, 두 번째 지점에서 동시에 살 수 있는 개수 구함
  arr[idx] -= k	# 구매한 개수 빼기
  arr[idx+1] -= k	# 구매한 개수 빼기
  cost += 5 * k	# 비용 누적

def buy_each(idx):
  global cost
  cost += 3 * arr[idx]	# 비용 누적

n = int(input())
arr = list(map(int, input().split())) + [0, 0]
cost = 0
for i in range(n):
  if arr[i+1] > arr[i+2]:	# 두 번째 지점의 개수가 세 번째 지점의 개수보다 큰 경우는 따로 처리
    k = min(arr[i], arr[i+1]-arr[i+2])	# 첫 번째, 두 번째 지점에서 동시에 살 수 있는 개수 구함
    arr[i] -= k	# 구매한 개수 빼기
    arr[i+1] -= k	# 구매한 개수 빼기
    cost += 5*k	# 비용 누적
    
    buy_triple(i)	# 세 지점에서 동시에 사기
  else:
    buy_triple(i)	# 세 지점에서 동시에 사기
    buy_double(i)	# 두 지점에서 동시에 사기
  buy_each(i)	# 각각 사기
print(cost)