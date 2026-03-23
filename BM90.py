# 描述 给出两个字符串 s 和 t，要求在 s 中找出最短的包含 t 中所有字符的连续子串。
class Solution:
    def minWindow(self , S: str, T: str) -> str:
        # 起点均为0的左右指针，左指针不动，右指针向右扫描整个str
        # 维护一个与左右指针对应的window（字典），代表指针范围内包含的字符类别和频率
        # 当window和required一致时，右指针停止，开始向右移动左指针
        # 直到得到 右指针在停止位置时 通过移动左指针能得到的最短长度
        # 继续移动右指针，直到结束
        
        # 剪枝
        if len(S) < len(T):
            return ""
        
        # 统计出T中字符及出现的频率（因为不care顺序）
        from collections import Counter
        required = Counter(T) # 本质上是一个字典
        
        # 维护两个指针及指针范围内对应的窗口
        left,right = 0,0
        window,cat_in_window = {},0
        
        # 最小长度
        min_len = float("inf")
        min_len_start = 0   #  要保存历史中min_len对应的left，需要再维护一个变量，因为left在过程中是在变化的
           
        # 右指针从起点开始向右扩张，直到扫描完整个字符串
        while right < len(S):
            c = S[right] # 获取字符 
            if c in required: # 说明是我们想要的
                window[c] = window.get(c,0) + 1
                if window[c] == required[c]:
                    cat_in_window += 1
            right += 1
            
            while cat_in_window == len(required):
                # 由于循环条件，先计算上一轮left对应的min_len
                # 不仅更新min_len,要保存历史中min_len对应的left，需要再维护一个变量，因为left在过程中是在变化的
               if right - left < min_len:
                   min_len = right - left
                   min_len_start = left
                
               d = S[left] # 此时左指针位置的字符
               left += 1
               if d in window:
                    if window[d] == required[d]:
                        cat_in_window -= 1
                    window[d] -= 1
               
        return "" if min_len == float("inf") else S[min_len_start:min_len_start+min_len]