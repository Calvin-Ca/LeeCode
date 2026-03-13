# 描述
# 有一个NxN整数矩阵，请编写一个算法，将矩阵顺时针旋转90度。
# 给定一个NxN的矩阵，和矩阵的阶数N,请返回旋转后的NxN矩阵。
class Solution:
    def rotateMatrix(self , mat: List[List[int]], n: int) -> List[List[int]]:
        # write code here
        mat_2 = [[0]*n for _ in range(n)]
        for i in range(n):
            r = mat[i][:]
            # mat_2[:] 返回的是整个二维列表的 浅拷贝，
            # 对其赋值不会修改 mat_2 的列,Python 里不能直接用 mat_2[:][index] = ... 来修改某一列，需要明确列索引。
            # 正确做法是：mat_2[j][...] = ... 逐元素赋值
            mat_2[:][n-i] = r 
        return mat_2
class Solution:
    def rotateMatrix(self , mat: List[List[int]], n: int) -> List[List[int]]:
        # write code here
        mat_2 = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                mat_2[j][n-1-i] = mat[i][j]
        return mat_2
                
        # [1,2,3] [0,0]-[0,2] [0,1]-[1,2] 
        # [4,5,6]
        # [7,8,9]
        
        # 7,4,1
        # 8,5,2
        # 9,6,3