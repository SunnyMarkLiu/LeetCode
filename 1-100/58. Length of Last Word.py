#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-12-1 下午3:53
"""


class Solution(object):
    def lengthOfLastWord2(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = len(s) - 1
        # 去除头部和尾部的空格
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1

        # 开始计数
        last_word_count = 0
        for i in range(left, right + 1, 1):
            if s[i] == ' ':
                last_word_count = 0
            else:
                last_word_count += 1
        return last_word_count

    def lengthOfLastWord(self, s):
        """
        从后往前遍历
        :type s: str
        :rtype: int
        """
        right = len(s) - 1
        while right >= 0 and s[right] == ' ':
            right -= 1

        last_right = right
        while right >= 0:
            if s[right] != ' ':
                right -= 1
            else:
                break
        return last_right - right

print Solution().lengthOfLastWord('  Hello World ')
