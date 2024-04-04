
### Problem #713. Subarray Product Less Thank K

# Time Complexity: O(n)
# Space Complexity: O(1)

To solve this problem, I decided to use the sliding window technique because I had the constraint to find the number of subarrays and a constraint metric which was the product of inside the subarray to be less than k. Since sliding window is efficient for this kind of problems, I also defined a few variables: left, right, ans, curr=product of all elements inside the valid subarray. To find the subarrays, I had to find a valid subarray and then mathematically calculate the number of valid subarrays by taking the length of that valid subarray and adding it to our answer. If the window becomes invalid, I used a while loop to make the window valid again.
