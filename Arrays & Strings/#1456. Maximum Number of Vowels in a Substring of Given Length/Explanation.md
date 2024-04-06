### Problem #1456. Maximum Number of Vowels in a Substring of Given Length

# Time Complexity: O(n)
# Space Complexity: O(1)

To solve this problem efficiently, a variable "vowels" is created to store the set of vowels in the alphabet. The first substring is built using the sliding window technique while counting the number of vowels in the window. After obtaining the first substring, the "ans" variable is updated. Then, a for loop is initiated starting at index "k," which represents the length of the substring. In each iteration of the for loop, the window expands to create a new substring while simultaneously deleting a character from the left end of the window to maintain a constant length of "k." If the character being deleted is a vowel, we decrease the current count of vowels for that specific window; conversely, if there's a vowel added to that window, we increase its count. Finally, we update "ans." Once all iterations are complete, we return "ans."
