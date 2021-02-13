class SList:
    class Node:
        def __init__(self,item,next):
            self.item = item
            self.next = next
    def __init__(self):
        self.size = 0
        self.head = SList.Node(None,None)

    def insert_item(self,item):
        if self.size :
            self.head.next = SList.Node(item,None)
        else:
            while self.head.next == None:
                self.head.next = self.head.next.next
                