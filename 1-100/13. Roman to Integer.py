#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
罗马数字有如下符号：

基本字符	    I	V	X	L	C	D	M
对应阿拉伯数字	1	5	10	50	100	500	1000
计数规则：
- 相同的数字连写，所表示的数等于这些数字相加得到的数，例如：III = 3
- 小的数字在大的数字右边，所表示的数等于这些数字相加得到的数，例如：VIII = 8
- 小的数字，限于（I、X和C）在大的数字左边，所表示的数等于大数减去小数所得的数，例如：IV = 4
- 正常使用时，连续的数字重复不得超过三次
- 在一个数的上面画横线，表示这个数扩大1000倍（本题只考虑3999以内的数，所以用不到这条规则）

其次，罗马数字转阿拉伯数字规则（仅限于3999以内）：
从前向后遍历罗马数字，如果某个数比前一个数小或相等，则加上该数。反之，减去前一个数的两倍然后加上该数

@author: MarkLiu
@time  : 17-11-20 上午10:06
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
        convert_num = char_map[s[0]]
        for i in range(1, len(s)):
            pre, cur = char_map[s[i - 1]], char_map[s[i]]
            if cur <= pre:
                convert_num += cur
            else:
                convert_num += (- 2 * pre + cur)
        return convert_num


print Solution().romanToInt('DCXXI')
