#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-8 下午7:57
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        # 从以　root 为起点计算，以及从ｒｏｏｔ的左右子结点开始的数量之和
        return self.dfs(root, sum, 0) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, root, sum, cur_sum):
        """
        当前 root　结点为起点，满足要求的数目，需要一直走到叶子结点，因为中间可能存在正负值
        """
        if not root:
            return 0

        cur_sum += root.val
        if cur_sum == sum:
            cur_result = 1
        else:
            cur_result = 0

        # 当前以结点开始以及当前结点的左右子结点开始满足要求的数目
        return cur_result + self.dfs(root.left, sum, cur_sum) + self.dfs(root.right, sum, cur_sum)
