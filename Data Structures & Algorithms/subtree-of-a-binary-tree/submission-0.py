# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def hasSubtree(root, subRoot):
            if root == None:
                return False

            return sameTree(root, subRoot) or hasSubtree(root.left, subRoot) or hasSubtree(root.right, subRoot)
        
        def sameTree(rootA, rootB):
            if rootA == None and rootB == None:
                return True

            if rootA and rootB and rootA.val == rootB.val and sameTree(rootA.left, rootB.left) and sameTree(rootA.right, rootB.right):
                return True

            return False

        return hasSubtree(root, subRoot)


