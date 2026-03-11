# 描述
# 给定一个数组height，长度为n，每个数代表坐标轴中的一个点的高度，height[i]是在第i点的高度，请问，从中选2个高度与x轴组成的容器最多能容纳多少水
# 1.你不能倾斜容器
# 2.当n小于2时，视为不能形成容器，请返回0
# 3.数据保证能容纳最多的水不会超过整形范围，即不会超过231-1

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param height int整型一维数组 
# @return int整型
#
from typing import List
class Solution:
    def maxArea(self , height: List[int]) -> int:
        # write code here
        if len(height) < 2:
            return 0
        left,right = 0,len(height)-1
        max_area = 0
        
        while left < right:
            area = min(height[right],height[left]) * (right - left)
            max_area = max(max_area,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

from typing import List
class Solution:
    def maxArea(self , height: List[int]) -> int:
        # write code here
        if len(height) < 2:
            return 0
        max_area = 0
        
        # 计算了大量受限于短板且宽度在减小的无效组合
        for i in range(len(height)):
            for j in (i+1,len(height)):
                area = (j-i) * min(height[j],height[i])
                max_area = max(area,max_area)
        return max_area