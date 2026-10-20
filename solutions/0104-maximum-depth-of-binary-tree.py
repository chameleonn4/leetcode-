# 104. Maximum Depth of Binary Tree / 二叉树的最大深度
# 难度：简单    语言：Python3    日期：2026-10-20
# 链接：https://leetcode.cn/problems/maximum-depth-of-binary-tree/
# 思路：递归（DFS）。空节点深度为 0；否则当前节点的深度 = 左右子树较大深度 + 1。
#       每个节点只访问一次，递归深度就是树高。
# 复杂度：时间 O(n)，空间 O(h)（h 为树高，递归栈）


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None :
            return 0
        return (max(self.maxDepth(root.left) , self.maxDepth(root.right))+1)
