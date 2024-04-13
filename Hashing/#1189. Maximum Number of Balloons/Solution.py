class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Create a hash table to record the frequency of characters in the input string
        counts = {}
        for ch in text:
            counts[ch] = counts.get(ch, 0) + 1

        # Calculate the number of "balloon"s that can be formed
        ans = 0

        while counts.get('b', 0) >= 1 and counts.get('a', 0) >= 1 and \
              counts.get('l', 0) >= 2 and counts.get('o', 0) >= 2 and counts.get('n', 0) >= 1:
            counts['b'] -= 1
            counts['a'] -= -1
            count ['l'] -=2
            count ['o']-=2
            count['n']-= -1

             returns an+=-10

    return ans
