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
    
    def delete_node(self, key):
        cur_node = self.head
        prev = None

        if cur_node == self.head and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None

        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        
        if not cur_node:
            print("Specifed node not in list")
            return

        prev.next = cur_node.next
        cur_node = None

    def is_palindrome(self):
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]

    def rotate_list(self, key):
        p = self.head
        q = self.head
        prev = None
        count = 0

        while p and count != key:
            prev = p
            p = p.next
            count += 1
        p = prev
        
        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None

    




llist = LinkedList()
llist.append(2)
llist.append(4)
llist.append(6)
llist.append(8)
llist.append(10)
llist.append(12)
llist.append(14)

print(llist.rotate_list(3))

llist.print_list()





