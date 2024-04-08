class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Find the length of nums
        # Create a set and insert all the numbers in nums [0, n]
        # Run a for loop against the range [0, n] and check if every number in the range appears in the set
        # If a number in the range doesn't exist in the set then we have found our answer and just return that number

        myRange = set(nums)

        n = len(nums) + 1

        for i in range(n):
            if i not in myRange:
                return i     ‌
