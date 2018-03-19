#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-19 上午11:55
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root):
        """
        递归找到每层最左边的下标和最右边的下标(leftmost node and rightmost node in each level)
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        level_left_most = []    # 记录每层最左边的下标
        level_right_most = []   # 记录每层最右边的下标

        self.dfs(root, 0, 1, level_left_most, level_right_most)

        max_width = 0
        for level in range(len(level_left_most)):
            level_width = level_right_most[level] - level_left_most[level] + 1
            if level_width > max_width:
                max_width = level_width
        return max_width

    def dfs(self, root, level, cur_node_index, level_left_most, level_right_most):
        """
        :param root:
        :param level: 属于哪一层
        :param cur_node_index:      当前层当前结点的下标
        :param level_left_most:     保存最左边非空结点的下标
        :param level_right_most:    保存最右边非空结点的下标
        """
        if not root:
            return

        # 递归遍历寻找最左边的结点
        if len(level_left_most) == level:   # 遍历新的level
            level_left_most.append(cur_node_index)
            level_right_most.append(cur_node_index)
        else:   # 还是遍历当前level，更新最右边的结点
            level_right_most[level] = cur_node_index

        # 计算此时的宽度
        self.dfs(root.left,  level + 1, 2*cur_node_index,   level_left_most, level_right_most)
        self.dfs(root.right, level + 1, 2*cur_node_index+1, level_left_most, level_right_most)
