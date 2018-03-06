#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-6 下午7:45
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
    def inorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, root, result):
        if not root:
            return

        # 先遍历左子树
        self.dfs(root.left, result)
        # 访问根结点
        result.append(root.val)
        # 再遍历右子树
        self.dfs(root.right, result)

    """
    方法2：迭代
    其实就是用一个栈来模拟递归的过程。所以算法时间复杂度也是O(n)，空间复杂度是栈的大小O(logn)
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        if not root:
            return result

        stack = []
        head = root  # 辅助结点
        # 第一个判断表示左边分支还没访问完，
        # 第二个判断表示向上返回的时候stack里面还存在访问过的根结点，此时root为None，开始访问右分支
        while head or len(stack) > 0:
            if head:  # 当前结点不为 None, 继续看左子树
                # 当前根结点入栈
                stack.append(head)
                # 开始访问左子树
                head = head.left

            else:  # 当前左结点为空
                pre_head = stack.pop()
                result.append(pre_head.val)
                # 开始访问右子树
                head = pre_head.right

        return result
