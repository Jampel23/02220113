class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance_factor(root)

        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, value):
        if not root:
            return root
        elif value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self._min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance_factor(root)

        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotate(root)
        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotate(root)
        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def _min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def search(self, root, value):
        if not root or root.value == value:
            return root
        elif value < root.value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def search_value(self, value):
        return self.search(self.root, value)

    def print_tree(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.value))
            if root.left is not None or root.right is not None:
                if root.left:
                    self.print_tree(root.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if root.right:
                    self.print_tree(root.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")
        else:
            print(" " * (level * 4) + prefix + "None")
            
if __name__ == "__main__":
    tree = AVLTree()
    tree.insert_value(10)
    tree.insert_value(20)
    tree.insert_value(30)
    tree.insert_value(40)
    tree.insert_value(50)

    print("Tree after insertions:")
    tree.print_tree(tree.root)

    tree.delete_value(20)
    print("\nTree after deletion of 20:")
    tree.print_tree(tree.root)

    result = tree.search_value(30)
    if result:
        print("\nNode 30 found.")
    else:
        print("\nNode 30 not found.")
