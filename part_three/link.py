"""
@jetou
@date : 2017/12/10
@algorithms: link
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def append(self, this_node):
        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(data=this_node)

        if self.is_empty():
            self.head = this_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = this_node
        self.length += 1

    def head_insert(self, this_node):
        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(data=this_node)
        if self.is_empty():
            self.head = this_node
        else:
            this_node.next = self.head
            self.head = this_node

    def print_linked_list(self):
        if self.is_empty():
            print "Linked list's length is 0"
        else:
            node = self.head
            print "Head -->", node.data
            while node.next:
                node = node.next
                print "-->", node.data
            print "-->Node. Linked node finished"

    def reversed(self):
        if self.head == None or self.head.next == None:
            return self.head

        p = self.head
        cur = None
        pre = None
        while p is not None:
            cur = p.next
            p.next = pre
            pre = p
            p = cur
        self.head = pre




node1 = Node("asda")
linked_list = LinkedList()
linked_list.append(node1)
linked_list.append("Sdaw")
linked_list.append("wqeqwe")
linked_list.append("wqrrtrytr")
linked_list.head_insert("wqeqwe")
linked_list.print_linked_list()
linked_list.reversed()
linked_list.print_linked_list()
