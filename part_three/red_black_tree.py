"""
@jetou
@date : 2017/12/10
@algorithms: red_black_tree
"""
class Node:
    def __init__(self, key, left=None, right=None, color=None, p=None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right
        self.p = p
        if key == "Nil":
            self.p = self

    def tree_minimum(self, T, x):
        while x.left != T.nil:
            x = x.left
        return x

    def left_rotate(self, T, x):
        y = x.right # suppose y is x's right node
        x.right = y.left
        if y.left != T.nil:
            y.left.p = x
        y.p = x.p
        if x.p == T.nil: #if the father of x is an empty node, then set y as the root node
            T.root = y
        elif x == x.p.left: # if x is left child of its father, then set y to the left child of the father of x
            x.p.left = y
        else:
            x.p.right = y

        y.left = x
        x.p = y

    def right_rotate(self, T, x):
        y = x.left
        x.left = y.right
        if x.right != T.nil:
            y.right.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y

        y.right = x
        x.p = y

    def rb_insert(self, T, z):
        y = T.nil
        x = T.root
        while x != T.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == T.nil:
            T.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = T.nil
        z.right = T.nil
        z.color = "Red"
        self.rb_insert_fixup(T, z)

    def rb_insert_fixup(self, T, z):
        while z.p.color == "Red":
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == "Red":
                    z.p.color = "Black"
                    y.color = "Black"
                    z.p.p.color = "Red"
                    z = z.p.p
                elif z == z.p.right:
                    z = z.p
                    self.left_rotate(T, z)
                z.p.color = "Black"
                if z.p.p != T.nil:
                    z.p.p.color = "Red"
                    self.right_rotate(T, z.p.p)
            else:
                y = z.p.p.left
                if y.color == "Red":
                    z.p.color = "Black"
                    y.color = "Black"
                    z.p.p.color = "Red"
                    z = z.p.p
                elif z == z.p.left:
                    z = z.p
                    self.right_rotate(T, z)
                z.p.color = "Black"
                if z.p.p != T.nil:
                    z.p.p.color = "Red"
                    self.left_rotate(T, z.p.p)
        T.root.color = "Black"

    def rb_transplant(self, T, u, v):
        if u.p == T.nil:
            T.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def rb_delete(self, T, z):
        y = z
        y_original_color = y.color
        if z.left == T.nil:
            x = z.right
            self.rb_transplant(T, z, z.right)
        elif z.right == T.nil:
            x = z.left
            self.rb_transplant(T, z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.rb_transplant(T, y, y.right)
                y.right = z.right
                y.right.p = y
            self.rb_transplant(T, z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == 'Black':
            self.rb_delete_fixup(T, x)

    def rb_delete_fixup(self, T, x):
        while x != T.root and x.color == 'Black':
            if x == x.p.left:
                w = x.p.right
                if w.color == 'Red':
                    w.color = 'Black'
                    x.p.color = 'Red'
                    self.left_rotate(T, x.p)
                    w = x.p.right
                if w.left.color == 'Black' and w.right.color == 'Black':
                    w.color = 'Red'
                    x = x.p
                else:
                    if w.right.color == 'Black':
                        w.left.color = 'Black'
                        w.color = 'Red'
                        self.right_rotate(T, w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = 'Black'
                    w.right.color = 'Black'
                    self.left_rotate(T, x.p)
                    x = T.root
            else:
                w = x.p.left
                if w.color == 'Red':
                    w.color = 'Black'
                    x.p.color = 'Red'
                    self.right_rotate(T, x.p)
                    w = x.p.left
                if w.right.color == 'Black' and w.left.color == 'Black':
                    w.color = 'Red'
                    x = x.p
                else:
                    if w.left.color == 'Black':
                        w.right.color = 'Black'
                        w.color = 'Red'
                        self.left_rotate(T, w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = 'Black'
                    w.left.color = 'Black'
                    self.right_rotate(T, x.p)
                    x = T.root
        x.color = 'Black'

    def inorder_tree_walk(self, T, s, A):
        if s == T.nil :
            return
        if s.left != T.nil:
            self.inorder_tree_walk(T, s.left, A)
        A.append(s)
        if s.right != T.nil:
            self.inorder_tree_walk(T, s.right, A)


class Tree:
    def __init__(self):
        nil = Node("Nil", color="Black")
        self.root = nil
        self.nil = nil

node = [11, 2, 14, 1, 7, 15, 5, 8, 4]
print node
T = Tree()
# T.root.rb_insert(T, Node(11))
# T.root.rb_insert(T, Node(13))
for j in node:
    T.root.rb_insert(T, Node(j))


A = []
T.root.inorder_tree_walk(T, T.root, A)

for i in A:
    T.root.rb_delete(T, i)
    AA = []
    T.root.inorder_tree_walk(T, T.root, AA)
    print "AfterDeleting ", i.key, ".Nodes in tree:", [AAA.key for AAA in AA]

