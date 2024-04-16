### Problem #24. Swap Nodes in Pairs

# Time Complexity: O(n)
# Space Complexity: O(1)

To efficiently address this challenge, I needed to adeptly manipulate pointers while carefully considering several edge cases. There are three primary edge cases to note: First, if the list is empty, I simply return it as is. Second, if the list consists of only one node, I return that node directly. The third edge case revolves around whether the list contains an odd or even number of nodes, as this distinction is crucial for adjusting the pointers correctly.

Furthermore, it's essential to identify and save the new head of the linked list after completing the pair swaps. To achieve this, I utilized a placeholder variable, denoted as dummy, which points to the second node in the list (dummy = head.next). This setup ensures that we have a reference to the new head once the swaps are finalized.

The main logic involves iterating over the list to examine each node pair. For every pair, I used a temporary variable to save the connection to the subsequent list segment. I also maintained a reference to the current head using a variable, and another variable named prev to keep track of the preceding node. With these references, I proceeded to swap each pair.

After swapping, it's necessary to update the current head to the next pair. However, before moving on, I assessed whether any nodes remained. If only one node is left, indicating an odd number of nodes, no further pointer adjustments are made. Conversely, if a pair remains, indicating an even number of nodes, I ensure prev.next is updated to point to the next node in the sequence, thus maintaining the integrity of the swapped list.



