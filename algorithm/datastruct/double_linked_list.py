class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class doubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.head.next = self.tail
        self.tail.prev = self.head