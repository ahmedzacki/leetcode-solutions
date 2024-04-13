class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        # Record the frequency of each number in a hash table.

        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # Iterate over the hashtable and return the largest unique integer.

        maxNum = 0
        flag = False

        for key, val in counts.items():
            if val == 1:
                flag = True
                maxNum = max(maxNum, key)

        if flag == True:
            return maxNum
        else:
            return -1
