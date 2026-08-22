class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {'}': '{', ')': '(', ']': '['}

        for c in s:
            if c in closeToOpen: # if its a close
                if stack and stack[-1] == closeToOpen[c]:
                    close = stack.pop()
                else: # close but no open
                    return False
            else:
                stack.append(c)

        return len(stack) == 0