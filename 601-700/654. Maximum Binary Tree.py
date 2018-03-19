#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-19 上午11:40
"""
import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def find_max_index(self, nums):
        """
        找到数组的最大值
        """
        max_num = -sys.maxsize
        for i, num in enumerate(nums):
            if num > max_num:
                max_num = num
                max_index = i

        return max_index

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) == 0:
            return None

        # 构建根结点
        max_index = self.find_max_index(nums)
        root = TreeNode(nums[max_index])

        # 构建左子树
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        # 构建右子树
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])

        return root
