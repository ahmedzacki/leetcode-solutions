
### Problem #643. Maximum Average Subarray I

# Time Complexity: O(n)
# Space Complexity: O(1)

To solve this problem, I decided to use a sliding window. I kept the window to a fixed length, then did the calculation by summing up the elements in the window and taking the average, then updating the answer. However, when I want to check another subarray, I add an element from the right to the window and remove one from the other end at the same time to keep the length constraint valid. To add all of these elements, I am just using a single variable. So, to add another element to the window, I just add it to the current variable and subtract from it at  same time.
