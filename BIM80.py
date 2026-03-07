# 描述
# 假设你有一个数组prices，长度为n，其中prices[i]是股票在第i天的价格，请根据这个价格数组，返回买卖股票能获得的最大收益
# 1.你可以买入一次股票和卖出一次股票，并非每天都可以买入或卖出一次，总共只能买入和卖出一次，且买入必须在卖出的前面的某一天
# 2.如果不能获取到任何利润，请返回0
# 3.假设买入卖出均无手续费

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param prices int整型一维数组 
# @return int整型
#
from typing import List

# 枚举部分测试用例
class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        # write code here
        # 剪枝
        if len(prices) <= 1:
            return 0
        if len(prices) == 2:
            return max(0,prices[1]-prices[0])
        if len(prices) == 3:
            return max(0,prices[1]-prices[0],prices[2]-prices[0],prices[2]-prices[1])

# 暴力枚举
class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        # write code here
        max_profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                profit = prices[j]-prices[i]
                max_profit = max(profit,max_profit)
        return max_profit



        
