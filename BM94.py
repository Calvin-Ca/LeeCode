# 描述
# 给定一个整形数组arr，已知其中所有的值都是非负的，将这个数组看作一个柱子高度图，
# 计算按此排列的柱子，下雨之后能接多少雨水。(数组以外的区域高度视为0)
# 任何一个位置 i 能接多少水，取决于它左边最高的柱子和右边最高的柱子中的“较小值”
from typing import List
class Solution:
    def maxWater(self , arr: List[int]) -> int: 
        # write code here 
        # 剪枝
        if len(arr) < 3:
            return 0
        total_water = 0
        for i in range(1,len(arr)-1):
            max_left = 0
            max_right = 0
            for j in range(i,-1,-1): # 一直到0
                max_left = max(max_left,arr[j])
            for j in range(i,len(arr)):
                max_right = max(max_right,arr[j])
            total_water += min(max_left,max_right)
        return total_water
    
class Solution1:
    def maxWater(self, arr: list[int]) -> int:
        if not arr or len(arr) < 3:
            return 0
        # 动态维护左右最大高度，并始终处理较低的一侧
        n = len(arr)
        left, right = 0, n - 1
        left_max, right_max = 0, 0  # 维护两个变量，保存的是值而不是索引
        res = 0
        # [1,2,3]
        while left < right:
            # 更新左右两边的已知最高门槛
            left_max = max(left_max, arr[left])         # left_max 是 arr[left]位置 之前的最大值
            right_max = max(right_max, arr[right])
            
            # 谁矮移动谁，因为水位受限于“短板”
            if left_max < right_max:
                # 左边最高比右边最高矮，左边这格能存多少水已经确定了
                res += left_max - arr[left]   # 当前水位储水量始终取决于两边矮的那一个
                left += 1
            else:
                # 右边同理
                res += right_max - arr[right]
                right -= 1
                
        return res

class Solution1:
    def maxWater(self, arr: list[int]) -> int:
        # 剪枝
        if len(arr) < 3:
            return 0
        # 维护两个变量，表示两边指针范围内的最大值，left_max，right_max
        # 维护两个指针 left，right用于遍历，移动哪个的条件为left_max和right_max 哪个小
        left,right = 0,len(arr)-1
        left_max,right_max = 0,0
        total = 0

        while left < right:
            left_max = max(left_max,arr[left])
            right_max = max(right_max,arr[right])
            # 移动矮的一边的指针，并可得到指针移动后下一位置的储水量
            if left_max < right_max:
                res += left_max - arr[left] # 注意由于left_max统计的是left之前的，所以这里直接减去arr[left]即可
                left += 1
            else:
                res += right_max - arr[right]
                right -= 1
        return res




if __name__ == "__main__":
    # arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    arr = [8,4,3,7,5]
    res = Solution1().maxWater(arr=arr)
    pass