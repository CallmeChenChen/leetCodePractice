# -*- coding: utf-8 -*-

# 练习上

from utils import LinkedList, Node

# 删除链表中的节点， 除了结尾，只允许访问那个节点
def practice_work1(node):
    print(node.val)
    node.val = node.next.val
    node.next = node.next.next

# 找到中间节点
def practice_work2(ll):
    '''起2个指针 一个每次走1步 一个每次走2步'''
    if not ll.head or not ll.head.next:
        raise Exception('LL is Empty')
    node1 = ll.head
    node2 = ll.head
    while node1 is not None and node1.next is not None:
        node1 = node1.next.next
        node2 = node2.next
    return node2.val

# 是否有环：判定一个链表是否存在环
def practice_work3(ll):
    '''起2个指针 一个快 一个慢 看二者是否追上'''
    if not ll.head or not ll.head.next:
        raise Exception('LL is Empty')
    node1 = ll.head
    node2 = ll.head
    while node1 is not None and node1.next is not None:
        node1 = node1.next.next
        node2 = node2.next
        if node1 == node2:
            return 1
    return 0

# 环的开始：给定一个循环链表，找到环的开始节点
def practice_work4(ll):
    '''起2个指针 1个快 1个慢 二者追上时，
    将慢的放在head 然后二者同时用一倍速跑'''
    if not ll.head or not ll.head.next:
        raise Exception('LL is Empty')
    slow = ll.head
    fast = ll.head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    # 二者相遇时， 将任一节点移到head处
    slow = ll.head
    if slow is None or slow.next is None:
        return None
    # 二者再次相遇时，为环的开始位置
    while fast != slow:
        if not slow.next:
            return None
        fast = fast.next
        slow = slow.next
    return slow



#删除倒数第N个节点：删除一个链表中的倒数第N个节点
def practice_work5(ll, n):
    '''fast节点先走n步，然后slow节点在出发，
    当fast节点到尾部时，slow节点对应的为删除的节点位置'''
    if ll.len < n and n < 0:
        raise Exception('ERROr')
    fast = ll.head
    while n > 0:
        fast = fast.next
        n -= 1
    slow = ll.head
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    result = slow.next # 返回删除的那个节点
    slow.next = slow.next.next # 删除那个节点
    ll.len = ll.len - 1
    return result


# 分半：给定一个列表，把它分成两个列表，一个是前半部分，一个是
# 后半部分。
def practice_work6(ll):
    '''起 节点1 和节点2  节点1每次走1步 节点2每次走2步 节点2走到尾部时 节点1位于中间位置'''
    if not ll.head or not ll.head.next:
        raise Exception('LL is Empty')
    node1 = ll.head
    node2 = ll.head
    tmp = node2
    while node1 is not None:
        tmp = node2
        node2 = node2.next
        node1 = node1.next.next if node1.next is not None else None
    tmp.next = None
    # node2 中间节点
    back = node2
    front = ll.head
    return front, back




ll = LinkedList()
ll.add_first(2)
ll.add_first(3)
ll.add_first(4)
ll.add_first(5)

ll.print_list()

practice_work1(ll.head.next.next)

practice_work2(ll)

# 起一个循环链表
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d
d.next = b
ll = LinkedList()
ll.head = a
practice_work3(ll)

a, b = practice_work6(ll)
print(a)

a = practice_work5(ll,4)
a = practice_work4(ll)

import unittest

class TestBinarySearch1(unittest.TestCase):
    def setUp(self):
        self._f = binary_search_rec

    def test_empty(self):
        alist = []
        r = self._f(alist, 5)
        self.assertEqual(-1, r)

    def test_one(self):
        alist = [1]
        r = self._f(alist, 0)
        self.assertEqual(-1, r)
        r = self._f(alist, 1)
        self.assertEqual(0, r)

    def test_two(self):
        alist = [1, 10]
        r = self._f(alist, 0)
        self.assertEqual(-1, r)
        r = self._f(alist, 1)
        self.assertEqual(0, r)
        r = self._f(alist, 2)
        self.assertEqual(-1, r)
        r = self._f(alist, 10)
        self.assertEqual(1, r)
        r = self._f(alist, 11)
        self.assertEqual(-1, r)

    def test_multiple(self):
        alist = [1, 2, 3, 4, 5]
        r = self._f(alist, 5)
        self.assertEqual(4, r)
        r = self._f(alist, 4)
        self.assertEqual(3, r)
        r = self._f(alist, 2)
        self.assertEqual(1, r)
        r = self._f(alist, 1)
        self.assertEqual(0, r)
        r = self._f(alist, 6)
        self.assertEqual(-1, r)
        r = self._f(alist, 0)
        self.assertEqual(-1, r)

    def test_duplicate(self):
        alist = [1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5]
        r = self._f(alist, 5)
        self.assertEqual(5, alist[r])
        r = self._f(alist, 4)
        self.assertEqual(4, alist[r])
        r = self._f(alist, 2)
        self.assertEqual(2, alist[r])
        r = self._f(alist, 3)
        self.assertEqual(3, alist[r])
        r = self._f(alist, 1)
        self.assertEqual(1, alist[r])
        r = self._f(alist, 6)
        self.assertEqual(-1, r)
        r = self._f(alist, 0)
        self.assertEqual(-1, r)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
