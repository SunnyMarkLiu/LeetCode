#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-6 上午9:35
"""


class Solution(object):
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 　统计每个字符出现的次数，如果出现偶数则对半分到左右两边，如果是奇数，选取奇数最大的放中间
        char_count = {}
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1

        max_odd = 1
        max_pal_len = 0
        has_max_odd = False

        for word in char_count:
            if char_count[word] % 2 == 0:  # 字符出现偶数次
                max_pal_len += char_count[word]
            else:  # 字符出现奇数次
                if char_count[word] >= max_odd:
                    has_max_odd = True
                    max_pal_len += max_odd - 1
                    max_odd = char_count[word]
                else:
                    max_pal_len += char_count[word] - 1

        # 加上中间的最大奇数次
        if has_max_odd:
            max_pal_len += max_odd

        return max_pal_len

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_set = set()

        for c in s:
            if c in word_set:
                word_set.remove(c)  # 删除偶数次数
            else:  # 增加奇数次数
                word_set.add(c)

        # word_set 中剩下奇数次的字符
        odd = len(word_set)
        left_odd = 0 if odd == 0 else odd - 1  # 此处 -1　表示保留一个奇数的字符到中间

        return len(s) - left_odd
