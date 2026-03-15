# 描述 # 给定一个长度为n的数组arr，返回arr的最长无重复元素子数组的长度，无重复指的是所有数字都不相同。 
# 子数组是连续的，比如[1,3,5,7,9]的子数组有[1,3]，[3,5,7]等等，但是[1,3,7]不是子数组

class Solution:
    def maxLength(self , arr: List[int]) -> int:
        # 记录每个以右指针结尾的最长无重复元素子数组
        # 维护两个指针（对应一个窗口），右指针遍历整个数组
        # 右指针每到一个位置，如果与窗口已有元素不重复，加入新元素
        # 如果重复，移动左指针，找到重复的元素，移除重复的元素及其之前的元素
        # 更新窗口长度（max_len）[1,2,2,3]
        max_len = 0
        left = 0
        window = set() # 以右指针为终点的最长无重复元素子数组 集合
        for right in range(len(arr)):  # 2
            # 如果不在窗口内，直接加
            if arr[right] not in window: 
                window.add(arr[right])
            # 如果在窗口内，移动左指针直到使它刚好不在窗口内
            else:
                while arr[left] != arr[right]: # # 删除重复元素前的所有元素
                    window.remove(arr[left])
                    left += 1
                left += 1 # 删除重复的元素
                window.add(arr[right])
            max_len = max(max_len,right-left+1)
        return max_len