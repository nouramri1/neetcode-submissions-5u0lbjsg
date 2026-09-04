class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmin = nums[0]
        currmax = nums[0]
        maxprod = nums[0]
        for num in nums[1:]:
            prevmin = currmin
            prevmax = currmax

            currmax = max(num, prevmax * num, prevmin * num)
            currmin = min(num, prevmax * num, prevmin * num)

            maxprod = max (maxprod, currmax)
        return maxprod

        