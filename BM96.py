# 描述 有 n 个活动即将举办，每个活动都有开始时间与活动的结束时间，第 i 个活动的开始时间是 starti ,第 i 个活动的结束时间是 endi ,
# 举办某个活动就需要为该活动准备一个活动主持人。 一位活动主持人在同一时间只能参与一个活动。并且活动主持人需要全程参与活动，
# 换句话说，一个主持人参与了第 i 个活动，
# 那么该主持人在 (starti,endi) 这个时间段不能参与其他任何活动。求为了成功举办这 n 个活动，最少需要多少名主持人。


from typing import List

class Solution:
    def minmumNumberOfHost(self , n: int, startEnd: List[List[int]]) -> int:
        
        starts = [x[0] for x in startEnd]
        ends = [x[1] for x in startEnd]
        
        starts.sort() # O(n log n)
        ends.sort() 
        
        i = j = 0
        host = 0
        res = 0
    #      ---
    #           ---
    #               ----
        while i < n:   # O(n)        # 一直盯着的是开始的活动
            if starts[i] < ends[j]:  # 先开始的活动的开始时间 小于 先结束的活动的结束时间，不管是不是一个活动（这里主持人管的是某个时间段内的所有活动，而不是针对某一个）
                host += 1
                res = max(res, host) # 
                i += 1
            else:
                host -= 1
                j += 1
                
        return res
    
class Solution: 
    def minmumNumberOfHost(self , n: int, startEnd: List[List[int]]) -> int: 
        # write code here
        # 同一时间内，同时有多少个活动同时进行
        start = [e[0] for e in startEnd]
        end = [e[1] for e in startEnd]
        start.sort()
        end.sort()
        
        i,j = 0,0
        host_for_current_period = 0
        host_max = 0
        
        while i < n: # 确保所有活动都考虑
            # 一个时间段对应一个主持人，从 最早开始 和 最早结束 这个时间段开始
            if start_sort[i] < end_sort[j]:        # 意味着当前时间段的活动还在进行，又开始了新的活动
                host_for_current_period += 1
                host_max = max(host_max,host_for_current_period)
                i += 1
            else:  # 开始以新起点开始的新的时间段的活动
                host_for_current_period -= 1
                j += 1
        return host_max

class Solution: 
    def minmumNumberOfHost(self , n: int, startEnd: List[List[int]]) -> int: 
        # write code here
        # 维护一个 host_max ，记录整个时间区间内同时所须的最多主持人
        # 时刻盯着当前开始的活动
        # 给最早开始、最早结束的区间安排一个主持人
        # 向右移动活动开始指针，
        # 如果扫进来的活动 开始时间 小于 最早结束时间
        # 加派主持人，记录当前时间段所须的主持人，继续 向右移动活动开始指针，
        # 如果扫进来的活动 开始时间 大于 最早结束时间
        # 意味着这个活动可以使用 之前释放的一个主持人 host-1
        # 结束时间指针后移，因为上一个结束时间已经小于 开始时间 可以开始负责新的区间了
        
        # 同一时间内，同时有多少个活动同时进行
        
        start = [e[0] for e in startEnd]
        end = [e[1] for e in startEnd]
        start.sort()
        end.sort()
        
        i,j = 0,0
        host_for_current_period = 0
        host_max = 0
        
        while i < n: # 确保所有活动都考虑
            # 一个时间段对应一个主持人，从 最早开始 和 最早结束 这个时间段开始
            if start_sort[i] < end_sort[j]:        # 意味着当前时间段的活动还在进行，又开始了新的活动
                host_for_current_period += 1
                host_max = max(host_max,host_for_current_period)
                i += 1
            else:  # 开始以新起点开始的新的时间段的活动
                host_for_current_period -= 1
                j += 1
        return host_max