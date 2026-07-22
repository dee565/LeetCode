# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        ans = []
        def traversal(curr):
            if not curr:
                return
            traversal(curr.left)
            traversal(curr.right)
            ans.append(curr.val)
        traversal(root)
        return ans
        