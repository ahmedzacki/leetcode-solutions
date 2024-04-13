class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        # [0,1,2,3,4,5,6,7]
        # [1,1,1,-1,1,-1,-1,1]

        # {
        #     1:0
        #     2:1
        #     3:2
        # }

        # max = 6
        # sum = 2

        counts = {}
        CurrSum = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                CurrSum += 1
            else:
                CurrSum -= 1

            # check if the CurrSum is already store in the hash table
            if CurrSum in counts:
                # find the index of where that sum was recorded and then substract it from the current index to find the length
                index = counts.get(CurrSum)
                sub_len = i - index
                # udate answer
                ans = max(ans, sub_len)

            # check if the sum equal to zero, that means we have a valid subarray starting fromt he first index up unitl the last index
            elif CurrSum == 0:
                ans = max(ans, i+1)

            # store the curr sum in the hash table as a key, and give their index as a value (index is where the sum was found)
            else:
                counts[CurrSum] = i
        return ans
