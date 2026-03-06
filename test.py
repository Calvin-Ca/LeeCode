class Solution:
    def permuteUnique(self, num: List[int]) -> List[List[int]]:
        num.sort()  # 第一步：必须排序！
        res, path = [], []
        used = [False] * len(num)

        def backtrack():
            if len(path) == len(num):
                res.append(path[:])
                return

            for i in range(len(num)):
                # 如果当前数字已使用，跳过
                if used[i]: continue

                # 核心剪枝：如果当前数字和前一个一样，且前一个还没被使用（说明刚回溯完）
                # 这种情况下，当前数字产生的全排列一定和前一个重复，必须剪掉
                if i > 0 and num[i] == num[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(num[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return res
# 描述
# 给一个01矩阵，1代表是陆地，0代表海洋， 如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。
# 岛屿: 相邻陆地可以组成一个岛屿（相邻:上下左右） 判断岛屿个数。
# 例如：
# 输入
# [
# [1,1,0,0,0],
# [0,1,0,1,1],
# [0,0,0,1,1],
# [0,0,0,0,0],
# [0,0,1,1,1]
# ]
# 对应的输出为3
# (注：存储的01数据其实是字符'0','1')
from typing import List

class Solution:
    def solve(self , grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(i,j):
# 当我们发现一个 1，我们并不知道：
# 这个岛是向哪边延伸的
# 这个格子是不是岛的左边缘 / 右边缘 / 中间  
            if i<0 or j<0 or i > rows-1 or j > cols-1 or grid[i,j]==0:
                return
            grid[i,j] = 0
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i,j] == 1:
                    count += 1
                    # 将相连的陆地全部置为0，避免重复搜索
                    dfs(i,j)
        return count

# 描述
# 输入一个长度为 n 字符串，打印出该字符串中字符的所有排列，
# 你可以以任意顺序返回这个字符串数组。
# 例如输入字符串ABC,则输出由字符A,B,C所能排列出来的
# 所有字符串ABC,ACB,BAC,BCA,CBA和CAB
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 
# @return string字符串一维数组
#
class Solution:
    def Permutation(self , str: str) -> List[str]:
        # write code here
        res = []
        n = len(str)
        if n == 0:
            return res
        
        used = n * [False]
        
        def dfs(str_path):
            if len(str_path) == n:
                res.append(str_path)
                return # 目的是填满path后加入res，因此无需返回值
            for i in range(n):
                if used[i]:
                    continue
                # 注意这里是从str中选数时注意str中相邻的重复
                # used[i-1]==False目的
                # 同一个位置选时，选相同数字代表重复
                # 但不同的位置选时，选相同的数字并不代表重复
                if i>0 and str[i]==str[i-1] and used[i-1]==False:
                    continue
                used[i] = True
                str_path += str[i]
                # if 
                dfs(str_path)
                str_path = str_path[:-1]
                used[i] = False

        dfs('') # 递归往字符串加字符
        return res

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 the n
# @return int整型
#
class Solution:
    def Nqueen(self , n: int) -> int:
        if n <= 0:
            return 0
        
        cols = [False] * n
        # diag1中的bool值代表主对角线差相同的元素所在对角线是否被占领
        diag1 = [False] * (2 * n)   # row - col + n
        diag2 = [False] * (2 * n)   # row + col
        
        count = 0
        
        def dfs(row):
            nonlocal count
            
            if row == n:
                count += 1
                return
            
            for col in range(n):
                # 在对第row行做决策时，每一列都看一下
                # row - col + n代表某条对角线（差为固定值的所有元素）
                if cols[col] or diag1[row - col + n] or diag2[row + col]:
                    continue
                # 采用当前列并向更深层传递
                cols[col] = True
                diag1[row - col + n] = True
                diag2[row + col] = True
                dfs(row + 1)
                
                # 释放当前列，因为其它行也可以用
                cols[col] = False
                diag1[row - col + n] = False
                diag2[row + col] = False
        
        dfs(0)
        return count

class Solution:
    def Nqueen(self , n: int) -> int:
        count = 0
        if n<=0:
            return count
        # 回溯记录
        used_cols = [False]*n  # 记录在某行选择皇后位置时某列是否被占
        used_diag1 = [False] * (2*n-1) # 记录在某行选择皇后位置时，某列所处对角线是否有皇后了（根据索引差是否相同）
        used_diag2 = [False] * (2*n-1)
        def dfs(row):
            if row == n:
                count += 1
                return
            for i in range(cols):
                # 注意我只需要保证row-i+n索引不越used_diag1的界就行，本身它们就是一一对应的
                if used_cols[i] == True or used_diag1[row-i+n] == True or used_diag2[row+i] == True:
                    continue
                used_cols[i],used_diag1[row-i+n],used_diag2[row+i] = True,True,True
                dfs(row+1)
                used_cols[i],used_diag1[row-i+n],used_diag2[row+i] =False,False,False
                
        # 不用递归具体选择方案的原因在于问题只需要返回方案数量
        dfs(0) # 这里的0代表行索引，因为是逐行选择皇后的
        return count

# 给出n对括号，请编写一个函数来生成所有的由n对括号组成的合法组合。
# 例如，给出n=3，解集为：
# "((()))", "(()())", "(())()", "()()()", "()(())"
class Solution:
    def generateParenthesis(self , n: int) -> List[str]:
        # write code here
        res = []
        if n <= 0:
            return res
        used_left = 0
        used_right = 0
        
        def dfs(path):
            if len(path) == 2*n:
                res.append(path)
                return
            for i in range(2*n):
                if used_left==n or used_right==n or used_left<used_right:
                    continue
                

                return
            
        dfs('')
        return res

# 描述
# 给定一个 n 行 m 列矩阵 matrix ，矩阵内所有数均为非负整数。 
# 你需要在矩阵中找到一条最长路径，使这条路径上的元素是递增的。
# 并输出这条最长路径的长度。
# 这个路径必须满足以下条件：

# 1. 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外。
# 2. 你不能走重复的单元格。即每个格子最多只能走一次。
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 递增路径的最大长度
# @param matrix int整型二维数组 描述矩阵的每个数
# @return int整型
#
class Solution:
    def solve(self , matrix: List[List[int]]) -> int:
        # write code here
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        # 动态规划的记忆变量
        # 元素含义：从dp[i][j]出发的最长递增路径，初始值0代表未计算
        # 作用：避免对一个格子进行重复计算，解决重叠子问题
        dp = [[0] * cols for _ in range(rows)]
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c):
            if dp[r][c] != 0:
                return dp[r][c]
            
            max_len = 1  # 至少包含自己
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] > matrix[r][c]:
                        # 当前格子的最长递增路径=相邻格子能走的最长递增路径+1
                        max_len = max(max_len, 1 + dfs(nr, nc))
            
            dp[r][c] = max_len
            return max_len
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))
        
        return res

