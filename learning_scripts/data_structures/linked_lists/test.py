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
        new_node = Node(data)
        if not prev_node:
            return
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

        if not cur_node:
            return
        
        prev.next = cur_node.next
        cur_node = None

    def delete_node_by_pos(self, pos):
        cur_node = self.head
        
        if cur_node and pos == 1:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if not cur_node:
            return

        prev.next = cur_node.next
        cur_node = None

    def list_length(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count +=1
            cur_node = cur_node.next
        return count

    def list_len_recursive(self, node):
        if not node:
            return 0
        return 1 + self.list_len_recursive(node.next)

    def node_swap(self, key1, key2):
        if key1 == key2:
            return

        prev1 = None
        cur1 = self.head
        while cur1 and cur1.data != key1:
            prev1 = cur1
            cur1 = cur1.next

        prev2 = None
        cur2 = self.head
        while cur2 and cur2.data != key2:
            prev2 = cur2
            cur2 = cur2.next
        
        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2

        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1

        cur1.next, cur2.next = cur2.next, cur1.next

    def reverse_list(self):
        cur = self.head
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    def remove_duplicates(self):
        cur_node = self.head
        prev_node = None
        duplicates = dict()

        while cur_node:
            if cur_node.data in duplicates:
                prev_node.next = cur_node.next
                cur_node = None
            else:
                duplicates[cur_node.data] = 1
                prev_node = cur_node
            cur_node = prev_node.next

    

        


# llist = LinkedList()
# llist.append("A") 
# llist.append("B")
# llist.append("C")
# llist.append("D")
# llist.prepend("E")
# llist.delete_node("C")

# llist.insert_after_node(llist.head.next, "E")
# llist.node_swap("D", "C")
# llist.reverse_list()

# Merge two sorted lists
llist1 = LinkedList()
llist2 = LinkedList()

llist1.append(1)
llist1.append(5)
llist1.append(7)
llist1.append(9)
llist1.append(10)
llist1.print_list()
print("\n")
llist2.append(2)
llist2.append(3)
llist2.append(4)
llist2.append(6)
llist2.append(8)
llist2.append(8)
llist2.print_list()
print("\n")

llist1.merge_sorted(llist2)
llist1.remove_duplicates()
llist1.print_list()
# print(llist.list_len_recursive(llist.head))

    

    

        




    


    

        