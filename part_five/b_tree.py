"""
@jetou
@date : 2017/12/13
@algorithms: b_tree
"""
class b_tree_node:
    def __init__(self, T):
        self.n = 0
        self.key = [None] * (2 * T - 1)
        self.c = [None] * (2 * T)
        self.leaf = True

class b_tree:
    def __init__(self, degree):
        self.t = degree
        self.root = b_tree_node(degree)

    def disk_write(self, x):
        pass

    def disk_read(self, x):
        pass

    def split_child(self, x, i):
        t = self.t
        z = b_tree_node(t)
        y = x.c[i]
        z.leaf = y.leaf
        z.n = t - 1
        for j in range(t - 1):
            z.key[j] = y.key[j + t]

        if not y.leaf:
            for j in range(t):
                z.c[j] = y.c[j + t]
        y.n = t - 1
        for j in range(x.n, i - 1, -1):
            x.c[j + 1] = x.c[j]
        x.c[i + 1] = z
        for j in range(x.n - 1, i - 2, -1):
            x.key[j + 1] = x.key[j]
        x.key[i] = y.key[t - 1]
        x.n += 1
        self.disk_write(y)
        self.disk_write(z)
        self.disk_write(x)

    def insert(self, k):
        t = self.t
        r = self.root
        if r.n == 2 * t - 1:
            s = b_tree_node(t)
            self.root = s
            s.leaf = False
            s.n = 0
            s.c[0] = r
            self.split_child(s, 0)
            self.insert_nonfull(s, k)
        else:
            self.insert_nonfull(r, k)

    def insert_nonfull(self, x, k):
        t = self.t
        i = x.n - 1
        if x.leaf:
            while i >= 0 and k < x.key[i]:
                x.key[i + 1] = x.key[i]
                i -= 1
            x.key[i + 1] = k
            x.n += 1
            self.disk_write(x)
        else:
            while i >= 0 and k < x.key[i]:
                i -= 1
            i += 1
            self.disk_read(x.c[i])
            if x.c[i].n == 2 * t - 1:
                self.split_child(x, i)
                if k > x.key[i]:
                    i += 1
            self.insert_nonfull(x.c[i], k)

    def display(self):
        def display_sub(x, space):
            if x is None:
                return
            print(' ' * space + '[' + ' '.join(map(str, x.key[:x.n])) + ']')
            for c in x.c[:x.n + 1]:
                display_sub(c, space + 4)
        display_sub(self.root, 0)



v = ['F', 'S', 'Q', 'K', 'C', 'L', 'H', 'T', 'V', 'W', 'M', 'R',
             'N', 'P', 'A', 'B', 'X', 'Y', 'D', 'Z', 'E']
A = ['A', 'C', 'D', 'E', 'G', 'J', 'K', 'M', 'N', 'O', 'P', 'R',
     'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
tree = b_tree(3)
for c in A:
    tree.insert(c)
tree.display()
tree.insert('B')
tree.display()