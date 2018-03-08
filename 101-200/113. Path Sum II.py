#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-8 上午9:43
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def dfs(self, root, left_value, ret_stack, results):
        ret_stack.append(root.val)
        # 当前结点是叶子结点，判断这个叶子结点的值和 sum 剩下的值是否相等
        if not root.left and not root.right and left_value == root.val:
            # 注意此处不能直接写 ret_stack, 需要 list 创建新对象
            results.append(list(ret_stack))

        # 前序遍历左子树
        if root.left:
            self.dfs(root.left, left_value - root.val, ret_stack, results)
        # 前序遍历右子树
        if root.right:
            self.dfs(root.right, left_value - root.val, ret_stack, results)

        ret_stack.pop()

    def pathSum1(self, root, sum):
        """
        递归的形式
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        results = []
        ret_stack = []
        self.dfs(root, sum, ret_stack, results)
        return results

    def pathSum(self, root, sum):
        """
        迭代的形式
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        results = []
        stack = [(root, sum - root.val, [root.val])]

        while stack:
            cur_node, left_sum, result = stack.pop()

            # 到达叶子结点
            if not cur_node.left and not cur_node.right and left_sum == 0:
                results.append(result)

            if cur_node.left:
                stack.append((cur_node.left, left_sum - cur_node.left.val, result + [cur_node.left.val]))

            if cur_node.right:
                stack.append((cur_node.right, left_sum - cur_node.right.val, result + [cur_node.right.val]))

        return results
