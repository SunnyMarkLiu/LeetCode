#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-7 下午12:43
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.dfs(root, sum)

    def dfs(self, root, left_value):
        # 如果遍历到叶子结点的左右空结点，说明　root-to-leaf　已经遍历完，还没找到
        if not root:
            return False

        # 当前结点是叶子结点，判断这个叶子结点的值和 sum 剩下的值是否相等
        if not root.left and not root.right:
            return left_value == root.val

        # 前序遍历左子树
        result = self.dfs(root.left, left_value - root.val)
        if result:
            return True

        # 前序遍历右子树
        result = self.dfs(root.right, left_value - root.val)
        if result:
            return True

        return False
