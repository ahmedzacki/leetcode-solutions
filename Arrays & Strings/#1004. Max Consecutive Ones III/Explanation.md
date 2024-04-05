### Problem #1004. Max Consecutive Ones III

# Time Complexity: O(n)
# Space Complexity: O(1)

To solve this problem, I decided to use the sliding window technique because I had the constraint to find consecutive subarray elements. So, I bet on the sliding window. I have a window that is valid as long as it has no more than k zeros in it. If the window gets another element and the constraint is broken, then I used a while loop to make the window valid again by removing zeros from the left end of the window until the constraint is satisfied again. Then, I update the answer with the window that has the longest length.
