
‌class Solution:
    def simplifyPath(self, path: str) -> str:

        data = path.split("/")

        stack = []

        for item in data:
            if item == "..":
                if stack:
                    stack.pop()
            elif item != " " and item != "" and item != ".":
                stack.append(item)

        if stack:
            return "/" + "/".join(stack)
        else:
            return "/"
