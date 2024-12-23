class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class singleLinkedList:
    def __init__(self, head=None):
        self.head = head
    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
