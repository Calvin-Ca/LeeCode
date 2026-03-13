# 先举几个测试用例：
# 描述
# 给定一个m x n大小的矩阵（m行，n列），按螺旋的顺序返回矩阵中的所有元素。
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param matrix int整型二维数组 
# @return int整型一维数组
#
class Solution:
    def spiralOrder(self , matrix: List[List[int]]) -> List[int]:
        # 剪枝
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        left,right = 0,n-1
        up,down = 0,m-1
        res = []
        # 带等于 防止一行的情况不做遍历
        while left <= right and up <= down: # 每执行一次循环，上下压缩一次，左右压缩一次
        # 想象只有两行，但有50列，当行指针收缩一次后，列指针也收缩一次
        # 此时行指针停止，但列指针仍满足left < right，这种情况下循环应该停止
        # 因为所有元素已经遍历完了
            for i in range(left,right+1): # 把第0行元素遍历完了
                res.append(matrix[up][i])
            up += 1           # 顶部下一行
            for j in range(up,down+1):
                res.append(matrix[j][right])
            right -= 1        # 右边往左移一列
             #  < 说明遍历完半圈后up下还有行，(比如原数组3行)
             #  = 说明遍历完顶部后底部和顶部都在一行了，都还要遍历down(比如原数组2行)
             #  比如原数组1行
            if up <= down:
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
                down -= 1         # 底部上一行
            if left <= right:
                for j in range(down,up-1,-1):
                    res.append(matrix[j][left])
                left += 1
        return res