class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0  # Initialize pointers for strings s and t.

        while i < len(s) and j < len(t):  # Traverse both strings.
            if s[i] == t[j]:  # If characters match,
                i += 1  # move to the next character in s.
            j += 1  # Always move to the next character in t.

        if i < len(s):  # If not all characters in s are matched,
            return False  # s is not a subsequence of t.

        return True  # All characters in s are matched in t.
