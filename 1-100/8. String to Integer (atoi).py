#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-12-5 下午8:36
"""


class Solution(object):
    def myAtoi(self, input_str):
        """
        :type input_str: str
        :rtype: int
        """
        # 去除空格
        input_str = input_str.strip()
        if len(input_str) == 0:
            return 0

        max_int = 2147483647
        min_int = -2147483648
        start_index = 0
        result = 0
        flag = 1

        contain_plus = False
        if start_index < len(input_str) and input_str[start_index] == '+':
            start_index += 1
            contain_plus = True

        if start_index < len(input_str) and input_str[start_index] == '-':
            if contain_plus:
                return 0
            flag = -1
            start_index += 1

        for i in range(start_index, len(input_str)):
            if '0' <= input_str[i] <= '9':
                result = result * 10 + ord(input_str[i]) - ord('0')
            else:
                break

        result *= flag
        result = result if result <= max_int else max_int
        result = result if result >= min_int else min_int

        return result


print Solution().myAtoi("+-2")
