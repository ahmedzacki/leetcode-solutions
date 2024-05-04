### Problem #1047. Remove All Adjacent Duplicates In String

# Time Complexity: O(n)
# Space Complexity: O(n)

To address this problem efficiently, I employed a stack. By iterating over the input string, I aimed to eliminate adjacent duplicates. If the current character matches the one at the top of the stack, it indicates a duplicate, and I then remove the character from the stack. If there's no match, it signifies the absence of duplicates at that moment, and I proceed to add the current character to the stack. Ultimately, the stack will hold the valid string with all duplicates removed. To generate the final output, I concatenate all the characters in the stack to form a single string, effectively transforming the stack array into the desired string format.
