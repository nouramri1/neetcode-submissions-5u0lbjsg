class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # array of integers nums , integer k 
        # slinding window of size k starts at the left edge of the array
        # the window slides one position at a time
        res = []
        
        for l in range (len(nums) - k + 1):
            res.append(max(nums[l: l + k ]))
        return res


        