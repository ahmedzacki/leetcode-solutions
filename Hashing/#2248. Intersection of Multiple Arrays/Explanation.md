### Problem #2248. Intersection of Multiple Arrays


# Time Complexity: O(n)
# Space Complexity: O(n)

In order to efficiently solve this problem, I utilized a hash table. I employed a for loop to iterate over each array in the nums list and count the frequency of the integers. Then, using another for loop, I iterated over the hash table to find the integers that appeared once in each array of the nums list by checking if the value associated with every key in the hash table is equal to the length of the nums list. Subsequently, I stored these valid keys in another array. For the final answer, I returned a sorted answer list.
