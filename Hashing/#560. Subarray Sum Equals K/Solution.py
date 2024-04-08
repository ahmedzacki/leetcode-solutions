class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # Create a dictionary to store prefix sums and their occurrences
        # Initialize the dictionary with a prefix sum of 0 since an empty subarray has a sum equal to 0
        count = { 0 : 1 }
        curr = ans = 0

        for num in nums:
            curr += num
            ans += count.get(curr - k, 0) # Returns zero if this doesn't exist
            count[curr] = count.get(curr, 0) + 1
        return ans
