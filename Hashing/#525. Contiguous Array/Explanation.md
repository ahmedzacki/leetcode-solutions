### Problem #525. Contiguous Array

# Time Complexity: O(n)

# Space Complexity: O(n)

To efficiently solve this problem, a hash table was used. Within the hash table, the current sum of the current subarray was stored as a key. Subsequently, the index where that sum was found was stored as the key's value in the hash table. A for loop iterated over the input array and computed and stored each sum in the hash table. If a sum already existed in the hash table, it indicated that a valid subarray existed between the current index and a previous index.

In such cases, by retrieving the value of that sum (the index), it became possible to calculate the length of that valid subarray by subtracting it from its corresponding current index. This updated answer variable would help track if there is possibly another longest valid subarray starting from index 0 up until the current index.

Finally, after looping through all elements, returning the answer variable would provide an accurate result.
