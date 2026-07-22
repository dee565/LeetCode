# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, n: Optional[TreeNode]) -> bool:
        return bool((f:=lambda l,r:l==r==None or l and r and l.val==r.val
        and f(l.left,r.right) and f(l.right,r.left))(n.left,n.right))
        