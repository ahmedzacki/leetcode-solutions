class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Initialize pointers and the answer list.
        n = len(nums) - 1  
        left, right = 0, n 
        ans = [] 
      
        # Loop until the left pointer exceeds the right pointer.
        while left <= right:
            # Compare squared values at the left and right pointers.
            if nums[left] ** 2 > nums[right] ** 2:
                ans.append(nums[left]**2)  
                left += 1 
            else:
                ans.append(nums[right]**2)  # Add the larger squared value to the answer list.
                right -= 1 
        # Return the reversed list to ensure it is sorted in non-decreasing order.
        return ans[::-1]
