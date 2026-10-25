# 94. Binary Tree Inorder Traversal / 二叉树的中序遍历
# 难度：简单    语言：Python3    日期：2026-10-25
# 链接：https://leetcode.cn/problems/binary-tree-inorder-traversal/
# 思路：递归 DFS。中序遍历的顺序是「左子树 → 根 → 右子树」，所以先递归左子树，
#       再把当前节点的值追加到 res，最后递归右子树。
#       进阶：递归在树很深时会栈溢出，可以用栈手动模拟（迭代版）做到 O(h) 空间、O(n) 时间。
# 复杂度：时间 O(n)，空间 O(h)（h 为树高，递归栈）


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
