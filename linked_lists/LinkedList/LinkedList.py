from LinkedList.Node import Node
class LinkedList:
    def __init__(self):
        # just create a null header node
        self.head = Node(None)

    def addToTail(self, value):
        toAppend = Node(value)
        curr = self.head
        while(curr.next != None):
            curr = curr.next
        
        # once we have found the end, append.
        curr.next = toAppend

    def printList(self):
        curr = self.head
        while(curr.next != None):
            print(curr.value)
            curr = curr.next
        print(curr.value)
    