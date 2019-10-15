from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList(node=None)

    def push(self, value):
        value = self.storage.add_to_tail(value)
        self.size += 1

        return value

    def pop(self):
        if self.storage.tail == None:
            return None
        value = self.storage.remove_from_tail()
        self.size -= 1

        return value

    def len(self):
        return self.size
