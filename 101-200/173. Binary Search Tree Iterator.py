#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-19 下午4:48
"""


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []

        # 前序遍历直到左结点为None的结点
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        return the next smallest number in the BST
        :rtype: int
        """
        if self.hasNext():
            # 栈顶保存最小值
            min_node = self.stack.pop()
            # 如果最小值结点有右子树，将右子树根结点及其左结点入栈
            if min_node.right:
                tmp = min_node.right
                while tmp:
                    self.stack.append(tmp)
                    tmp = tmp.left

            return min_node.val

        return None

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
