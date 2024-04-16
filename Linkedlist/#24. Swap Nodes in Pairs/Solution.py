‌# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        #first make sure we have a pair to swap
        dummy = head.next

        while head and head.next:
            prev = head
            # save the next pair
            nextNode = head.next.next
            #swap the pair now
            head.next.next = head
            head.next = nextNode
            #update the head for the next pair
            head = nextNode

            #if there are two more pairs left, change the prev.next pointer to the correct Node
            if head and head.next:
                prev.next = head.next

        return dummy
