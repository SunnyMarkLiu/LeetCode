#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
a.将无需序列构建成一个堆，根据升序降序需求选择大顶堆或小顶堆;
b.将堆顶元素与末尾元素交换，将最大元素"沉"到数组末端;
c.重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素，
  反复执行调整+交换步骤，直到整个序列有序。

@author: SunnyMarkLiu
@time  : 18-3-18 上午11:27
"""


def sift_down(arr, start, end):
    root = start
    while True:
        # 从root开始对最大堆调整
        child = 2 * root + 1    # root对应的左子结点
        if child > end:
            break

        # 找出两个child中较大的一个
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1

        if arr[root] < arr[child]:
            # 最大堆小于较大的child, 交换顺序
            arr[root], arr[child] = arr[child], arr[root]

            # 正在调整的节点设置为root
            # 调整完根结点后需要调整子结点
            root = child
        else:
            # 无需调整的时候, 退出
            break


def heap_sort(nums):
    # 创建最大堆
    # 从最后一个有子节点的孩子开始调整最大堆，叶子结点已经满足堆的要求
    first = len(nums) // 2 - 1  # 最后一个非叶子结点
    for start in range(first, -1, -1):
        sift_down(nums, start, len(nums) - 1)

    # 堆排序
    # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
    for end in range(len(nums) - 1, 0, -1):
        # 交换当前最大的根元素和当前最后一个元素
        nums[0], nums[end] = nums[end], nums[0]
        sift_down(nums, 0, end - 1)

    return nums


l = [4, 6, 8, 5, 9]
print(l)
heap_sort(l)
print(l)
