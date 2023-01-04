import sys
input = sys.stdin.readline

v, e = map(int, input().split())
# root를 저장하는 vroot 배열을 생성
# (여기에서 root는 연결 요소 중 가장 작은 값, 처음에는 자기 자신을 저장함)
vroot = [i for i in range(v+1)]
elist = []	# 간선
for _ in range(e):
  elist.append(list(map(int, input().split())))
  
elist.sort(key=lambda x:x[2])	# 간선들을 가중치 기준으로 정렬

def find(x):	# root 찾는 함수
  if x != vroot[x]:
    vroot[x] = find(vroot[x])
  return vroot[x]

ans = 0
for s, e, w in elist:
  # 간선들을 이은 두 정점을 find 함수를 통해 두 root(sroot, eroot)를 찾음
  sroot = find(s)
  eroot = find(e)
  # 두 root가 다르면 큰 root 값을 작은 root값으로 만들어 연결되게 해줌
  if sroot != eroot:
    if sroot > eroot:
      vroot[sroot] = eroot
    else:
      vroot[eroot] = sroot
    ans += w	# 가중치 누적
    
print("ans :", ans)