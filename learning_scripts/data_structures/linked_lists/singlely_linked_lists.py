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

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node not in list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node == None:
            print("Element to be deleted is not in list")
            return
        else:
            prev.next = cur_node.next
            cur_node = None

    def delete_node_by_pos(self, node_pos):
        cur_node = self.head
        if node_pos == 0:
            self.head = cur_node.next 
            cur_node = None
            return

        prev = None 
        count = 1
        while cur_node and count != node_pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            print("Position greater than number of elements")
            return

        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
         
    def node_swap(self, key1, key2):
        if key1 == key2:
            return
        
        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head =  curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next


        

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
# llist.insert_after_node(llist.head.next, "E")
llist.delete_node("B")
# llist.print_list()

# print(llist.len_iterative())
# print(llist.len_recursive(llist.head))

# Node swap data
llist2 = LinkedList()
llist2.append("A")
llist2.append("B")
llist2.append("C")
llist2.append("D")

llist2.node_swap("A", "D")
llist2.print_list()