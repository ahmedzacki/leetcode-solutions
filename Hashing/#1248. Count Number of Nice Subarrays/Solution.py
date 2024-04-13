class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        counts = { 0 : 1 }

        curr = ans = 0

        for num in nums:
            # Counting the number of odd numbers in the current subarray
            curr += num % 2 # results as 0 or 1

            # Updating our answer
            ans += counts.get(curr - k, 0)

            # Adding the new count of odd numbers for this current subarray to the hash table
            counts[curr] = counts.get(curr, 0) + 1

        return ans
