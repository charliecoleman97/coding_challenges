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

    def list_length(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
        

    def nth_to_last(self, n):
        # Method 1
        # total_len = self.list_length()
        # cur_node = self.head
        # while cur_node:
        #     if total_len == n:
        #         print(cur_node.data)
        #         return
        #     total_len -= 1
        #     cur_node = cur_node.next
        # if cur_node is None:
        #     return

        # Method 2
        p = self.head
        q = self.head
        count = 0

        while q and count < n:
            q = q.next 
            count += 1
        
        if not q:
            return

        while p and q:
            p = p.next
            q = q.next 
        return p.data
        


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
# llist.print_list()

print(llist.nth_to_last(2))
        
