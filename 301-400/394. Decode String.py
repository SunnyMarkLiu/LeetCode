#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-5 下午2:54
"""


class Solution(object):
    def decodeString2(self, s):
        """
        使用　stack
        :type s: str
        :rtype: str
        """
        num_stack = []
        str_stack = []
        ans = ''

        i = 0
        while i < len(s):
            # 如果开始为数字
            if s[i].isdigit():
                # 计算数值
                count = 0
                while s[i].isdigit():
                    count = count * 10 + int(s[i])
                    i += 1
                num_stack.append(count)

            elif s[i] == '[':
                # 保存　[　之前的字符
                str_stack.append(ans)
                ans = ''
                i += 1

            elif s[i] == ']':
                # 开始计算匹配的 [] 的 ans
                pre_ans = str_stack.pop()
                cur_count = num_stack.pop()
                # 此处 ans 保留当前 [] 之间完成解析的结果
                pre_ans += ans * cur_count

                # 将新的处理完的结果作为 ans
                ans = pre_ans
                i += 1

            else:
                # 匹配到的是普通字符，将之前的结果拼接上
                ans += s[i]
                i += 1

        return ans

    def decodeString(self, s):
        """
        更清晰的 stack
        :type s: str
        :rtype: str
        """
        stack = []
        current_str = ''
        current_num = 0

        for c in s:
            # 如果是数字
            if c.isdigit():
                current_num = current_num * 10 + int(c)

            elif c == '[':
                # 需要将之前解析的字符串和出现的次数入栈
                stack.append(current_str)
                stack.append(current_num)

                # 重新开始记录
                current_str = ''
                current_num = 0
            elif c == ']':
                previous_num = stack.pop()
                previous_str = stack.pop()
                current_str = previous_str + current_str * previous_num
            else:
                current_str += c

        return current_str


print(Solution().decodeString("2[11[a]2[bc]]"))
