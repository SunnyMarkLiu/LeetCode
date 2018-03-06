#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-6 下午6:55
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        先序遍历判断结构和结果是否相等
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.dfs(p, q)

    def dfs(self, p, q):
        if (not p and q) or (p and not q):  # p, q 只有一个为 None， [[p0, q1], [p1, q0]]的情况
            return False

        if not p and not q:  # p q都是 None [p0, q0]的情况
            return True

        # [p1, q1] 的情况
        if p.val == q.val:
            # 遍历并检测左子树和右子树
            return self.dfs(p.left, q.left) and self.dfs(p.right, q.right)

        # p q　不为 None,　但 val 不相等
        return False
