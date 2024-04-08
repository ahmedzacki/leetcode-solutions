class Solution:
    def countElements(self, arr: List[int]) -> int:

        count = defaultdict(int)
        ans = 0

        # build hash table for the array elements
        for num in arr:
            count[num] += 1

        for num in arr:
            if num + 1 in count:
                ans += 1

        return ans
