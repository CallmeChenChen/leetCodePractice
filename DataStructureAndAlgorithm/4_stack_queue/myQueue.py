# -*- coding: utf-8 -*-
# @Date   : 2019/11/12
# @File   : myQueue.py

from linkedList import Node

# 固定容量
DEFAULT_CAPACITY = 10

class ArrayQueue(object):
    def __init__(self):
        self._data = [None] * DEFAULT_CAPACITY
        self._size = 0 # tail
        self._front = 0 # head
    def __len__(self):
        return self._size

    def first(self):
        if self._size == 0:
            raise Exception("Queue is Empty")
        return self._data[self._front]

    def dequeue(self):
        if self._size == 0:
            raise Exception("Queue is Empty")
        result = self._data[self._front]
        self._data[self._front] = None # dequeue 之后移动head指针
        self._front = (self._front + 1) % len(self._data)
        self._size = self._size - 1
        return result

    def enqueue(self, x):
        # 如果队列的容量超过固定容量时，就扩大为当前容量的2倍
        # 同时，重新处理front 和 tail 2个指针
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        # 插入 x
        pos = (self._front + self._size) % len(self._data)
        self._data[pos] = x
        self._size += 1

    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            # 新的queue的位置
            self._data[k] = old[walk]
            # old 通过取模的形式 移动指针
            walk = (1 + walk) % len(old)
        self._front = 0


class LinkedListQueue(object):
    def __init__(self):
        # 起2个指针 头和尾指针
        self.head = None
        self.tail = None
        self.len = 0

    def enqueue(self, value):
        # 在尾指针增加新值
        new_node = Node(value)
        if self.tail is not None:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.len += 1

    def dequeue(self):
        # 在头指针删除值
        if not self.is_empty():
            # point head to next node
            tmp = self.head
            self.head = self.head.next
            print("dequeue sucess")
            self.len -= 1
            return tmp
        else:
            raise ValueError("Empty QUEUE")

    def is_empty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False

    def peek(self):
        return self.head.val

    def __len__(self):
        return self.len

    def print(self):
        node = self.head
        while node:
            print(node.val, end=" ")
            node = node.next
        print('')
