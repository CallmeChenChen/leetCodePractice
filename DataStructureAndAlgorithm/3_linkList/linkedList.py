# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = Node() # dummy node
        self.len = 0

    def get_first(self):
        if not self.head.next:
            raise Exception('LinkedList is Empty')
        return self.head.next
    def get_last(self):
        if not self.head.next:
            raise Exception('LinkedList is Empty')
        node = self.head
        while node.next != None:
            node = node.next
        return node

    def add_first(self, value):
        node = Node(val=value)
        node.next = self.head.next
        self.head.next = node
        self.len += 1

    def add_last(self, value):
        new_node = Node(val=value)
        now_node = self.head
        while now_node.next != None:
            now_node = now_node.next
        now_node.next = new_node
        self.len += 1

    def remove_first(self):
        if not self.head.next:
            raise Exception('LinkedList is Empty')
        remove_value = self.head.next.val
        self.head.next = self.head.next.next
        self.len -= 1
        return remove_value

    def remove_last(self):
        if not self.head.next:
            raise Exception('LinkedList is Empty')
        node = self.head.next
        prev = self.head
        while node.next != None:
            prev = node
            node = node.next
        remove_value = node.val
        prev.next = None
        self.len -= 1
        return remove_value

    def insert_at(self, value, index):
        if index < 0 or index > self.len:
            raise Exception('index bigger than LinkedList length')
        if not self.head.next:
            raise Exception('LinkedList is Empty')
        new_node = Node(val=value)
        node = self.head
        for i in range(index):
            node = node.next
        new_node.next = node.next
        node.next = new_node
        self.len += 1

    def remove_at(self, index):
        if index < 0 or index > self.len:
            raise Exception('index bigger than LinkedList length')
        if not self.head.next:
            raise Exception('LinkedList is Empty')
        node = self.head
        for i in range(index):
            node = node.next
        remove_value = node.next.val
        node.next = node.next.next
        return remove_value

    def print_list(self):
        node = self.head.next
        while node.next != None:
            print(node.val, end=' ')
            node = node.next
        print(node.val, end=' ')
        print()

if __name__ == '__main__':
    ll = LinkedList()
    ll.add_first(10)
    ll.add_first(12)
    ll.add_first(13)
    ll.add_last(1)
    ll.add_last(5)
    ll.add_last(7)
    ll.print_list()
    print('remove first value: ', ll.remove_first())
    ll.print_list()
    print('remove last value: ', ll.remove_last())
    ll.print_list()
    ll.insert_at(88, 2)
    ll.print_list()
    print('remove value: ', ll.remove_at(2))
    ll.print_list()

    print(ll.get_first().val)
    print(ll.get_last().val)
