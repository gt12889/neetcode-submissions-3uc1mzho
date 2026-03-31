# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr= []

        def dfs(n):
            if not n:
                return None
            arr.append(n.val)
            dfs(n.left)
            dfs(n.right)

        dfs(root)
        arr.sort()
        return arr[k-1]