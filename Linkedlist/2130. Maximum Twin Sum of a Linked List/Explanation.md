### Problem #2130. Maximum Twin Sum of a Linked List


# Time Complexity: O(n)
# Space Complexity: O(1)

To efficiently solve this problem, I employed a technique to manipulate the pointers, recognizing that the length of the linked list was an even number. I understood that twin nodes correspond to each other when counted from opposite ends. For example, the twin of the first node in the linked list is the last node, the twin of the second node is the second-to-last node, and so on. Therefore, my approach involved iterating over the first half of the linked list and adjusting their pointers to point in the opposite direction.

I used a while loop to iterate over both halves of the linked list. At each iteration, I ensured that I had the twin nodes and simply added their values. Then, I checked if the sum of the values of the current twin nodes was greater than the current maximum sum we had so far. If it was, I updated the maximum sum; if not, I moved on to the next twin nodes
