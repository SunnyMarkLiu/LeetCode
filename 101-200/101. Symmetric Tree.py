#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-9 下午4:31
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric1(self, root):
        """
        方法１：递归
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.subtree_check(root.left, root.right)

    def subtree_check(self, left_node, right_node):
        """
        递归判断 left, right 构成的树是否是对称的
        """
        if not left_node and not right_node:  # left 和 right 都是 None
            return True

        if not left_node or not right_node:  # left 和 right 只有一个是 None，不对称
            return False

        if left_node.val != right_node.val:  # left 和 right 不为空，但值不相等，不对称
            return False

        # 递归检测
        return self.subtree_check(left_node.left, right_node.right) and self.subtree_check(left_node.right,
                                                                                           right_node.left)

    def isSymmetric(self, root):
        """
        方法2：利用栈
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [root.left, root.right]

        while stack:
            right_node = stack.pop()
            left_node = stack.pop()

            if not right_node and not left_node:
                continue    # 此处注意 continue

            if not right_node or not left_node:
                return False

            if right_node.val != left_node.val:
                return False

            # 当前 pop 出来的两个结点相等
            # 注意入栈的顺序（由 pop 出来的左右结点入手）,对称的入栈
            stack.append(left_node.left)
            stack.append(right_node.right)

            stack.append(left_node.right)
            stack.append(right_node.left)

        return True
