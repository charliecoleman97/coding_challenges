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

    def count_occurences(self):
        cur_node = self.head
        letter_count = dict()
        while cur_node:
            if cur_node.data in letter_count:
                letter_count[cur_node.data] += 1
            else:
                letter_count[cur_node.data] = 1
            cur_node = cur_node.next
        return letter_count

    def delete_node_at_pos(self, pos):
        cur_node = self.head
        if pos == 1:
            self.head = cur_node.next
            cur_node = None
        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None

    def is_palindrome(self):
        str = ""
        cur_node = self.head
        while cur_node:
            str += cur_node.data
            cur_node = cur_node.next
        return str == str[::-1]

        


        

    

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("B")
llist.append("A")
llist.append("B")
llist.append("C")


llist.print_list()
# print(llist.count_occurences())
print(llist.is_palindrome())
