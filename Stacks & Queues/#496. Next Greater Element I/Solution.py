‌from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        data = {}

        for num in nums2:
            while stack and num > stack[-1]:
                data[stack[-1]] = num
                stack.pop()

            stack.append(num)

        for i in range(len(nums1)):
            if nums1[i] in data:
                nums1[i] = data[nums1[i]]
            else:
                nums1[i] = -1

        return nums1
