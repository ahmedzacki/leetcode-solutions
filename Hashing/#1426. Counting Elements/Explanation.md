### Problem #1426. Counting Elements

# Time Complexity: O(n)

# Space Complexity: O(n)

To efficiently solve this problem, a hash table was used. The numbers in the original array were stored in the hash table. Then, a for loop was executed against the input array to check if ( (the number + 1) ) exists in the hash table. If it does, the ans variable is incremented. After the loop ends, the ans variable is returned.
