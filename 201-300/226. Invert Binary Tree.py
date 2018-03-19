#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-19 上午11:29
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree1(self, root):
        """
        方法一：递归的方式，反转左右子树
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        self.helper(root)
        return root

    def helper(self, root):
        """
        反转root的左右子结点
        """
        root.left, root.right = root.right, root.left

        # 反转左子树
        if root.left:
            self.helper(root.left)
        # 反转右子树
        if root.right:
            self.helper(root.right)

    def invertTree(self, root):
        """
        方法二：利用栈
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return root
