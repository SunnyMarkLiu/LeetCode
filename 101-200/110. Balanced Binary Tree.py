#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-8 下午5:29
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced1(self, root):
        """
        自顶向上的方法：时间复杂度 O(n^2)
        当前结点的左右子树的深度相差 <= 1；
        左子树也要满足上面的条件；
        右子树也要满足上面的条件；
        :type root: TreeNode
        :rtype: bool
        """
        # 空结点也是平衡二叉树
        if not root:
            return True

        left_depth = self.get_subtree_depth(root.left)
        right_depth = self.get_subtree_depth(root.right)

        return abs(left_depth - right_depth) <= 1 and self.isBalanced1(root.left) and self.isBalanced1(root.right)

    def get_subtree_depth(self, root):
        if not root:
            return 0

        # 左右子树的最大值，同时加上当前结点
        return max(self.get_subtree_depth(root.left), self.get_subtree_depth(root.right)) + 1

    def isBalanced(self, root):
        """
        自底向上的方法：时间复杂度 O(n)
        在遍历的时候获取当前结点的深度，满足要求返回其深度，不满足返回 -1
        :param root:
        :return:
        """
        if not root:
            return True

        tree_depth = self.get_node_depth(root)
        # 如果正常取到深度值，则说明满足平衡二叉树条件
        return tree_depth != -1

    def get_node_depth(self, root):
        """
        获取当前结点的深度
        :return:
        """
        if not root:
            return 0

        # 当前结点的左子树的深度
        left_depth = self.get_node_depth(root.left)
        if left_depth == -1:
            return -1

        # 当前结点的右子树的深度
        right_depth = self.get_node_depth(root.right)
        if right_depth == -1:
            return -1

        # 当前结点的左右子树的深度均存在，判断当前结点构成的树是否是平衡二叉树
        if abs(left_depth - right_depth) > 1:
            return -1  # 不满足返回 -1

        # 若满足则返回结点的深度
        return max(left_depth, right_depth) + 1
