class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

root = Node(1)
node1 = Node(2)
node2 = Node(3)

root.left = node1
root.right = node2

