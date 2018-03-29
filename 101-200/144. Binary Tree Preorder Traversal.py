#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-6 下午6:58
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    方法1：递归
    算法的时间复杂度是O(n), 而空间复杂度则是递归栈的大小，即树的深度，O(logn)
    """
    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, root, result):
        # 边界条件，访问完叶子结点
        if not root:
            return

        # 先遍历根结点
        result.append(root.val)
        # 遍历左子树
        self.dfs(root.left, result)
        # 遍历右子树
        self.dfs(root.right, result)

    """
    方法2：迭代
    其实就是用一个栈来模拟递归的过程。所以算法时间复杂度也是O(n)，空间复杂度是栈的大小O(logn)
    """
    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        if not root:
            return result

        stack = []
        node = root  # 辅助结点
        # 第一个判断表示左边分支还没访问完，
        # 第二个判断表示向上返回的时候stack里面还存在访问过的根结点，此时root为None，开始访问右分支
        while node or len(stack) > 0:
            if node:
                # 访问当前根结点
                result.append(node.val)
                # 当前根结点入栈
                stack.append(node)
                # 前序遍历左子树
                node = node.left
            else:  # 访问完叶子结点
                # 取出上一次已经访问的根结点
                node = stack.pop()
                # 开始访问右结点
                node = node.right

        return result

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        if not root:
            return result

        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            result.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return result
