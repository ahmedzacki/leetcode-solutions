‌class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        leftSum = 0
        rightSum = sum(nums)

        n = len(nums)
        count = 0

        for right in range(n - 1):
            leftSum += nums[right]

            if leftSum >= rightSum - leftSum:
                count += 1

        return count
