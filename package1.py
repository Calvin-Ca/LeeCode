# 主要考察操作的数据结构
## 数组：二分查找，最大值，排序
## 链表：反转，合并，环判断
## 树：遍历/判断树类型

# 主要考察应用的数据结构
## 栈
## 队列
## 堆
## 哈希

# 思想
## 分治
## 贪心
## 动态规划
## 双指针 

# ACM IO
## 输入：
### sys.stdin.read()，运行此代码后，用户可一次性输入所有数据，<EOF>结束，适合数据量达到 $10^5$ 或 $10^6$
### 返回一个字符串，若输入有多行则包括换行符\n
### input(),运行此代码后，用户可输入一行数据，Enter结束
### 返回一个去除行尾换行符的字符串
### str.strip()，移除首尾字符（默认空白），返回字符串
### str.split()，分割字符，返回字符串组成的列表
### eval(input()),直接把input当作 Python 表达式，{1,2,1,1},2,3，前者会被视为集合

# 链表的特点
## 无法直接知道链表有多长，导致不能写for循环，需要while遍历






############################################################ 反转链表
# 维护一个pre变量，遍历链表，从头节点开始改变指针，返回pre
# class LinkNode:
#     def __init__(self,x):
#         self.val = x
#         self.next = None

# def build_link(arr):
#     dummy = LinkNode(0)
#     cur = dummy
#     for x in arr:
#         cur.next = LinkNode(x)
#         cur = cur.next
#     return dummy.next

# def print_link(head):
#     res = []
#     while head:
#         res.append(str(head.val))
#         head = head.next
#     print ("["+",".join(res)+"]")

# def solve(head):
#     # 维护一个pre
#     pre = None
#     while head:
#         temp = head.next # 断开前维护后一个节点
#         head.next = pre # 改变节点指针
#         pre = head
#         head = temp
#     return pre

# if __name__ == "__main__":
#     arr = eval(input())
#     head = build_link(arr)   # 从列表构建链表
#     print_link(head)
#     pass

############################################################ 反转链表m,n位置
# 找到m位置节点，从m位置开始遍历n个节点，逐个改变指针
# {1,2,3,4,5},2,4
# {1,4,3,2,5}
class LinkNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def input2():
    # {1,2,3,2},2,3
    # 替换法去括号
    raw = input().replace("{","").replace("}","")
    # print(raw)
    str_list = raw.split(",")
    # print(str_list)
    n = int(str_list[-1])
    m = int(str_list[-2])
    arr = [int(s) for s in str_list[:-2]]
    # print(arr,m,n)
    return arr,m,n

def arr2head(arr):
    # 列表转换为链表
    dummy = LinkNode(0)
    cur = dummy
    for value in arr:
        cur.next = LinkNode(value)
        cur = cur.next
    return dummy.next

def solve_v1(head,m,n):
    # 反转链表第m到第n个元素
    # 关键：要翻转第m个到第n个，必须维护第m-1个，第n+1个无需维护，因为会遍历到
    # 但维护第m-1个使用range容易导致越界！

    # 剪枝
    if not head or m == n:
        return head

    # 找到第m个元素
    print("solve")
    m_pre = head
    for i in range(m): # m=1时，m_pre是第二个
        m_pre = m_pre.next
    # 改变第m到第n个元素的指针
    pre = m_pre
    cur = m_pre.next
    for i in range(m,n+1): # 第m到第n个元素的指针都反转了
        temp = cur.next # 是第n+1个
        cur.next = pre
        pre = cur   # pre 是第n个
        cur = temp
    temp.next = pre
    print("solve")
    return head

def solve_v2(head,m,n):
    # 反转链表第m到第n个元素
    # 关键：要翻转第m个到第n个，必须维护第m-1个，第n+1个无需维护，因为会遍历到
    # 但维护第m-1个，从head开始遍历的话需使用range(m-2)容易导致越界！！！！
    # 思路：与反转整个链表一样，从dummy开始遍历，只需到m-1，并对m=1的情况单独讨论

    # 剪枝
    if not head or m == n:
        return head
        
    dummy = LinkNode(0)
    dummy.next = head

    # 第m个元素的前驱
    pre = dummy
    for i in range(m-1): # 执行1次到第1个节点,执行m-1次到第m-1个节点,range(0)合法
       pre = pre.next
    
    cur = pre.next       # pre现在是第m-1个节点，cur是第m个节点
    for i in range(n-m+1): 
        temp = cur.next 
        cur.next = pre  # 将第m个节点指向了第m-1个，但第m-1个也是指向第m个的！！！！！
        pre = cur
        cur = temp # 改变了第m到第n个节点的next，但第m-1的next还是指向第m个
    temp.next = cur 
    return dummy.next

