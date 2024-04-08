### Problem #560. Subarray Sum Equals K

# Time Complexity: O(n)

# Space Complexity: O(n)

To solve this problem efficiently, the prefix sum technique was utilized. Additionally, a hash map was employed to store the occurrences of prefix sums of subarrays. The process involved iterating over the array and calculating the sum of the subarray that ends at each index. Then, it checked for valid subarrays ending at the current index with a sum equal to k. If found true, it updated the answer with the number of occurrences that happened in the past due to potential negative numbers in the input array.
