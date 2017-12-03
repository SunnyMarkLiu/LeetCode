#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
c:

    if(b==0) return a;
    if(a==0) return b;

    while(b!=0){
        int carry = a&b; //进位值
        a = a^b;         //相加
        b = carry << 1;  //进位
    }
    return a;

由于Python没有无符号右移操作，并且当左移操作的结果超过最大整数范围时，会自动将int类型转换为long类型，因此需要对上述代码进行调整

@author: MarkLiu
@time  : 17-12-3 下午7:32
"""


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a & MAX_INT) ^ MAX_INT)

print Solution().getSum(1, 2)
