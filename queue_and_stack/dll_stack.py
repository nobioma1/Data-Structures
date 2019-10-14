from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList(node=None)

    def push(self, value):
        self.size = self.storage.__len__()
        value = self.storage.add_to_tail(value)
        return value

    def pop(self):
        if self.storage.tail == None:
            return None
        self.size = self.storage.__len__()
        value = self.storage.remove_from_tail()
        return value

    def len(self):
        return self.storage.__len__()
