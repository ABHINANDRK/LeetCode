# enQueue() This operation adds a new node after rear and moves rear to the next node.
# deQueue() This operation removes the front node and moves front to the next node.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return self.front == None

    def enQueue(self, value):
        node = Node(value)
        if self.isEmpty():
            self.front = self.rear = node
            return
        
        self.rear.next = node
        self.rear = node


    def deQueue(self):
        if self.isEmpty():
            return
        
        temp = self.front
        self.front = self.front.next
        temp = None

        if self.isEmpty():
            self.rear = None



if __name__ == '__main__':
    
    queue = Queue()
    queue.enQueue(1)
    queue.enQueue(2)
    queue.enQueue(3)
    queue.deQueue()
    queue.deQueue()
    queue.deQueue()



