class Treenode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution(object):
  def findTarget(self, root, k):
    if not root:	# root가 없으면 false
      return False
    return self._findTarget(root, set(), k)
  
  def _findTarget(self, node, nodes, k):
    if not node:	# node가 없으면 false
      return False
    complement = k - node.val
    # node 집합에 타겟값 complement에 해당하는 값 있으면 sum이 target과 같다는 뜻 : true
    if complement in nodes:
      return True
    nodes.add(node.val)	# 해당하는 값 없으면 현재 노드를 set에 추가
    # 왼쪽 자식 노드와 오른쪽 자식 노드를 대상으로 재귀적으로 검사
    return self._findTarget(node.left, nodes, k) or self._findTarget(node.right, nodes, k)
  
# 실행 결과 확인
a = Solution()
node1 = Treenode()
node2 = Treenode()
node3 = Treenode()
node4 = Treenode()
node5 = Treenode()
node6 = Treenode()
node1.__init__(5, node2, node3)
node2.__init__(3, node4, node5)
node3.__init__(6, None, node6)
ans = a.findTarget(node1, 9)
print("ans :", ans)