#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
回文字符串判断，但只判断字母和数字是否形成回文字符串，标点符号被略过。

使用头尾双指针, 收尾遍历比较字符, 同时注意过滤无效字符
@author: MarkLiu
@time  : 17-11-19 下午3:36
"""


class Solution(object):
    def isPalindrome2(self, s):
        """
        beat 13.46%
        :type s: str
        :rtype: bool
        """
        if (s is None) or (s.strip() == ''):
            return True
        # 1. 过滤无效字符
        new_s = []  # 这里如果以字符串保存会超时，使用数组运行时间会减少
        for i in range(len(s)):
            if ((s[i] >= 'a') and (s[i] <= 'z')) or ((s[i] >= 'A') and (s[i] <= 'Z')) \
                    or ((s[i] >= '0') and (s[i] <= '9')):
                new_s.append(s[i].lower())
        # 2. 头尾指针判断字符是否相等
        for i in range(len(new_s) / 2):
            if new_s[i] != new_s[-(i + 1)]:
                return False
        return True

    def is_legal_str(self, s):
        if ((s >= 'a') and (s <= 'z')) or ((s >= 'A') and (s <= 'Z')) or ((s >= '0') and (s <= '9')):
            return True
        else:
            return False

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if (s is None) or (s.strip() == ''):
            return True

        processed_str_len = 0

        # 头尾指针判断字符是否相等
        i, j = 0, len(s) - 1
        while (i <= j) and processed_str_len < len(s):
            if not self.is_legal_str(s[i]):
                i += 1
                processed_str_len += 1
                continue

            if not self.is_legal_str(s[j]):
                j -= 1
                processed_str_len += 1
                continue

            if s[i].lower() != s[j].lower():
                return False
            if i == j:
                processed_str_len += 1
            else:
                processed_str_len += 2

            i += 1
            j -= 1

        return True


print Solution().isPalindrome('a a')
