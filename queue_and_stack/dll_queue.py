from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList(node=None)

    def enqueue(self, value):
        self.size = self.storage.__len__()
        value = self.storage.add_to_tail(value)
        return value

    def dequeue(self):
        if self.storage.head == None:
            return None
        self.size = self.storage.__len__()
        value = self.storage.remove_from_head()
        return value

    def len(self):
        return self.storage.__len__()
