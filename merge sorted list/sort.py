class Node:
    def __init__(self,value = 0):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next

def merge

if __name__ == '__main__':

    list = LinkedList()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    list.head = node1
    list.head.next = node2
    node2.next = node3
    node3.next = node4


    list2 = LinkedList()

    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)

    list2.head = node5
    list2.head.next = node6
    node6.next = node7
    node7.next = node8


    # list.printList()
    list2.printList()