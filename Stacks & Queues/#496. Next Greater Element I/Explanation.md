### Problem #496. Next Greater Element I

# Time Complexity: O(n)
# Space Complexity: O(n)

To efficiently tackle this challenge, I utilized a stack alongside a hashtable. The stack was employed to maintain a descending order of the numbers in the nums2 array, enabling the identification of the next greater number for each element in nums2. Upon discovering the next greater number, I stored this information in the hashtable, with the original number serving as the key and its next greater counterpart as the value. In the final step, I iterated over the nums1 input array using a for loop. For each number in nums1, I retrieved its corresponding greater number from the hashtable. If a number's next greater counterpart was absent in the hashtable, I substituted that instance in the nums1 array with -1. Consequently, I returned the modified nums1 array as the solution.
