class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove_duplicates(self):
        cur_node = self.head
        prev = None
        duplicates = dict()

        while cur_node:
            if cur_node.data in duplicates:
                prev.next = cur_node.next
                cur_node = None
            else:
                duplicates[cur_node.data] = 1
                prev = cur_node
            cur_node = prev.next




llist1 = LinkedList()

llist1.append(1)
llist1.append(6)
llist1.append(1)
llist1.append(4)
llist1.append(2)
llist1.append(2)
llist1.append(4)
llist1.remove_duplicates()

llist1.print_list()
