#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-20 下午1:10
"""


class Solution:
    def generateParenthesis(self, n):
        """
        思路：向string 中插入( 和 )，每插入一个就减1。 那么如何保证这个combination 是正确的呢？
            插入数量不超过n
            可以插入 ） 的前提是 ( 的数量大于 ）

        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return []

        results = []
        self.helper('', n, n, results)
        return results

    def helper(self, cur_parentheses, left, right, results):
        """
        left 和 right 记录左右括号剩下的数目
        """
        # 左括号和右括号都插入完成
        if left == 0 and right == 0:
            results.append(cur_parentheses)
            return

        # 插入左括号的前提是，left > 0
        if left > 0:
            self.helper(cur_parentheses + '(', left - 1, right, results)

        # 插入右括号的前提是，right > 0, 并且左括号的数量大于右括号的数量
        if right > 0 and right > left:
            self.helper(cur_parentheses + ')', left, right - 1, results)
