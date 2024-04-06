class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        if k == 0:
            return nums

        ans = [-1] * n

        pref = [nums[0]]

        for i in range(1, len(nums)):
            pref.append(nums[i] + pref[-1])
          
        # We iterate only on those indices which have atleast 'k' elements in their left and right.
        for index in range(k, len(nums) - k):

            leftBound = index - k
            rightBound = index + k

            if leftBound >= 0 and rightBound <= n - 1:
                temp = pref[rightBound] - pref[leftBound] + nums[leftBound]
                ans[index] = temp // (2 * k + 1)

        return ans
