__doc__ = """
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        leftH = self.height(root.left)
        rightH = self.height(root.right)
        if abs(leftH - rightH) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def height(self, root:TreeNode) -> int:
        if not root:
            return 0
        leftH = self.height(root.left)
        rightH = self.height(root.right)
        return max(leftH, rightH) + 1