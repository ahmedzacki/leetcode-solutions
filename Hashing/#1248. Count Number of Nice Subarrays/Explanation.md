### Problem #1426. Counting Elements

# Time Complexity: O(n)

# Space Complexity: O(n)

To efficiently solve this problem, I utilized a hash table to keep track of the counts of the number of odd numbers in each subarray. Then, I employed a for loop to iterate over the input. At each element, I calculated the number of odd numbers and checked if there were any other subarrays preceding this array with an odd number count satisfying our requirement (k). In other words, if (curr - k) is found in our dictionary, it indicates that one or more subarrays before this subarray had a number of odd numbers such that subtracting it from the current count would result in k. Consequently, we updated our answer with the value of (curr - k) from our hash table and stored the new/current number of odd numbers in our hash table.
