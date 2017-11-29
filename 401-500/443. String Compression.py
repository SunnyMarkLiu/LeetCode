#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
给定 read, write 指针
对字符数组循环 read 记录循环的下标:
    如果 当前字符和下一个字符不同, 则开始记录有多少个该不同的字符, 如果相同则直接继续循环 read
        先 write 位置记录该不同的字符,  write + 1
        利用 anchor 和 read 的位置计算该不同的字符出现的次数
        次数转成字符形, 利用 write 写入, write + 1
        次数写完之后, anchor = read + 1, 用于定位下一个不同的字符

@author: MarkLiu
@time  : 17-11-28 下午9:48
"""


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # anchor 用于定位索要检索的不同的字符的位置
        anchor = write = 0
        for read, c in enumerate(chars):
            # 如果 read 和下一个字符相等, 直接移动 read
            if read + 1 == len(chars) or chars[read + 1] != c:    # 开始出现不同的字符
                # 先记录不同的字符, anchor 是指定的字符
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:   # 出现不知1次
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1

        return write

a = ["a", "b", "b", "b"]
print Solution().compress(a)
print a
