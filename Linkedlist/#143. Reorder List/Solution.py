‌# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # find the middle node first

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slwo is at node 3, fast is Null
        # now, lets reverse the second half

        prev = None
        curr = slow

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        # prev is the head of the second half now

        # start merging the two halves now

        first, second = head, prev

        while second.next:
            nextFirst = first.next
            first.next = second
            first = nextFirst

            nextSecond = second.next
            second.next = first
            second = nextSecond
