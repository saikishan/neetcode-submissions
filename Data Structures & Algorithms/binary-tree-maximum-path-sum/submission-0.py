# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -float('inf')

        if root == None:
            return 0

        def recurFindMaxPath(root):
            nonlocal result

            if root == None:
                return 0

            left = recurFindMaxPath(root.left)
            right = recurFindMaxPath(root.right)

            result = max(result, root.val + max(0, left) + max(0, right))

            return root.val + max(0, left, right)

        recurFindMaxPath(root)

        return result

