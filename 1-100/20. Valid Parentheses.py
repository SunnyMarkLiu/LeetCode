#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
1. 用栈来操作，将所有的字符依次入栈，当栈顶的括号和正要入栈的括号匹配时将栈顶的括号弹出且不入栈，否则入栈新的括号。
   最后，只有当栈里没有括号时，才表明输入是有效的。

2. 实际上，通过观察可以发现：如果正要入栈的是右括号，而栈顶元素不是能与之消去的相应左括号，那么该输入字符串一定是无效的。
   于是，可以大大加快判断过程。

@author: MarkLiu
@time  : 17-11-21 下午8:16
"""


class Solution(object):
    def isValid2(self, s):
        """
        beat 32.85%
        :type s: str
        :rtype: bool
        """
        stack = []
        # 括号匹配可以通过字典键值对来匹配
        par_map = {')': '(',
                   ']': '[',
                   '}': '{'}
        for c in s:
            # 新入栈的字符需要进行匹配
            if len(stack) and c in par_map and par_map[c] == stack[-1]:  # 所要匹配的括号和栈顶的元素相等, 匹配成功
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0

    def isValid(self, s):
        """
        beat 60.91%
        :type s: str
        :rtype: bool
        """
        stack = []
        # 括号匹配可以通过字典键值对来匹配
        par_map = {')': '(',
                   ']': '[',
                   '}': '{'}
        for c in s:
            if c == ']' or c == '}' or c == ')':
                if len(stack) == 0 or stack[-1] != par_map[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0

print Solution().isValid(']')
