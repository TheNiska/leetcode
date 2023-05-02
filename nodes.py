class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def addTail(self, val):
        if self.head:
            el = self.head
            while el.next:
                el = el.next
            el.next = Node(val)
        else:
            self.head = Node(val)

    def addHead(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def add(self, val, index):
        if index == 0: self.addHead(val)
        else:
            el = self.head
            for i in range(1, index):
                el = el.next
                if el is None: return
            prev = el
            node = Node(val)
            node.next = prev.next
            prev.next = node



    def show(self):
        el = self.head
        print(f"({el.val})[{0}] --> ", end='')
        i = 0
        while True:
            i += 1
            if el.next is None:
                print(f"(None)[{i}]")
                break
            el = el.next
            print(f"({el.val})[{i}] --> ", end='')





lst = LinkedList()
for i in range(10):
    lst.addTail(i)
lst.show()


        
