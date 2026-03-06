# 描述
# 你是一个经验丰富的小偷，准备偷沿街的一排房间，每个房间都存有一定的现金，
# 为了防止被发现，你不能偷相邻的两家，即，如果偷了第一家，就不能再偷第二家；
# 如果偷了第二家，那么就不能偷第一家和第三家。
# 给定一个整数数组nums，数组中的元素表示每个房间存有的现金数额，
# 请你计算在不被发现的前提下最多的偷窃金额。

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
class Solution:
    def rob(self , nums: List[int]) -> int:
        # write code here

        # 定义状态，偷到第i个房子时的最大金额dp[i]
        # 状态转移：dp[i] = max(dg[i-2]+num[i],dg[i-1]) # 要么偷，要么不偷num[i]
        # 剪枝
        if len(nums) <= 0:
            return 0
        n = len(nums)
        dp = [-1] * (n+1) # dp[i] 抢到第i家时的最大值
        def dfs(cur):
            # 返回抢到第cur家时抢到的最大值
            if cur == 1:
                return nums[0]
            if cur == 2:
                return max(nums[0],nums[1])
            if dp[cur] != -1:
                return dp[cur]
            dp[cur] = max(dfs(cur-1),nums[cur-1]+dfs(cur-2))
            return dp[cur]
            # dp[3]开始才有值
        
        return dfs(n)  # 抢到第n家时的最大值，第n家已经做出决策