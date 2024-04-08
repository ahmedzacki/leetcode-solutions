class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        # Create a hashmap to count the frequency of each element in nums[i]
        # Iterate through the hashmap and look for keys that have values equal to
        #the length of  the nums array
        # Store  the keys with those values in a different array
        # Return that array

        count = defaultdict(int)

        for el in nums:
            for num in el:
                count[num] += 1

        ans = []
        n = len(nums)

         for key in count:
             if count[key] == n:
                 ans.append(key)

         return sorted(ans)
