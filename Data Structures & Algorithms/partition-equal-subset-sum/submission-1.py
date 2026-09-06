from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        @cache
        def dfs(i, current_sum):
            if current_sum == target:
                return True

            if i == len(nums) or current_sum > target:
                return False

            # Take nums[i]. If this works, we're done.
            if dfs(i + 1, current_sum + nums[i]):
                return True

            # Otherwise, try skipping nums[i].
            return dfs(i + 1, current_sum)

        return dfs(0, 0)