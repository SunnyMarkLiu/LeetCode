#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-19 下午7:20
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        从根结点（root）找左子树（l）的最右子结点（x），将root的右子树（r）接到x的右子树上（x的右子树为空），
        root的左子树整体调整为右子树，root的左子树赋空。 递归 root.right
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        while root:
            # 如果左子树为空，则不用处理
            if root.left:  # 左子树不为空，找到左子树最右边的结点
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right

                # 把当前root结点的右子树拼接到最右边结点的right
                tmp.right = root.right
                # root的左子树移到右结点
                root.right = root.left
                # 清空root的左子树结点
                root.left = None

            # 处理右子树
            root = root.right
