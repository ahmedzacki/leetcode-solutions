‌class Solution:
    def isValid(self, s: str) -> bool:


        # create stack
        stack = []

        brkts = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        # go over the input string
        # if the current ch in the string is an open bratks, put it in the stack
        # if the current ch in the string is a close bratks, check if the bracket at the top of the stakc is its opening brack, if not return false, otherwise remove from the stack and keep scanning

        for ch in s:
            if ch not in brkts:
                stack.append(ch)
            else:
                tmp = brkts.get(ch)
                if not stack or tmp != stack[-1]:
                    return False
                stack.pop()


        return len(stack) == 0
