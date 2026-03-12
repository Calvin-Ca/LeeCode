# 描述
# 一个数组A中存有 n 个整数，在不允许使用另外数组的前提下，将每个整数循环向右移 M（ M >=0）个位置，
# 即将A中的数据由（A0 A1 ……AN-1 ）变换为（AN-M …… AN-1 A0 A1 ……AN-M-1 ）（最后 M 个数循环移至最前面的 M 个位置）。
# 如果需要考虑程序移动数据的次数尽量少，要如何设计移动的方法？

class Solution:
    def solve(self , n: int, m: int, a: List[int]) -> List[int]:
        # write code here 
        # 把要移动的数组找出来
        move_m = a[n-m:n]
        move_left = a[:n-m]
        a[:m] = move_m
        a[m:] = move_left
        return a

from typing import List

class Solution:
    def solve(self , n: int, m: int, a: List[int]) -> List[int]:
        # 剪枝 m > n 的情况
        m = m % n
        
        def reverse(l,r):
            while l < r:
                a[l],a[r] = a[r],a[l]
                l += 1
                r -= 1
            
        # 反转整个数组
        reverse(0,n-1)
        # 反转前 m 个
        reverse(0,m-1)
        # 反转剩下的
        reverse(m,n-1)
        return a 