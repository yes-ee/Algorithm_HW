import sys

# 키에서 이진 검색 트리를 구성하기 위한 최적의 비용 찾기
# 'i'에서 'j' 까지, 여기서 각 키 'k'는 'freq[k]' 횟수로 발생
def findOptimalCost(freq, i, j, level):
  # 베이스 케이스
  if j < i:
    return 0
  optimalCost = sys.maxsize
  # 각 키를 루트로 간주하고 재귀적으로 최적의 솔루션을 찾음
  for k in range(i, j+1):
    # 왼쪽 하위 트리의 최적 비용을 재귀적으로 찾음
    leftOptimalCost = findOptimalCost(freq, i, k-1, level+1)
    # 올바른 하위 트리의 최적 비용을 재귀적으로 찾음
    rightOptimalCost = findOptimalCost(freq, k+1, j, level+1)
    # 현재 노드의 비용은 'freq[k]*level'
    # 최적 비용 업데이트
    optimalCost = min(optimalCost, freq[k] * level + leftOptimalCost + rightOptimalCost)
  
  # 최소값 반환
  return optimalCost

freq = list(map(int, input().split()))
# freq = [25, 10, 20]
print('binary search tree를 구성하는 데 드는 최소 비용은:', findOptimalCost(freq, 0, len(freq) - 1, 1))