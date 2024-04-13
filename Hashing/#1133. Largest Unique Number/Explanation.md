### Problem #1133. Largest Unique Number

# Time Complexity: O(n)

# Space Complexity: O(n)

To solve this problem efficiently, a hash table was utilized to keep track of the frequencies of each number in the input array. Subsequently, another for loop was employed to iterate over the hash table and identify the maximum number that occurred only once. If there were no unique max numbers, -1 was returned.
