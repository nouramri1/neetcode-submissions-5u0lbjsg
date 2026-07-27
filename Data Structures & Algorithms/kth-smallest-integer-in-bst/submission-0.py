# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # dfs in order traverasal
        def dfs(node):
            counter = 0
            if not node:
                return []
            res = []
            res.extend(dfs(node.left))
            res.append(node.val)
            res.extend(dfs(node.right))
            return res
        return dfs(root)[k-1]




        