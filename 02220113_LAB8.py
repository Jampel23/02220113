class Node:
    def __init__(self, value, color="RED", left=None, right=None, parent=None):
        self.value = value
        self.color = color  # "RED" or "BLACK"
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(value=None, color="BLACK")  # Sentinel node
        self.root = self.NIL

    def insert(self, value):
        new_node = Node(value=value, color="RED", left=self.NIL, right=self.NIL)
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if not parent:
            self.root = new_node
        elif value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
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

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
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

    def fix_insert(self, z):
        while z.parent and z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.left_rotate(z.parent.parent)
        self.root.color = "BLACK"

    def search(self, value):
        current = self.root
        while current != self.NIL and current.value != value:
            current = current.left if value < current.value else current.right
        return current if current != self.NIL else None

    def get_black_height(self):
        def count_black(node):
            if node == self.NIL:
                return 1
            left_height = count_black(node.left)
            return left_height + (1 if node.color == "BLACK" else 0)
        return count_black(self.root)

    def print_tree(self, node=None, indent="", last=True):
        if node is None:
            node = self.root
        if node != self.NIL:
            print(indent + ("└── " if last else "├── ") + f"{node.value} ({node.color})")
            indent += "    " if last else "│   "
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)


# Example usage
if __name__ == "__main__":
    rb_tree = RedBlackTree()
    for value in [10, 20, 30, 15, 25, 5, 1]:
        rb_tree.insert(value)

    print("Red-Black Tree Structure:")
    rb_tree.print_tree()

    print("\nSearch for 15:", "Found" if rb_tree.search(15) else "Not Found")
    print("Search for 99:", "Found" if rb_tree.search(99) else "Not Found")
    print("Black Height:", rb_tree.get_black_height())
