class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")":"(","]":"[","}":"{" }
        stack = []
        for par in s:
            if par in closeToOpen:
                if stack and stack[-1] == closeToOpen[par]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(par)

        return True if not stack else False
                

        