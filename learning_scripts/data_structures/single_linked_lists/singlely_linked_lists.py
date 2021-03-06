# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
        
#     def print_list(self):
#         cur_node = self.head
#         while cur_node:
#             print(cur_node.data)
#             cur_node = cur_node.next

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return
        
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node 

#     def prepend(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def insert_after_node(self, prev_node, data):

#         if not prev_node:
#             print("Previous node not in list")
#             return

#         new_node = Node(data)
#         new_node.next = prev_node.next
#         prev_node.next = new_node

#     def delete_node(self, key):
#         cur_node = self.head
#         if cur_node and cur_node.data == key:
#             self.head = cur_node.next
#             cur_node = None
#             return

#         prev = None
#         while cur_node and cur_node.data != key:
#             prev = cur_node
#             cur_node = cur_node.next
        
#         if cur_node == None:
#             print("Element to be deleted is not in list")
#             return
#         else:
#             prev.next = cur_node.next
#             cur_node = None

#     def delete_node_by_pos(self, node_pos):
#         cur_node = self.head
#         if node_pos == 0:
#             self.head = cur_node.next 
#             cur_node = None
#             return

#         prev = None 
#         count = 1
#         while cur_node and count != node_pos:
#             prev = cur_node
#             cur_node = cur_node.next
#             count += 1

#         if cur_node is None:
#             print("Position greater than number of elements")
#             return

#         prev.next = cur_node.next
#         cur_node = None

#     def len_iterative(self):
#         count = 0
#         cur_node = self.head

#         while cur_node:
#             count += 1
#             cur_node = cur_node.next
#         return count

#     def len_recursive(self, node):
#         if node is None:
#             return 0
#         return 1 + self.len_recursive(node.next)
         
#     def node_swap(self, key1, key2):
#         if key1 == key2:
#             return
        
#         prev1 = None
#         curr1 = self.head
#         while curr1 and curr1.data != key1:
#             prev1 = curr1
#             curr1 = curr1.next

#         prev2 = None
#         curr2 = self.head
#         while curr2 and curr2.data != key2:
#             prev2 = curr2
#             curr2 = curr2.next

#         if not curr1 or not curr2:
#             return

#         if prev1:
#             prev1.next = curr2
#         else:
#             self.head =  curr2

#         if prev2:
#             prev2.next = curr1
#         else:
#             self.head = curr1

#         curr1.next, curr2.next = curr2.next, curr1.next

#     def print_helper(self, node, name):
#         if node is None:
#             print(name + ": None")
#         else:
#             print(name + ":" + node.data)

#     def reverse_iterative(self):
#         prev = None
#         cur = self.head
#         while cur:
#             nxt = cur.next
#             cur.next = prev
#             self.print_helper(nxt, "NXT")
#             self.print_helper(prev, "PREV")
#             self.print_helper(cur, "CUR")
#             self.print_helper(cur.next, "CUR.NEXT")
#             prev = cur
#             cur = nxt 
#         self.head = prev
        
#     def reverse_recursive(self):

#         def _reverse_recursive(cur, prev):
#             if not cur:
#                 return prev

#             nxt = cur.next
#             cur.next = prev
#             prev = cur
#             cur = nxt 
#             return _reverse_recursive(cur, prev)

#         self.head = _reverse_recursive(cur=self.head, prev=None)

#     def merge_sorted(self, llist):
#         p = self.head
#         q = llist.head
#         s = None
#         s = p
#         p = s.next
#         print(q)
#         print(p.data)
#         print(s.next)
#         if not p:
#             return q
#         if not q:
#             # return p

#         # if p and q:
#         #     if p.data <= q.data:
#         #         s = p
#         #         p = s.next
#         #     else:
#         #         s = q
#         #         q = s.next
#         #     new_head = s 
#         # while p and q:
#         #     if p.data <= q.data:
#         #         s.next = p
#         #         s = p
#         #         p = s.next
#         #     else:
#         #         s.next = q
#         #         s = q
#         #         q = s.next
#         # if not p:
#         #     s.next = q
#         # if not q:
#         #     s.next = p
#         # return new_head



# # Merge two sorted lists
# llist1 = LinkedList()
# llist2 = LinkedList()

# llist1.append(1)
# llist1.append(5)
# llist1.append(7)
# llist1.append(9)
# llist1.append(10)

# llist2.append(2)
# llist2.append(3)
# llist2.append(4)
# llist2.append(6)
# llist2.append(8)

# llist1.print_list()
# print("\n")
# llist2.print_list()
# llist3 = LinkedList()

# llist1.merge_sorted(llist3)
# llist1.print_list()








# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# llist.insert_after_node(llist.head.next, "E")
# llist.delete_node("B")
# llist.print_list()

# print(llist.len_iterative())
# print(llist.len_recursive(llist.head))

# Node swap data
# llist2 = LinkedList()
# llist2.append("A")
# llist2.append("B")
# llist2.append("C")
# llist2.append("D")

# llist2.node_swap("A", "D")
# llist2.print_list()


# Reverse list
# A -> B -> C -> D -> 0
# D -> C -> B -> A -> 0
# A <- B <- C <- D <- 0

# llist2.reverse_iterative()
# llist2.reverse_recursive()
# llist2.print_list()