class Solution:
    def solve(self , matrix: List[List[int]]) -> int:
        # write code here
        ### 变量
        # res：整数，直接保存最长递增路径的长度
        # dynamicplan：二维数组，用来保存从每个位置出发能走的最长递增路径
        # directions:行走方向
        # 递归：当周围存在元素大于当前位置时，当前格子的最长递增路径 = 邻居的最长递增路径 + 1
        # 特殊情况处理
        res = 0
        rows,cols = len(matrix),len(matrix[0])
        if rows==0 or cols==0:
            return res
        directions = ([0,1],(0,-1),(-1,0),(1,0))
        dynamicplan_memory = [[0]*cols for _ in range(rows)]

        # 返回指定位置的最长递增路径
        def dfs(row,col):
            # 终止条件：到了一个已经计算过的位置
            # 首次调用dfs肯定不会执行
            if dynamicplan_memory[row][col] != 0:
                return dynamicplan_memory[row][col]
            
            max_len = 1 #只要有一个元素就有一个起码的最长递增路径

            # 递归关系：
            # 可以向周围走，当前格子的max_len = 1+dfs(row,col)
            # 不能向周围走，0
            for d_row,d_col in directions:
                next_row,next_col = row+d_row,col+d_col
                # 先判断是否越界
                if 0<=next_row<rows and 0<=next_col<cols:
                    if matrix[row][col]<matrix[next_row][next_col]:
                        # dynamicplan_memory[row][col] = 1+dfs(row+i,col+j)
                        max_len = max(max_len,1+dfs(next_row,next_col))
            dynamicplan_memory[row][col] = max_len # 在这个层级的最大长度   

            return max_len

        for i in range(rows):
            for j in range(cols):
                # 当前格子的最长递增路径
                cur_max = dfs(i,j)
                # 和历史的最长递增路径作比较，并更新res
                res = max(res,cur_max)
        return res

