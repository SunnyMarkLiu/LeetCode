#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-12-3 下午8:33
"""


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_length = 0
        # 记录出现的最近一次出现的下标
        used_set = {}

        for i in range(len(s)):
            if s[i] in used_set and start <= used_set[s[i]]:
                # 开始的位置,从重复出现的字符所在的下一个位置, start 的位置不必一个一个滑动
                start = used_set[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used_set[s[i]] = i

        return max_length


print Solution().lengthOfLongestSubstring("tmmzuxt")
