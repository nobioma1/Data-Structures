from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList(node=None)

    def enqueue(self, value):
        value = self.storage.add_to_tail(value)
        self.size += 1

        return value

    def dequeue(self):
        if self.storage.head == None:
            return None
        value = self.storage.remove_from_head()
        self.size -= 1

        return value

    def len(self):
        return self.size
