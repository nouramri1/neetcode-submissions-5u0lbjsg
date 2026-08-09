class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            #base case:
            if i >= len(nums):
                res.append(subset.copy())
                return 
            # yes include the option:
            subset.append(nums[i])
            dfs(i + 1)
            # No dont include the option:
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res

        # or 
        # res = [[]]
        # for n in nums:
        #     res += [ lst + [n] for lst in res]
        # return res 




       

        