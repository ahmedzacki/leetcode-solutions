### Problem #2090. K Radius Subarray Averages

# Time Complexity: O(n)
# Space Complexity: O(n)

To efficiently solve this problem, I used the prefix sum technique. Since I needed to find the averages of subarrays of size 2k+1, I used an extra array pref to store all the prefixes of the original nums array. Then, I used a loop to iterate only on those indices which have at least k elements from both left and right and calculated their average using the precomputed prefix sum array. If an array has a radius of 0, there is no work to do and I just returned the original list or array.
