#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-9 上午10:10
"""
import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST1(self, root):
        """
        递归的方式检测是否满足ＢＳＴ的要求
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        # 当前结点是否满足ＢＳＴ，同时左右子树是否满足
        return self.dfs_valid(root, -sys.maxsize, sys.maxsize)

    def dfs_valid(self, root, min_val, max_val):
        """
        当前结点是否满足ＢＳＴ
        """
        # 空结点
        if not root:
            return True

        if root.val <= min_val or root.val >= max_val:
            return False

        # 检测左子树时，其参考的最大值为当前结点的值
        # 检测右子树时，其参考的最小值为当前结点的值
        return self.dfs_valid(root.left, min_val, root.val) and self.dfs_valid(root.right, root.val, max_val)

    def isValidBST(self, root):
        """
        方法二：对二叉树进行中序遍历，得到遍历的序列是否是递增的序列
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        res_seq = []
        self.inner_traversal(root, res_seq)

        for i in range(0, len(res_seq) - 1):
            if res_seq[i] >= res_seq[i + 1]:
                return False

        return True

    def inner_traversal(self, root, results):
        if not root:
            return

        self.inner_traversal(root.left, results)
        results.append(root.val)
        self.inner_traversal(root.right, results)
