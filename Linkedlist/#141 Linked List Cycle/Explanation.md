### Problem #141 Linked List Cycle

# Time Complexity: O(n)
# Space Complexity: O(1)

To efficiently solve this problem, I used the fast and slow pointers technique in a linked list and achieved it in constant memory space. My technique is based on the fact that a cycle exists in the linked list if the fast and slow pointers meet twice because the fast pointer moves twice as fast as the slow pointer. Therefore, they are guaranteed to meet a second time apart from their initial meeting point at the head. If there is no cycle in the linked list, the loop will end after reaching the tail, and I simply return False.
