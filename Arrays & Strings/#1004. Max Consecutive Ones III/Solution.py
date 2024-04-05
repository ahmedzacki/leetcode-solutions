‌class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = right = ans = count = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                count += 1

            while count > k:
                 # remove zeros
                if nums[left] == 0:
                    count -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans
