"""
@jetou
@date : 2017/12/13
@algorithms: binomial_heap
"""

class Node:
    def __init__(self, value=0.0, degree=0.0, childs=None, sibling=None, parent=None):
        self.value = value
        self.degree = degree
        self.childs = childs
        self.sibling = sibling
        self.parent = parent

class bin_heap:
    def __init__(self):
        self.head = None

    def bin_heap_min(self):
        y = None
        x = self.head
        minimum = 100000
        while x != None:
            if x.key < minimum:
                minimum = x.key
                y = x

            x = x.sibling

        return y

    def bin_heap_link(self, y, z):
        y.parent = z
        y.sibling = z.childs
        z.childs = y
        z.degree = z.degree + 1

    def bin_heap_merge(self, h1, h2):
        pre_H3 = None

        if h1 != None and h2 != None:
            firstHeap = h1
            secondHeap = h2

            while firstHeap != None and secondHeap != None:
                if firstHeap.degree <= secondHeap.degree:
                    h3 = firstHeap
                    firstHeap = firstHeap.sibling
                else:
                    h3 = secondHeap
                    secondHeap = secondHeap.sibling

                if pre_H3 == None:
                    pre_H3 = h3
                    heap = h3
                else:
                    pre_H3.sibling = h3
                    pre_H3 = h3

                if firstHeap != None:
                    h3.sibling = firstHeap
                else:
                    h3.sibling = secondHeap

        elif h1 != None:
            heap = h1
        else:
            heap = h2

        h1 = h2 = None

        return heap

    def bin_heap_union(self, h1, h2):
        heap = self.bin_heap_merge(h1, h2)
        if (heap == None):
            return heap

        pre_x = None
        x = heap
        next_x = x.sibling

        while next_x != None:
            if (x.degree != next_x.degree) or (next_x.sibling != None and next_x.degree == next_x.sibling.degree):
                pre_x = x
                x = next_x
            elif x.value <= next_x.value:
                x.sibling = next_x.sibling
                self.bin_heap_link(next_x, x)
            else:
                if pre_x == None:
                    heap = next_x
                else:
                    pre_x.sibling = next_x

                self.bin_heap_link(x, next_x)
                x = next_x

            next_x = x.sibling

        return heap

    def bin_heap_insert(self, x):
        new_node = bin_heap()
        x.parent = None
        x.childs = None
        x.sibling = None
        x.degree = 0
        new_node = x
        self.head = self.bin_heap_union(self.head, new_node)

    def bin_heap_insertarray(self, array):
        for i in array:
            nodes = Node(i)
            self.bin_heap_insert(nodes)

    def print_bin_heap(self, head):
        if head == None:
            return "binomial heap is empty"
        position = head
        while position != None:
            print "(",
            print position.value,
            if position.childs != None:
                self.print_bin_heap(position.childs)
            print ")",

            position = position.sibling


k = [15, 41, 28, 33, 25, 7, 12]
heap = bin_heap()
heap.bin_heap_insertarray(k)
heap.print_bin_heap(heap.head)




