import sys
import heapq
n = int(sys.stdin.readline().rstrip("\n"))
nums=[]
temps=[0]*(n+1)
for _ in range(n):
  deadline, value = map(int, sys.stdin.readline().rstrip("\n").split())
  nums.append((deadline, value))

nums = sorted(nums)	# 데드라인을 오름차순으로 정렬
heaps=[]

for num in nums:
  heapq.heappush(heaps, num[1])	# 데드라인 순으로 각 문제의 컵라면 수를 리스트에 추가
  if (num[0] < len(heaps)):	# 리스트의 길이가 데드라인보다 크면 데드라인을 초과함 -> pop
    heapq.heappop(heaps)
print(sum(heaps))	# 최대 컵라면 수 출력