# 描述
# 大家都知道斐波那契数列，现在要求输入一个正整数 n ，请你输出斐波那契数列的第 n 项。
# 斐波那契数列是一个满足 
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#
# 1,1,2,3,5,8,13,...
class Solution:
    def Fibonacci(self , n: int) -> int:
        # write code here
        # 特殊情况处理
        if n==1 or n==2:
            return 1
        def dfs(n):
            if n <= 2:
                return 1
            res = dfs(n-1)+dfs(n-2)
            return res
        return dfs(n)

class Solution:
    def Fibonacci(self , n: int) -> int:
        # write code here
        # 特殊情况处理
        if n==1 or n==2:
            return 1
        a,b = 1,1
        for i in range(3,n+1):
            # 需要一个变量保存之前的b作为下一轮的a
            temp_a = b
            b = a + b
            a = temp_a
        return b

class Solution:
    def Fibonacci(self , n: int) -> int:
        # write code here
        memo = {}
        
        def dfs(k):
        # 函数功能：计算第 k 个值
        # 终止条件：k=0或k=1或者已经算过了！！！
            if k <= 1:
                return k
            if k in memo:
                return memo[k]
            
            memo[k] = dfs(k - 1) + dfs(k - 2)
            return memo[k]
        
        return dfs(n)


# 描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个 n 级的台阶总共有多少种跳法
# （先后次序不同算不同的结果）。
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param number int整型 
# @return int整型
#
class Solution:
    def jumpFloor(self , number: int) -> int:
        # write code here
        # 到第n级的跳法等于
        # 到 第n-1级 的跳法 + 
        # 到 第n-2级 的跳法
        
        # 特殊情况处理
        if number==1:
            return 1
        if number == 2:
            return 2
        a = 1
        b = 2
        for i in range(3,number+1):
            temp_a = b
            # b = 2*a+b # 不行的原因在于只能跳一次，不能跳两次一步
            b = a+b
            a = temp_a
        return b

# 描述
# cost[i]  是从楼梯第
# i 个台阶向上爬需要支付的费用，
# 下标从0开始。
# 一旦你支付此费用，即可选择向上爬一个或者两个台阶。
# 你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
# 请你计算并返回达到楼梯顶部的最低花费。

# @param cost int整型一维数组 
# @return int整型
#
class Solution:
    def minCostClimbingStairs(self , cost: List[int]) -> int:
        # write code here
        # 简单的情形
        n = len(cost)
        if n <= 2:
            # n=1意味着只有一个台阶,那不需要跳,直接选择下标为0的即可
            # n=2意味着只有两个台阶,那不需要跳,直接选择下标为1的即可
            return 0

        # 记录跳到第i格的最小花费
        dynamicplan_memory = [-1] * n

        # 返回跳到第i格的最小花费
        def dfs(n):
            if n <= 2:
                return 0
            if dynamicplan_memory[n-1] != -1:
                return dynamicplan_memory[n-1]
                # 到达第n个台阶花费的费用
            dynamicplan_memory[n-1] = min(dfs(n-1)+cost[n-1],dfs(n-2)+cost[n-2])
            return dynamicplan_memory[n-1]
        return dfs(n)

# 描述
# 给定两个字符串str1和str2，输出两个字符串的最长公共子序列。
# 如果最长公共子序列为空，则返回"-1"。
# 目前给出的数据，仅仅会存在一个最长的公共子序列

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common subsequence
# @param s1 string字符串 the string
# @param s2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , s1: str, s2: str) -> str:
        # write code here
        # 特殊情况处理
        if len(s1)==0 or len(s2)==0:
            return -1
        count = 0
        for s in s1:
            for ss in  s2:
                if s == ss:
                    count += 1
                else:
                    break
            count = max(0,count)
        return count

# 一个机器人在m×n大小的地图的左上角（起点）。
# 机器人每次可以向下或向右移动。机器人要到达地图的右下角（终点）。
# 可以有多少种不同的路径从起点走到终点？
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param m int整型 
# @param n int整型 
# @return int整型
#
#  * *
#  * *
class Solution:
    def uniquePaths(self , m: int, n: int) -> int:
        # write code here
        # 到达某一位置的不同路径数=到达其左边的不同路径数+到达其上方的不同路径数
        # 特殊情况处理
        if m < 1 or n < 1:
            return 0
        dynamicplan_memory = [[0] * n for _ in range(m)]
        def dfs(i,j):
            if i <= 0 and j <= 0:
                return 1
            if dynamicplan_memory[i][j] != 0:
                return dynamicplan_memory[i][j]
            if i < 0 or j < 0:
                return 0
            dynamicplan_memory[i][j] = dfs(i-1,j)+dfs(i,j-1)
            return dynamicplan_memory[i][j]
        return dfs(m-1,n-1)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 初始化 dp 数组
        dp = [[1] * n for _ in range(m)]  # 第一行和第一列都初始化为 1

        # 填充 dp 表
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

