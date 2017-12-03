#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-12-3 下午3:51
"""


class Solution(object):
    def reverse(self, left, right, s):
        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp

            left += 1
            right -= 1

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        left = right = 0
        while right < len(s):
            # 获取不包含空格的有效的字符串
            while right < len(s) and s[right] != ' ':
                right += 1

            print left, right
            self.reverse(left, right - 1, s)
            right += 1
            left = right

        return ''.join(s)

    def reverseWords2(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(sub_s[::-1] for sub_s in s.split(' '))


print Solution().reverseWords("Let's take LeetCode contest")
