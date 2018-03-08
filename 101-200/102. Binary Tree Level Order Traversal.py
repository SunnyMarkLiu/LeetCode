#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-8 上午11:38
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    """
    方法1：递归
    算法的时间复杂度是O(n), 而空间复杂度则是递归栈的大小，即树的深度，O(logn)
    """
    def levelOrder1(self, root):
        """
        层序遍历：递归，前序遍历的方式扫描树，保存层序遍历的结果
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        results = []
        self.bfs(root, results, 0)
        return results

    def bfs(self, root, results, level):
        """
        level　记录当前遍历的层
        """
        if not root:
            return

        if level == len(results):  # 遍历新的当前层
            current = [root.val]
            results.append(current)
        else:  # 遍历到前面几层(之前遍历过)
            level_result = results[level]
            level_result.append(root.val)
            results[level] = level_result

        # 遍历下一层
        self.bfs(root.left, results, level + 1)
        self.bfs(root.right, results, level + 1)

    """
    方法2：迭代
    其实就是用一个栈来模拟递归的过程。所以算法时间复杂度也是O(n)，空间复杂度是栈的大小O(logn)
    
    我们要把各个层的数分开，存到一个二维向量里面，大体思路还是基本相同的，建立一个queue，
    然后先把根节点放进去，这时候找根节点的左右两个子节点，这时候去掉根节点，
    此时queue里的元素就是下一层的所有节点，用一个for循环遍历它们，然后当前层遍历的结果存到一个一维向量里，
    遍历完之后再把这个一维向量存到二维向量也就是最终的结果里，以此类推，可以完成层序遍历
    
    """
    def levelOrder(self, root):
        """
        前序遍历的方式扫描树，保存层序遍历的结果

        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result

        current_level = [root]
        while current_level:
            cur_level_res = []
            next_level_nodes = []

            for node in current_level:  # 遍历当前结点
                cur_level_res.append(node.val)
                if node.left:
                    next_level_nodes.append(node.left)

                if node.right:
                    next_level_nodes.append(node.right)

            current_level = next_level_nodes
            result.append(cur_level_res)

        return result
