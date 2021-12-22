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

    def palindrome(self):
        # method 1
        # cur_node = self.head
        # s = []
        # while cur_node:
        #     s.append(cur_node.data)
        #     cur_node = cur_node.next
        # cur_node = self.head
        # while cur_node:
        #     data = s.pop()
        #     if cur_node.data != data:
        #         return False
        #     cur_node = cur_node.data
        #     return True

        # # method 2
        cur_node = self.head
        s = ""
        while cur_node:
            s += cur_node.data
            cur_node = cur_node.next
        return s == s[::-1]

    def nth_to_last(self, key):
        p = self.head
        q = self.head
        count = 0

        while q and count < key:
            q = q.next
            count += 1
        
        while p and q:
            p = p.next
            q = q.next
        return p.data

    def count_occurence(self, key):
        cur_node = self.head
        count = 0
        while cur_node:
            if cur_node.data == key:
                count += 1
            cur_node = cur_node.next
        return count

    def rotate_list(self, key):
        p = self.head
        q = self.head
        count = 1

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
        



# Rotate list
# 1 -> 2 -> 3 -> 4 -> 5 -> 6
# 4 -> 5 -> 6 -> 1 -> 2 -> 3

llist2 = LinkedList()
llist2.append(1)
llist2.append(2)
llist2.append(3)
llist2.append(3)
llist2.append(4)
llist2.append(5)
llist2.append(6)

llist2.remove_duplicates()
# llist2.rotate_list(3)
llist2.print_list()
    



        

# PALINDROME
# llist = LinkedList()
# llist.append("R")
# llist.append("A")
# llist.append("C")
# llist.append("E")
# llist.append("C")
# llist.append("A")
# llist.append("R")


# llist2 = LinkedList()
# llist2.append ("A")
# llist2.append ("B")
# llist2.append ("C")

# llist.print_list()
# print("\n")
# llist2.print_list()
# print(llist.palindrome())
# print(llist2.palindrome())

# NTH TO last 
llist1 = LinkedList()
llist1.append(1)
llist1.append(2)
llist1.append(4)
llist1.append(5)
llist1.append(7)
llist1.append(7)
llist1.append(10)

# print(llist1.nth_to_last(4))
# print(llist1.count_occurence(7))






