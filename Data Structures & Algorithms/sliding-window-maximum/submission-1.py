import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # array of integers nums , integer k 
        # slinding window of size k starts at the left edge of the array
        # the window slides one position at a time
        # we can use queue 
        output = []
        l,r = 0 , 0
        q = collections.deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # q[-1] means the top of the queu
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
            


        