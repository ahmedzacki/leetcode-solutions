### Problem #724. Find Pivot Index

# Time Complexity: O(n)
# Space Comlexity: O(n) 

To solve this problem efficiently, I utilized the prefix sums technique. By creating an additional array of prefix sums, I could easily determine the sum of the left and right subarrays in each iteration in constant time. If the sum of the left subarray equaled the sum of the right subarray, I returned the current index. If the for loop exited without finding a pivot index that satisfied the condition, I simply returned -1.
