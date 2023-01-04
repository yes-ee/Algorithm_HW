class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution(object):
	def sortList(self, head):
		# mid (pivot) 선정하는 함수
		def get_mid(head):
			s = f = head
			while f and f.next:
				s, f = s.next, f.next.next
			return s.val

		# 피벗 기준으로 l, m, r 나누는 함수
		def partition(head, val):
			fake_l = l = ListNode(0)
			fake_m = m = ListNode(0)
			fake_r = r = ListNode(0)
			cur = head
			# head에 연결된 노드 순회
			while cur:
				# 피벗보다 작으면 l 리스트에 연결
				if cur.val < val:
					l.next = cur
					l = l.next
				# 피벗과 같으면 m 리스트에 연결
				elif cur.val  == val:
					m.next = cur
					m = m.next
				# 피벗보다 크면 r 리스트에 연결
				elif cur.val > val:
					r.next = cur
					r = r.next
				cur = cur.next
			l.next, m.next, r.next = None, None, None
			return fake_l.next, fake_m.next, fake_r.next
		
		# next 노드가 None인 노드 반환
		def get_tail(head):
			cur = head
			while cur.next:
				cur = cur.next
			return cur

		# 노드 합치기
		def combine(l, m, r):
			fake = ListNode(0)
			fake.next = l
			t = get_tail(fake)
			t.next = m
			t = get_tail(t)
			t.next = r
			return fake.next	# 합쳐진 리스트 반환

		if not head or not head.next:	# 노드가 없거나 다음 노드가 없으면 리턴
			return head
		l, m, r = partition(head, get_mid(head))	# get_mid(head) 한 피벗 기준으로 l m r 나눔
		# l r 각각 재귀적으로 정렬
		l = self.sortList(l)
		r = self.sortList(r)
		return combine(l, m, r)

a = Solution()
list0 = ListNode()
list1 = ListNode()
list2 = ListNode()
list0.val = -1
list0.next = list1
list1.val = 5
list1.next = list2
list2.val = 3
ans = a.sortList(list0)
p = list0
print("ans :", end = ' ')
while p != None:
  print(p.val, end = ' ')
  p = p.next