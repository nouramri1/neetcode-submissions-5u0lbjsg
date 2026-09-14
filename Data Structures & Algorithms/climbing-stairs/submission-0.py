class Solution:
    def climbStairs(self, n: int) -> int:
        # number of steps to reach the top of a staircase 
        # either 1 or 2 
        # n = 3
        # dp = [ 3.  2.  1, 1]

        one = 1
        two = 1 
        for i in range(n - 1):
            temp = one 
            one = one + two 
            two = temp
        return one

        