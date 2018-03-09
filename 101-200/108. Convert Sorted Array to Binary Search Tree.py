#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
根节点应该是有序数组的中间点，从中间点分开为左右两个有序数组，在分别找出其中间点作为原中间点的左右两个子节点，
这不就是是二分查找法的核心思想么。所以这道题考的就是二分查找法

@author: SunnyMarkLiu
@time  : 18-3-9 上午11:27
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST1(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) == 0:
            return None

        ln = len(nums)
        if ln == 1:
            return TreeNode(nums[0])

        # 首先找到排序数组的中间值
        root = TreeNode(nums[ln // 2])
        # 创建左子树
        root.left = self.sortedArrayToBST1(nums[:ln // 2])  # 注意此处存在的问题是 list 的分片处理，空间复杂度较高，考虑采用下标的方式进行改进
        # 创建右子树
        root.right = self.sortedArrayToBST1(nums[ln // 2 + 1:])

        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) == 0:
            return None

        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums, low, high):

        if low > high:
            return None

        mid = low + (high - low) // 2

        # 创建当前根结点
        node = TreeNode(nums[mid])
        # 创建左右子树
        node.left = self.dfs(nums, low, mid - 1)
        node.right = self.dfs(nums, mid + 1, high)
        return node
