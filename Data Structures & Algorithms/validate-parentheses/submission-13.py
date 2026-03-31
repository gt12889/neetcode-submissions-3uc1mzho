class Solution:
    def isValid(self, s: str) -> bool:
        cTo = {"}":"{","]":"[",")":"("}
        stack = []
        if len(s) == 0:
            return True
        if not s:
            return False
        for i in s: #every c in string
            if i in cTo: #if closing
                if not stack:
                    return False
                if stack.pop() != cTo[i]: #
                    return False
            else:
                stack.append(i)
        return not stack