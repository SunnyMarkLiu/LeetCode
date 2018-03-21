#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-21 下午4:19
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(0, 0, len(inorder) - 1, preorder, inorder)

    def helper(self, preStart, inStart, inEnd, preorder, inorder):
        if preStart > len(preorder) - 1 or inStart > inEnd:
            return None

        root = TreeNode(preorder[preStart])

        # 当前根结点再中序遍历中的位置
        inIndex = inorder.index(root.val)

        # 构造左子树
        root.left = self.helper(preStart + 1, inStart, inIndex - 1, preorder, inorder)
        # 构造右子树，注意preorder开始的位置：上一次preStart + 左子树再前序遍历的长度
        root.right = self.helper(preStart + (inIndex - inStart + 1), inIndex + 1, inEnd, preorder, inorder)

        return root