# 描述 输入一个长度为n的整型数组array，
# 数组中的一个或连续多个整数组成一个子数组，
# 子数组最小长度为1。求所有子数组的和的最大值。
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param array int整型一维数组 
# @return int整型
#
class Solution:
    def FindGreatestSumOfSubArray(self , array: List[int]) -> int:
        # write code here
        # 原数组所有子数组可按以数组中的元素结尾划分!!!!!!
        # 比如[1,2]可按以1结尾和以2结尾划分
        # [1] 和 [2],[1,2]
        # 比如[1,2,3]可按以1结尾\以2结尾\以3结尾划分
        # [1] 和 [2],[1,2] 和 [3],[2,3],[1,2,3]
        # 因此只需要比较 按以 i 为结尾划分的子数组的和最大值
        # 那 以 i 为结尾 和 以 i - 1 为结尾联系是什么?
        # dp[i] 和 dp[i-1]+dp[i]二者间的最大值
        # 或者简单地想:第i和第i-1的区别在于多了一个元素
        # 多了一个元素只会多两种组合,前面的dp[i-1]加上dp[i]和dp[i]自己一个
        n = len(array)
        if n <= 0:
            return 0
        dp_memory = [0] * n
        dp_memory[0] = array[0]
        max_sum = dp[0]
        for i in range(1,n):
            dp_memory[i] = max(dp_memory[i-1],dp_memory[i-1] + array[i])
            max_sum = max(max_sum,dp_memory[i])
        return max_sum

# 描述
# 对于长度为n的一个字符串A（仅包含数字，大小写英文字母），
# 请设计一个高效算法，计算其中最长回文子串的长度。
# 回文子串:正读反读都一样

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param A string字符串 
# @return int整型
#
class Solution:
    def getLongestPalindrome(self , A: str) -> int:
        if len(A) == 0:
            return 0
        
        n = len(A)
        max_len = 0

        def expand(left,right):
            while left >= 0 and right < n and A[left] == A[right]:
                left -= 1
                right += 1
                return right - left + 1 - 2

        for i in range(n):
            len_1 = expand(i,i)
            len_2 = expand(i,i+1)
            max_len = max(len_1,len_2,max_len)
        return max_len

# 描述
# 现在有一个只包含数字的字符串，将该字符串转化成IP地址的形式，返回所有可能的情况。
# 例如：
# 给出的字符串为"25525522135",
# 返回["255.255.22.135", "255.255.221.35"]. (顺序没有关系)
from typing import List

class Solution:
    def restoreIpAddresses(self , s: str) -> List[str]:
        res = []
        
        def dfs(start, path):
            
            # 如果已经4段
            if len(path) == 4:
                # 在已经4段的情况下，当前处理的位置（索引）已经超出s索引范围
                if start == len(s):
                    res.append(".".join(path))
                return
            
            # 每段最多3位
            # 循环是针对path的，执行一次代表path当前的不同选择（选择1个或者2个或者3个...）
            # 递归是针对一种选择的不断深入
            #    i
            #    2
            #   /
            # 1
            #   \
            #    3   dfs()
            for i in range(1, 4):
                # start为当前处理的位置
                if start + i > len(s):
                    break
                
                # 当前循环截取的字符串长度
                segment = s[start:start+i]
                
                # 前导0判断
                if segment[0] == '0' and len(segment) > 1:
                    continue
                
                # 数值判断
                if int(segment) > 255:
                    continue
                
                dfs(start+i, path + [segment])
        
        dfs(0, [])
        return res

# 描述
# 给定两个字符串 str1 和 str2 ，请你算出将 str1 转为 str2 的最少操作数。
# 你可以对字符串进行3种操作：
# 1.插入一个字符
# 2.删除一个字符
# 3.修改一个字符。
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str1 string字符串 
# @param str2 string字符串 
# @return int整型
#
class Solution:
    def editDistance(self , str1: str, str2: str) -> int:
        # write code here
        # 如果str1包含str2的所有字符，那只需要删除并换位就可以，但不支持换位操作







        









