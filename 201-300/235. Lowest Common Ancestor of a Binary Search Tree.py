#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-19 下午7:54
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor1(self, root, p, q):
        """
        注意使用BST的性质！
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # 如果p，q在root同侧
        while (p.val - root.val) * (q.val - root.val) > 0:
            if p.val < root.val:  # 都在左侧
                root = root.left
            else:  # 都在右侧
                root = root.right

        # p、q 在root两侧或其中一个和root相等，则直接返回root
        return root

    def lowestCommonAncestor(self, root, p, q):
        """
        注意使用BST的性质！

        方法二：递归
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 如果 q p 在左子树
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # 如果 q p 在右子树
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # 如果再两边，直接返回 root
        return root
