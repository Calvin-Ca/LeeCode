# 反转k个节点，剩下不足k的不反转
# {1,2,3,4,5},2
# {2,1,4,3,5}
class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

def print_node(head):
    res = []
    cur = head
    while cur:
        res.append(str(cur.val))
        cur = cur.next
    print("{" + ",".join(res) + "}")

def solve():

    line = input()
    line = line.replace("{","").replace("}","")
    str_list = line.split(",")
    k = int(str_list[-1])
    arr = [int(s) for s in str_list[:-1]]
    print(arr,k)

    yummy = Node(0)
    cur = yummy
    for num in arr:
        cur.next = Node(num)
        cur = cur.next
    head = yummy.next
    
    print_node(head)
    print(k,end="")

def reverse_k(head,k):
    # 递归：函数功能，
    # 给定节点头，进行反转
    # 有没有k个节点
    dummy = Node(0)
    dummy.next = head
    cur = dummy
    for i in range(k): # 从头开始执行k次循环，结束后cur=第k个节点
        cur = cur.next
        if not cur:
            return
    head = reverse_k(head,k)
    return head
solve()