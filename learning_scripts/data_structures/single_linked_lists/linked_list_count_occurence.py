class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedLast:
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

    def count_occurence_of_all(self):
        cur_node = self.head
        occurence = dict()
        while cur_node:
            if cur_node.data in occurence:
                occurence[cur_node.data] += 1
            else:
                occurence[cur_node.data] = 1
            cur_node = cur_node.next
        return occurence

    def count_occurence_specific_data(self, data):
        cur_node = self.head
        count = 0
        while cur_node:
            if cur_node.data == data:
                count += 1
            cur_node = cur_node.next
        return count


    def occurence_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.occurence_recursive(node.next, data)
        else:
            return self.occurence_recursive(node.next, data)




llist = LinkedLast()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("B")
llist.append("A")
llist.append("B")
llist.append("C")

llist.print_list()
print("\n")
print(llist.count_occurence_of_all())
print("\n")
print(llist.count_occurence_specific_data("B"))
print(llist.occurence_recursive(llist.head, "B"))



    