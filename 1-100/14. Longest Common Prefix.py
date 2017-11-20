#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
先按照字符串数组的长度排序, 从最小长度的字符串入手进行检测

@author: MarkLiu
@time  : 17-11-20 上午11:24
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        beat 77.20%
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        lens = [len(s) for s in strs]
        str_len_zip = zip(lens, strs)
        str_len_zip.sort()
        shortest = str_len_zip[0][1]
        s_len = len(shortest)
        longest = ''
        for i in range(s_len):
            compare = shortest[:s_len - i]
            found = False
            for s in strs:
                if not s.startswith(compare):
                    found = False
                    break
                found = True

            if found:
                longest = compare
                break

        return longest


print Solution().longestCommonPrefix(['asde', 'asdef', 'asdd'])
