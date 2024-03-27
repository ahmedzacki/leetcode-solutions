### Problem #392. Is Subsequence

# Time Complexity: O(n)
# Space Complexity: O(1)

To efficiently solve this problem, I decided to use a two-pointer technique. The goal is to determine if string "s" is a subsequence of string "t", meaning all characters of "s" must appear in "t" in the same order. I initiated two pointers to iterate over "s" and "t" from the start. For each comparison, I only advance the pointer in "s" if the current characters match; otherwise, I only move the pointer in "t" forward. The process continues until one or both strings are fully scanned. If, by the end of the loop, all characters of "s" have been matched within "t", we conclude that "s" is a subsequence of "t," and return True. If there are unmatched characters left in  s , we return False, indicating that  s  is not a subsequence of  t .
