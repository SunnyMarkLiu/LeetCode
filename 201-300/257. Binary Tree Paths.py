#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-8 上午10:22
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        results = []
        self.dfs(root, [], results)
        return results

    def dfs(self, root, cur_result, results):
        if not root:
            return

        cur_result.append(str(root.val))
        if not root.left and not root.right:
            results.append('->'.join(list(cur_result)))

        if root.left:
            self.dfs(root.left, cur_result, results)

        if root.right:
            self.dfs(root.right, cur_result, results)

        cur_result.pop()
