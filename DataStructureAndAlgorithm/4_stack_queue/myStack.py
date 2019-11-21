# -*- coding: utf-8 -*-
# @Date   : 2019/11/12
# @File   : arrayStack.py


from linkedList import LinkedList

class arrayStack(object):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, x):
        self._data.append(x)

    def pop(self):
        if not self._data:
            raise Exception("Empty stack")
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise Exception("empty stack")
        return self._data[-1]

    def printStackItems(self):
        for i in self._data:
            print(self._data[i], end=' ')

class LinkListStack(object):
    def __init__(self):
        self._data = LinkedList()

    def __len__(self):
        return self._data.len

    def push(self, x):
        self._data.add_last(x)

    def pop(self):
        return self._data.remove_last()

    def peek(self):
        last = self._data.get_last()
        print(last.val)
        return last

    def printStackItems(self):
        self._data.print_list()
