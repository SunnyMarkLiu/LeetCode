#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
4 sum 问题转化为 3 sum 问题
同时注意时间复杂度而进行的边界检查

@author: MarkLiu
@time  : 17-10-31 下午8:05
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        solutions = []
        nums.sort()  # 注意先排序
        max_num = nums[-1]
        min_num = nums[0]

        if 4 * min_num > target or 4 * max_num < target:  # 最大值最小值的边间检测
            return []

        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # 去除重复数据
                continue

            if nums[i] + 3 * max_num < target:  # nums[i] 太小了
                continue
            if nums[i] + 3 * min_num > target:  # nums[i] 太大了
                break

            tmp_target = target - nums[i]
            if i == 0:
                tmp_nums = nums[1:]
            elif i == len(nums) - 1:
                tmp_nums = nums[:-1]
            else:
                tmp_nums = nums[:i]
                tmp_nums.extend(nums[i + 1:])

            # three sum problem
            for j in xrange(len(tmp_nums) - 2):
                if j > 0 and tmp_nums[j] == tmp_nums[j - 1]:  # 去除重复数据
                    continue

                l_index, r_index = j + 1, len(tmp_nums) - 1
                while l_index < r_index:
                    s = tmp_nums[j] + tmp_nums[l_index] + tmp_nums[r_index]
                    if s < tmp_target:
                        l_index += 1
                    elif s > tmp_target:
                        r_index -= 1
                    else:
                        s = [nums[i], tmp_nums[j], tmp_nums[l_index], tmp_nums[r_index]]
                        s.sort()
                        if s not in solutions:
                            solutions.append(s)
                        while l_index < r_index and tmp_nums[l_index] == tmp_nums[l_index + 1]:  # 去除重复数据
                            l_index += 1
                        while l_index < r_index and tmp_nums[r_index] == tmp_nums[r_index - 1]:
                            r_index -= 1

                        l_index += 1
                        r_index -= 1

        return solutions

print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
