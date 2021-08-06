class SList:
    class Node:
        def __init__(self,item,link):
            self.item = item
            self.next = link
        
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def insert_front(self,item):
        if self.is_empty : 
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def insert_after(self,target,item):
        p = self.head
        while p:
            if p.item == target:
                break
            p = p.next
        p.next = self.Node(item,p.next)
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self,target):
        if self.is_empty():
            raise EmptyError('Underflow')
        else:
            p = self.head
            while p.next:
                if p.next.item == target:
                    break
                p.next = p.next.next

    def search(self,target):
        if self.is_empty():
            print("SList is empty.")
        else:
            p = self.head
            for i in range(self.size):
                if target == p.item:
                    return i
                p = p.next
            return None

    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, end = '->')
            else:
                print(p.item)
            p = p.next

fruit = SList()
fruit.insert_front('orange')
fruit.insert_front('grape')
fruit.print_list()


            
            


        
            