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

    def swapNodes(self):
        temp = self.head

        if temp == None or temp.next == None:
            return
        
        self.head = temp.next
        while(temp):

            secondaryTemp = temp.next.next
            temp.next.next = temp
            if secondaryTemp:
                if secondaryTemp.next:
                    temp.next = secondaryTemp.next
                    temp = secondaryTemp
                else:
                    temp.next = secondaryTemp
                    temp = None
                    
                
            else:
                temp.next = None
                temp = secondaryTemp
            
            



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

    # list.printList()
    list.swapNodes()
    list.printList()