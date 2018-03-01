#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-1 上午11:02
"""


class Solution(object):
    def findMin(self, nums):
        """
        0　　1　　2　　 *4　　5　　6　　7*
        7　　0　　1　　 *2　　4　　5　　6*
        6　　7　　0　　 *1　　2　　4　　5*
        5　　6　　7　　 *0　　1　　2　　4*
        *4　　5　　6　　 7* 　0　　1　　2
        *2　　4　　5　　 6*　　7　　0　　1
        *1　　2　　4　　 5*　　6　　7　　0

        二分搜索法的关键在于获得了中间数后，判断下面要搜索左半段还是右半段

        A[mid] > A[low]，右半区间查找。
        A[mid] < A[low]，左半区间查找。
        A[mid] = A[low]，出现这种情况，我们跳过 low，重新查找，譬如[2,2,2,1]，A[mid] = A[low]都为2，
                         这时候我们跳过 low，使用[2,2,1]继续查找。

        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        low, high = 0, len(nums) - 1

        while low < high - 1:
            if nums[low] < nums[high]:  # 已经有序
                return nums[low]

            mid = (low + high) // 2

            if nums[mid] < nums[low]:  # 在左边
                high = mid
            elif nums[mid] > nums[low]:  # 在右边
                low = mid
            else:  # low == mid 出现重复值，跳过最低值 low + 1
                low += 1

        return min(nums[low], nums[high])
