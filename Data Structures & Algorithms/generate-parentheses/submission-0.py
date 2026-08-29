class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we saw this before 
        # input: integer n 
        # return all well formed parentheses string 
        # we have to use backtracking and keep count of the closed and open parenthesis 
        res = []
        stack = []
        def backtrack(openN, closeN):
            # when do we stop ?
            # base case
            if closeN == openN == n:
                res.append(''.join(stack))
                # thos return means return to the call
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        backtrack(0,0)
        return res
            
        