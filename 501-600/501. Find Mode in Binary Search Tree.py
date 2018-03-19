#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-19 下午5:08
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.pre_val = None
        self.cur_count = 0  # 记录当前值出现的次数
        self.max_count = -1  # 记录出现次数最多

    def findMode(self, root):
        """
        利用中序遍历
        :type root: TreeNode
        :rtype: List[int]
        """
        modes = []
        self.pre_val = root
        self.inner_traversal(root, modes)
        return modes

    def inner_traversal(self, root, modes):
        if not root:
            return

        # 递归左子树
        self.inner_traversal(root.left, modes)
        # 访问根结点
        self.cur_count = self.cur_count + 1 if root.val == self.pre_val.val else 1

        if self.cur_count == self.max_count:  # 如果存在多个 mode
            modes.append(root.val)

        elif self.cur_count > self.max_count:
            self.max_count = self.cur_count
            # modes 数组清空
            modes.clear()
            modes.append(root.val)

        self.pre_val = root
        # 递归右子树
        self.inner_traversal(root.right, modes)
