class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if num in map:
                return [map[num], i]
            map[remaining] = i
            
        