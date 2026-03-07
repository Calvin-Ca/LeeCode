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
        # 观察枚举过程中是否存在重复计算
        # 0,prices[1]-prices[0]二者的最大值 其实就是 到前一天能卖出的最大值
        # prices[2]-prices[0],prices[2]-prices[1] 的最大值 其实就是 用当天减去历史最小值的结果
        # 由此想到维护两个变量：到前一天能卖出的最大值（当天不卖），历史最小值（当天卖需要减去它）

# 暴力枚举
class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        # write code here
        # 时间复杂度o(n2),空间o(1)
        # 开变量的时机或者说场景：求最值、累计结果、记录历史状态、动态更新最优解
        max_profit = 0 # 由于并不关心所有买入卖出方案的利润（这样得用数组）,而只关心最大值,所以维护一个最大值变量,并在遍历过程中就实时更新它
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                profit = prices[j]-prices[i]
                max_profit = max(profit,max_profit)
        return max_profit

class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        # write code here
        if len(prices) == 0:
            return 0
        min_price = prices[0]   # 到第i天出现的最低价（不包括第i天，意思是第i天不买），起始值为第一天的
        max_profit = 0  # 到第i天能卖出的最大值

        for price in prices[1:]: # 卖只能从第二天开始
            # 遍历每一天，更新当前最低价，更新当前能卖出的最大值
            # 第二天选择卖，第二天的最大值为price - min_price
            # 第二天选择不卖，最大值为前一天的max_profit
            max_profit = max(max_profit, price - min_price)  
            min_price = min(min_price, price)
        return max_profit



        
