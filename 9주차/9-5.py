n, k = int(input()), list(map(int, input().split()))	# 추의 개수 n, 추의 무게 k
m, l = int(input()), list(map(int, input().split()))	# 구슬의 개수 m, 구슬의 무게 l
# 추의 무게는 최대 500dlamfh [[추의 개수 *500]*추의 개수]로 배열 구성
dp, r = [[0 for j in range((i+1)*500+1)] for i in range(n+1)], []

def cal(num, weight):
  if num > n:	# 추의 개수보다 크면 리턴
    return
  
  if dp[num][weight]:	# 해당 값이 0이 아니면 리턴
    return
  
  dp[num][weight] = 1
  
  cal(num+1, weight)	# 추를 사용하지 않는다
  cal(num+1, weight+k[num-1])	# 추의 무게를 더한다
  cal(num+1, abs(weight-k[num-1]))	# 추의 무게를 뺀다

cal(0, 0)

for i in l:
  if i > 30*500:
    r.append("N")
    continue
  if dp[n][i] == 1:
    r.append("Y")
  else:
    r.append("N")
print(*r)