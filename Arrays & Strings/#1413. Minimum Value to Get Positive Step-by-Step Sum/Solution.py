class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        left = 0
        right = 100 * len(nums) + 1
        ans = right - left // 2
        while left < right:
            mid = right - left // 2

            isInvalid = False
            newMid = mid
            for i in range(len(nums)):
                newMid += nums[i]
                if newMid <= 0:
                    isInvalid = True
                    break

            if isInvalid:
                left = mid + 1
            else:
              ans=min(ans,mid)
              right=mid-1

        return ans
