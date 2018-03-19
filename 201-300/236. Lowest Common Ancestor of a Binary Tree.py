#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-19 下午8:25
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:  # 没找到，返回 None
            return None

        if root == p or root == q:
            return root

        # 递归查找左子树使得 root == p或q，若找到则返回该root
        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)

        # 如果左右子树都查到，说明两边都有，则返回其根结点
        if left_result and right_result:
            return root

        # 如果左子树查到的结果不为空，右子树查到的结果为空，则 p q 在左子树
        # 如果右子树查到的结果不为空，左子树查到的结果为空，则 p q 在右子树
        return left_result if left_result else right_result
