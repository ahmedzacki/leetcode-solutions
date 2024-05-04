‌class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for ch in s:
            # Check if stack is not empty and the last character is a case-insensitive match but not a case-sensitive match to the current character
            if stack and stack[-1].lower() == ch.lower() and stack[-1] != ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
