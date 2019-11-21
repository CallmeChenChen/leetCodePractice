# -*- coding: utf-8 -*-
# @Date   : 2019/11/12
# @File   : linkedList_practice3.py
# @Author : zhaochen

# from linkedList import LinkedList, Node
from utils import LinkedList, Node
'''练习三'''
# 反转一个链表
def reverseLinkedList(ll):
    if not ll:
        raise ValueError("ll is Empty.")
    pre = None
    curr = ll
    while curr is not None:
        tmp = curr.next # 记录当前节点的之后节点
        curr.next = pre # 当前节点连接在pre上
        pre = curr # 将pre节点移到curr上
        curr = tmp # 移动curr节点
    return pre

ll = LinkedList()
ll.add_first(4)
ll.add_first(5)
ll.add_first(3)
ll.add_first(7)
ll.add_first(9)
ll.print_list()

a = reverseLinkedList(ll.head.next)
ll.head.next = a
ll.print_list()


# 反转一个链表2  从m到n之间进行反转
def reverseLinkedList2(ll, m, n):
    if m > n:
        return None
    if m == n:
        return ll
    dummy = Node(None) #
    dummy.next = ll
    pre = dummy
    for i in range(m - 1):
        pre = pre.next
    result = None
    curr = pre.next #
    for i in range(n - m + 1):
        tmp = curr.next
        curr.next = result
        result = curr
        curr = tmp
    #
    pre.next.next = curr
    pre.next = result
    return dummy.next


ll = LinkedList()
ll.add_first(4)
ll.add_first(5)
ll.add_first(3)
ll.add_first(7)
ll.add_first(9)
ll.print_list()

# ll.head.next = reverseBetween(ll.head.next, 2,3)
ll.print_list()
# a = reverseLinkedList(ll.head.next)
a = reverseLinkedList2(ll.head.next, 1, 3)
ll.head.next = a
ll.print_list()

# 成对交换节点
def swapPairLinkedListNodes(ll):
    if not ll :
        return None
    if ll.next is None:
        return ll
    dummy = curr = Node(None)
    dummy.next = ll
    # 画图理解
    while curr.next and curr.next.next:
        node1 = curr.next # 要交换的节点1
        node2 = curr.next.next # 要交换的节点2
        curr.next = node2 #
        node1.next = node2.next
        node2.next = node1
        curr = curr.next.next # 移动当前节点2步
    return dummy.next

ll = LinkedList()
ll.add_first(4)
ll.add_first(5)
ll.add_first(3)
ll.add_first(7)
ll.add_first(9)
ll.print_list()
ll.head.next = swapPairLinkedListNodes(ll.head.next)
ll.print_list()


#给定一个链表，对每两个相邻的节点作交换，返回head.


#以k-group反转节点

# 回文链表  可以用时间复杂度为O(n),空间复杂度为O(1)的算法实现吗？
def palindromeLinkedList(ll):
    # 先反转 在比较
    if not ll:
        flag = 1
    dummy = curr = ll
    pre = None
    while curr is not None:
        tmp = curr.next
        curr.next = pre
        pre = curr
        curr = tmp
    # 比较
    while dummy is not None:
        if dummy.val == pre.val:
            flag = True
        else:
            flag = False
            break
        dummy = dummy.next
        pre = pre.next
    return 1 if flag else 0

def palindromeLinkedList2(ll):
    # 反转一半 之后再比较
    pre = None
    slow = fast = ll
    while fast and fast.next:
        fast = fast.next.next
        pre, pre.next, slow = slow, pre, slow.next
        # pre = slow
        # pre.next = pre
        # slow = slow.next
    # 判断是否为奇偶数
    if fast:
        slow = slow.next
    while pre and pre.val == slow.val:
        slow = slow.next
        pre = pre.next
    return not pre

ll = LinkedList()
ll.add_first(1)
ll.add_first(2)
ll.add_first(2)
ll.add_first(1)
ll.print_list()
print(palindromeLinkedList2(ll.head.next))
print(palindromeLinkedList(ll.head.next))
ll.head.next = palindromeLinkedList(ll.head.next)
r = palindromeLinkedList(ll.head.next)
ll.print_list()


#从有序链表中删除重复元素
# 给定链表1->1->2->3->3,返回1->2->3
def duplicatesLinkedList(ll):
    dummy = curr = ll
    while curr.next is not None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy

ll = LinkedList()
ll.add_first(4)
ll.add_first(4)
ll.add_first(4)
ll.add_first(3)
ll.head.next = duplicatesLinkedList(ll.head.next)
ll.print_list()

# 从有序链表中删除重复元素II
# 给定链表1->2->3->3->4->4->5，返回 1->2->5
def duplicatesLinkedList2(ll):
    pass




