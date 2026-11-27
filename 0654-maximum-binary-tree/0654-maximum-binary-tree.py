# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        mx = max(nums)
        maxindx = nums.index(mx)
        
        node = TreeNode(mx)
        if maxindx > 0:
            node.left = self.constructMaximumBinaryTree(nums[:maxindx])
        
        if maxindx < len(nums) - 1:
            node.right = self.constructMaximumBinaryTree(nums[maxindx+1:])
        
        return node
        