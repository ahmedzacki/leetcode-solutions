‌# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head

        prev = head
        curr = head.next

        while curr:
            if curr.val == prev.val:
                # keep reference to the future node
                temp = curr.next
                prev.next = temp
                curr = prev.next

            # only move forward if the curr and prev node are different
            if curr != None and curr.val != prev.val:
                prev = curr
                curr = curr.next

        return head
