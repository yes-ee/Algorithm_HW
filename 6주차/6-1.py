# 배열을 균형 이진 검색 트리로 변환

class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


# 중간 값 구한 후에 왼쪽 오른쪽 트리 재귀적으로 구성
class Solution(object):
	def sortedArrayToBST(self, nums):
		len_nums = len(nums)
		if len_nums == 0:
			return None
		
		mid_node = len_nums // 2	# 중간 노드 구함
		return TreeNode(
			nums[mid_node],
			self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node+1:])
		)

# 실행 결과 확인
a = Solution()
ans = a.sortedArrayToBST([-10, -3, 0, 5, 9])

class Ans(object):
  def print_bst(self, root):
    if root is None:
      print("null", end = ' ')
      return
    print(root.val, end = ' ')
    self.print_bst(root.left)
    self.print_bst(root.right)
b = Ans()
b.print_bst(ans)