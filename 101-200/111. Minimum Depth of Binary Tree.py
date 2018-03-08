#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-8 下午3:57
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        # 如果当前结点的左右子结点均存在，则递归选择左子树和右子树的最小值，同时注意加上当前的结点 + 1
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        # 如果当前结点只存在一个左右结点，选择有叶子结点的分支，即 depth 较大的，同时注意加上当前的结点 + 1
        return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