def solve_v2(head,m,n):
    # 反转链表第m到第n个元素
    # 关键：要翻转第m个到第n个，必须维护第m-1个，第n+1个无需维护，因为会遍历到
    # 但维护第m-1个，从head开始遍历的话需使用range(m-2)容易导致越界！！！！
    # 思路：与反转整个链表一样，从dummy开始遍历，只需到m-1，并对m=1的情况单独讨论

    # 剪枝
    if not head or m == n:
        return head
        
    dummy = LinkNode(0)
    dummy.next = head

    # 第m个元素的前驱
    pre = dummy
    for i in range(m-1): # 执行1次到第1个节点,执行m-1次到第m-1个节点,range(0)合法
       pre = pre.next
    
    cur = pre.next       # pre现在是第m-1个节点，cur是第m个节点
    # 头插法避免顾及第m-1和n+1个节点的指针问题
    # 从第m+1个节点开始，将后面的每一个逐个插到m前面，直到n
    for i in range(n-m):
        nxt = cur.next # 锁定第m+1个节点
        cur.next = nxt.next  # 维护好前一个指针（保证原链表不断）并断开
        # 放在cur前面  对比nxt.next = pre.next(改变指针)，nxt = pre.next(变量赋值)
        # 不能写成nxt.next = cur的原因是，在除了第一次的后续循环中，cur之前插入了新元素
        nxt.next = pre.next   
        pre.next = nxt     # 放在pre后面

def print_solve(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print ("{"+",".join(res)+"}")

# if __name__ == "__main__":
    # input2arr,
    # arr,m,n = input2()
    # print(arr,m,n)

    # # arr2NodeList,
    # head = arr2head(arr)
    # print_solve(head)

    # # solve
    # re_head = solve(head,m,n)
    # print_solve(re_head)

# 输入{1,2,3,4},2,3
# 返回{1,2,4,3}

def input3():
    line = input() # 字符串
    line = line.replace("{","").replace("}","")          # 删除括号
    str_list = line.split(",")
    m,n = int(str_list[-2]),int(str_list[-1])
    arr = [int(s) for s in str_list[:-2]]
    return arr,m,n

class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

def arr2head1(arr):
    yummy = Node(0) # 变量，对象
    for num in arr:
        yummy.next = Node(num) # 把Node(0)的next指向Node(num)
        yummy = yummy.next
    return yummy.next  # yummy变量最后会指向None，所以需要单开一个变量维护头节点

def arr2head2(arr):
    dummy = Node(0)
    cur = dummy # 初始状态，cur和dummy都引用node（0）对象
    for num in arr:
        cur.next = Node(num) # 修改cur引用的对象（Node（0））的.next属性所引用的对象Node(num)
        cur = cur.next # 让cur引用 cur引用的对象（Node（0））的.next属性所引用的对象Node(num)
    return dummy.next

def solve_v3(head,m,n):
    if not head:
        return None
    # 翻转链表的第m到n个元素
    # s1，找到第m-1个元素，作为pre
    dummy = Node(0)  # dummy引用Node(0)
    dummy.next = head # 修改Node(0)的属性值，Node(0)指向head了

    pre = dummy # 不能改变dummy的引用，因为最后要返回
    for i in range(m-1): # 从虚拟头节点开始遍历，遍历了m次就到第m个节点
        pre = pre.next   # pre引用第m-1个节点
     
    # 头插法，将m后面的节点，即从m+1开始，逐个插到pre后面（不是cur前面）
    cur = pre.next   # cur引用的是第m个节点
    for i in range(n-m): # 只用从第m+1个节点执行到第n个（包括两端）
        nxt  =cur.next   # 锁定第m+1个节点
        cur.next = nxt.next # 将第m个节点指向第m+2个节点
        nxt.next = pre.next  # 将第m+1个节点指向原来pre后的第一个节点
        pre.next = nxt # 将第m-1个节点指向第m+1个节点
    return dummy.next

def print_node(head):
    res = []
    cur = head
    while cur:
        res.append(str(cur.val))
        cur = cur.next
    print("{" + ",".join(res) + "}")

arr,m,n = input3()
print(arr,m,n)
head = arr2head2(arr)
print_node(head)
res = solve_v3(head,m,n)
print_node(res)

# 删除链表中的重复元素
# {1,2,2}
# {1}

arr = 



