#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-6 下午8:09
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
    def postorderTraversal1(self, root):
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
        # 再遍历右子树
        self.dfs(root.right, result)
        # 访问根节点
        result.append(root.val)

    """
    方法2：迭代
    其实就是用一个栈来模拟递归的过程。所以算法时间复杂度也是O(n)，空间复杂度是栈的大小O(logn)
    
    后续的顺序是左-右-根，所以 **当一个节点值被取出来时，它的左右子节点要么不存在，要么左右子节点已经被访问过了**。
    我们先将根结点压入栈，然后定义一个辅助结点node，while循环的条件是栈不为空，在循环中，
    首先将栈顶结点 top 取出来，如果栈顶结点没有左右子结点，或者其左子结点是node，或者其右子结点是node的情况下,
    我们将栈顶结点值加入结果res中，并将栈顶元素移出栈，然后将node指向栈顶元素；
    否则的话就看如果右子结点不为空，将其加入栈，再看左子结点不为空的话，就加入栈，注意这里先右后左的顺序是因为栈的后入先出的特点，
    可以使得左子结点先被处理。
    下面来看为什么是这三个条件呢？
    首先如果栈顶元素没有左右子结点的话，说明其是叶结点，而且我们的入栈顺序保证了左子结点先被处理，
    所以此时的结点值就可以直接加入结果res了，然后移出栈，将 node 指向这个叶结点，
    **这样的话 node 每次就是指向前一个处理过并且加入结果res的结点**，那么如果栈顶结点的左子结点或者右子结点是node的话，
    说明其子结点已经加入结果res了，那么就可以处理当前结点(栈顶结点)了
    """
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        if not root:
            return result

        stack = [root]
        node = root  # 辅助结点

        while len(stack) > 0:
            # 取出栈顶结点
            top = stack[-1]
            # 如果 (当前处理的结点没有左右结点) 或者 (当前结点的左结点已经处理）或者（当前结点的右结点已经处理）
            # 因为：1. 如果当前处理的结点没有左右结点说明是叶子结点，直接输出（可以保证左叶子结点先输出）
            #       2. 如果当前结点的左结点已经处理，说明当前结点没有右结点
            #       3. 如果当前结点的右结点已经处理，说明当前结点有左右结点，并且左结点一定已经处理了
            if (not top.left and not top.right) or (top.left == node) or (top.right == node):
                # top 结果加入到 result
                result.append(top.val)
                # 将处理后的结点移除栈，同时 node 指向已经处理后的结点
                node = stack.pop()
            else:  # 存在左结点或右结点
                # 按照栈的处理顺序 FILO，后续遍历先输出左结点，因此先将右结点入栈
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)

        return result
