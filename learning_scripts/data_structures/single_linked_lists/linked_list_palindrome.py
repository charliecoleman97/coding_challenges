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

    def is_palindrome(self):
        # Method 1
        # cur_node = self.head
        # s = ""
        # while cur_node:
        #     s += cur_node.data
        #     cur_node = cur_node.next
        # return s ==s[::-1]

        # Method 2
        cur_node = self.head
        s = []
        while cur_node:
            s.append(cur_node.data)
            cur_node = cur_node.next
        cur_node = self.head
        while cur_node:
            data = s.pop()
            if cur_node.data != data:
                return False
            cur_node = cur_node.next
        return True

    



llist1 = LinkedList()
llist1.append("R")
llist1.append("A")
llist1.append("C")
llist1.append("E")
llist1.append("C")
llist1.append("A")
llist1.append("R")

llist2 = LinkedList()
llist2.append("A")
llist2.append("B")
llist2.append("C")

print(llist1.is_palindrome())
print(llist2.is_palindrome())



