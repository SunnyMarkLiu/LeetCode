# K Sum 问题总结
## K sum问题描述
K sum的求和问题一般是这样子描述的：给你一组N个数字(比如 vector num), 然后给你一个常数(比如 int target) ，我们的goal是在这一堆数里面找到K个数字，使得这K个数字的和等于target。

## 注意事项
注意这一组数字可能有重复项：比如 1 1 2 3 , 求3sum, 然后 target  = 6, 你搜的时候可能会得到两组1 2 3, 1 2 3，1 来自第一个1或者第二个1, 但是结果其实只有一组，所以最后结果要去重。

## 通用解法
```python
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()     # 注意先排序
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results
    
    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return
        
        # solve 2-sum
        if N == 2:
            l,r = 0,len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):   # careful about range
                if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return
    
```
