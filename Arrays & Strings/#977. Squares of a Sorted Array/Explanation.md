### Problem #977. Squares of a Sorted Array

# Time Complexity: O(n)
# Space Comlexity: O(1) 

To efficiently solve this problem, I decided to use a two-pointer technique. I also created extra memory space for the answer. I initialized my left and right pointers, and each time I compared the leftmost and rightmost values (assuming both are squared), whichever one was greater was added to the answer list at its appropriate position in the list. In this case, I used another variable to keep track of the current position that needed to be filled in the answer array. At the end, the list is sorted and squared, and the ans list will be returned.
