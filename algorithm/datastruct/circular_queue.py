class CircularQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = 1

    def isFull(self):
        return (self.rear+1)%self.capacity == self.front
    
    def isEmpty(self):
        return self.front == -1
    
    def enqueue(self, item):
        if self.isFull():
            print("queue is full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        if self.front == -1:
            self.front = self.rear 

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty.")
            return None

        result = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return result
    
    def front_element(self):
        if self.isEmpty():
            print("Queue is empty.")
            return None
        return self.queue[self.front]

    def rear_element(self):
        if self.isEmpty():
            print("Queue is empty.")
            return None
        return self.queue[self.rear]