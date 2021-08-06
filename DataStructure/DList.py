class DList:
    class Node:
        def __init__(self,prev,item,link):
            self.prev = prev
            self.item = item
            self.next = link

    def __init__(self):
        self.size = 0
        self.head = self.Node(None,None,None)
        self.tail = self.Node(self.head,None,None)
        self.head.next = self.tail

    def is_empty(self):
        return self.size == 0

    def insert_front(self,item):
        if self.is_empty():
            