#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-11-28 下午8:47
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False

        slide_window_len = 1
        while slide_window_len <= len(s) // 2:
            if len(s) % slide_window_len != 0:  # 如果字符串长度不是匹配窗的整数倍, 匹配窗长度加1, continue
                slide_window_len += 1
                continue

            slide_window = s[:slide_window_len]
            s_start = slide_window_len
            s_end = s_start + slide_window_len
            is_repeated = True
            while s_end <= len(s):
                if slide_window != s[s_start:s_end]:
                    is_repeated = False
                    break
                s_start = s_end
                s_end = s_start + slide_window_len

            if is_repeated:
                return True
            slide_window_len += 1

        return False

print Solution().repeatedSubstringPattern("bacbacbac")
