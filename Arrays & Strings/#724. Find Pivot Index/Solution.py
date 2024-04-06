class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # at each index, find the left sum and right sum
        # then compare both sums
        # if they are equal, return that index
        # if not, move on to the next index
        # at index 0, left sum = 0,
        # at index n - 1, right sum = 0,

        #pre-computing prefixes of nums array to easily find subarray sums

        pref = [nums[0]]

        for i in range(1, len(nums)):
            pref.append(nums[i] + pref[-1])

        leftSum = 0

        for i in range(len(nums)):
            if i != 0:
                leftSum = pref[i - 1]

            rightSum = pref[-1] - pref[i]

            if leftSum == rightSum:
                return i

          return -1
