‌# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # find the length of the linkedlist
        n = 0
        curr = head
        while curr:
            n+=1
            curr = curr.next
        ans = 0
        prev = None
        dummy = head
        count = 0
        while count < n // 2:
            nextNode = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = nextNode
            count += 1

        left = prev
        right = nextNode

        while left and right:
            twinSum = left.val + right.val
            ans = max(ans, twinSum)
            left = left.next
            right = right.next

        return ans
