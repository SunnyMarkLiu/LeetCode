#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-8 上午10:32
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        result = []
        self.post_order(root, result)
        return sum(result)

    def post_order(self, root, result):
        # 访问到叶子结点的下一个结点
        if not root:
            return 0

        # 访问左子树
        left = self.post_order(root.left, result)
        # 访问右子树
        right = self.post_order(root.right, result)

        result.append(abs(left - right))

        return left + right + root.val
