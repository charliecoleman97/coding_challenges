import re


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def append_list(self, llist):
        p = self.head
        q = llist.head

        if p and q is None:
            return

        while p.next:
            p = p.next 
        p.next = q


llist1 = LinkedList()
llist2 = LinkedList()

llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2.append(8)
llist2.append(4)
llist2.append(2)

llist1.append_list(llist2)
llist1.print_list()