‌class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def compareStrings(s):
            stack = []
            for ch in s:
                if ch != "#":
                    stack.append(ch)
                elif stack:
                    stack.pop()

            return "".join(stack)

        return compareStrings(s) == compareStrings(t)
