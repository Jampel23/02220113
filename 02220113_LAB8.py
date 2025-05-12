class Node:
    def __init__(self, val, color='RED', left=None, right=None, parent=None):
        self.val = val
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

    def is_red(self):
        return self.color == 'RED'

    def __str__(self):
        return f"{self.val}({self.color})"


class NilNode(Node):
    def __init__(self):
        super().__init__(val=None, color='BLACK')
        self.left = self
        self.right = self
        self.parent = None

    def __str__(self):
        return "NIL"


NIL = NilNode()


class RedBlackTree:
    def __init__(self):
        self.root = NIL

    def insert(self, val):
        new_node = Node(val, color='RED', left=NIL, right=NIL)
        self._bst_insert(new_node)
        self._fix_insert(new_node)

    def _bst_insert(self, node):
        parent = None
        current = self.root
        while current != NIL:
            parent = current
            if node.val < current.val:
                current = current.left
            else:
                current = current.right
        node.parent = parent
        if not parent:
            self.root = node
        elif node.val < parent.val:
            parent.left = node
        else:
            parent.right = node

    def _fix_insert(self, node):
        while node != self.root and node.parent.is_red():
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.is_red():
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.is_red():
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._left_rotate(node.parent.parent)
        self.root.color = 'BLACK'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != NIL:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != NIL:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node == NIL or val == node.val:
            return node != NIL
        if val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

    def get_black_height(self):
        def height(node):
            if node == NIL:
                return 1
            return height(node.left) + (1 if node.color == 'BLACK' else 0)
        return height(self.root)

    def print_tree(self, node=None, indent="", last=True):
        if node is None:
            node = self.root
        if node != NIL:
            print(indent, "`---- " if last else "|--- ", node, sep="")
            indent += "   " if last else "|  "
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)

# === Example Usage ===
rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(20)
rb_tree.insert(30)

print("Red-Black Tree:")
rb_tree.print_tree()

print("Black Height:", rb_tree.get_black_height())
print("Search 20:", rb_tree.search(20))
print("Search 40:", rb_tree.search(40))

