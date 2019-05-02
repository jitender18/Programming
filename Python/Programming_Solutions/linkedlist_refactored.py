# --- Directions
# Implement classes Node and Linked Lists
# See 'directions' document in misc folder
# NOTE:  These solutions are refactored so that methods reuse code in other
# methods, rather than re-creating code.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def clear(self):
        self.head = None

    def for_each(self, fn):
        node = self.head
        while node:
            fn(node)
            node = node.next

    def get_at(self, index):
        counter = 0
        node = self.head
        while node:
            if counter == index:
                return node
            counter += 1
            node = node.next
        return None

    def get_first(self):
        return self.head

    def get_last(self):
        return self.get_at(self.size() - 1)

    def insert_at(self, data, index):
        if not self.head:
            self.head = Node(data)
            return
        if index == 0:
            self.head = Node(data, self.head)
            return
        prev = self.get_at(index - 1) or self.get_last()
        prev.next = Node(data, prev.next)

    def insert_first(self, data):
        self.insert_at(data, 0)

    def insert_last(self, data):
        self.insert_at(data, self.size())

    def remove_at(self, index):
        if not self.head:
            return None
        if index == 0:
            self.head = self.head.next
            return
        prev = self.get_at(index - 1)
        if not prev or not prev.next:
            return
        prev.next = prev.next.next

    def remove_first(self):
        self.remove_at(0)

    def remove_last(self):
        self.remove_at(self.size() - 1)

    def size(self):
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.next
        return counter
