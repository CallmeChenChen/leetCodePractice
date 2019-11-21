# -*- coding: utf-8 -*-
from utils import LinkedList, Node

# 练习(下)

#  合并两个有序链表
# 合并两个有序链表，返回一个新的列表。新的列表是由这两个列表的节点
#  拼接而成的。

def merge_two_sorted_linked_list(l1, l2):
    '''
    合并l1 和 l2 2个有序链表
    :param l1:
    :param l2:
    :return:
    '''
    curr = dummy = Node(0)
    while l1 and l2:
        if l1.val > l2.val:
            curr.next = l2
            l2 = l2.next
        else:
            curr.next = l1
            l1 = l1.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next


def merge_two_sorted_linked_list1(l1, l2):
    '''
    合并l1 和 l2 2个有序链表
    :param l1:
    :param l2:
    :return:
    '''
    if not l1 or not l2:
        return l1 or l2
    if l1.val > l2.val:
        l2.next = merge_two_sorted_linked_list1(l1, l2.next)
        return l2
    else:
        l1.next = merge_two_sorted_linked_list1(l1.next, l2)
        return l1

l1 = LinkedList()
l1.add_last(1)
l1.add_last(5)
l1.add_last(7)
l1.print_list()
l2 = LinkedList()
l2.add_last(2)
l2.add_last(4)
l2.add_last(6)


merge_two_sorted_linked_list1(l1.head.next, l2.head.next)
merge_two_sorted_linked_list(l1.head.next, l2.head.next)


# 两个链表的交集
# 写一个可以找到两个链表交集开始节点的程序
def getIntersectNode(l1, l2):
    '''找到两个ll的长度差 先走k步 相遇点就是交集节点'''
    curr1, curr2 = l1, l2
    len1, len2 = 0, 0
    while curr1 is not None:
        curr1 = curr1.next
        len1 += 1
    while curr2 is not None:
        curr2 = curr2.next
        len2 += 1
    curr1, curr2 = l1, l2
    if len1 > len2:
        for i in range(len1-len2):
            curr1 = curr1.next
    else:
        for i in range(len2-len1):
            curr2 = curr2.next
    while curr1 != curr2:
        curr1 = curr1.next
        curr2 = curr2.next
    return curr1


def getIntersectNode1(l1, l2):
    '''跑马拉松 二者跑的长度不同 调整长度使二者在交点的node相遇'''
    if l1 and l2:
        raise Exception('Empty Linked List')
    curr1, curr2 = l1, l2
    while curr1 != curr2:
      curr1 = curr1.next if curr1 else curr2
      curr2 = curr2.next if curr2 else curr1
    return curr1


#  链表插入排序
#  用插入排序对一个链表做排序
def insertSortLinkedList(ll):
    '''ll为链表'''
    curr = ll  # X->2->7->1->2
    dummy = Node()  # X->2   X->2->7  X->1->2->7 ...
    while curr is not None:
        sorted_pre = dummy  # 每次指向已经排好序的头部
        while sorted_pre.next is not None and sorted_pre.next.val < curr.val:
            # 找到当前这个节点要插入的前一个节点
            sorted_pre = sorted_pre.next
        # 画图比较好理解
        tmp = curr.next  # 记录当前剩下的节点
        curr.next = sorted_pre.next  # curr节点的下一个节点；连在pre的下一个
        sorted_pre.next = curr  # pre的下一个节点为curr节点
        curr = tmp
    return dummy.next

ll = LinkedList()
ll.add_first(2)
ll.add_first(3)
ll.add_first(1)
ll.add_first(5)

ll.print_list()
a = ll.head.next
b = insertSortLinkedList(a)
ll.head.next = b
ll.print_list()

#  链表排序 (归并排序 merge sort)
#  用常数空间复杂度对链表排序，时间复杂度为 O ( n log n)
def getMiddle(ll):
    '''不存在dummy head 的ll'''
    if not ll:
        return ll
    slow = ll
    fast = ll
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def mergeSortLinkedList(ll):
    '''先把其拆成两半 在进行合并 找到中点拆成2半  递归'''
    if ll is None or ll.next is None:
        return ll
    mid = getMiddle(ll)
    right = mid.next
    mid.next = None
    left = ll
    return merge_two_sorted_linked_list(mergeSortLinkedList(left), mergeSortLinkedList(right))


ll = LinkedList()
ll.add_first(2)
ll.add_first(3)
ll.add_first(1)
ll.add_first(5)
ll.add_first(5)
ll.print_list()

a = ll.head.next
b = mergeSortLinkedList(a)
ll.head.next = b
ll.print_list()


# 分区链表
# 对链表进行partition
def partition(ll, x):
    if not ll:
        return None
    left = Node(None)
    left_node = left
    right = Node(None)
    right_node = right
    curr = ll
    while curr is not None:
        if curr.val >= x.val:
            right_node.next = curr
            right_node = right_node.next
        else:
            left_node.next = curr
            left_node = left_node.next
        curr = curr.next
    # [left] + [pivot] + [right]
    right_node.next = None
    left_node.next = x
    x.next = right.next
    # left_node.next = right.next
    return left.next

ll = LinkedList()
ll.add_first(4)
ll.add_first(5)
ll.add_first(3)
ll.add_first(7)
ll.add_first(9)
ll.print_list()

a = partition(ll.head.next, Node(6))
ll.head.next = a
ll.print_list()
