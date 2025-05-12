class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self._update_height(z)
        self._update_height(y)
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self._update_height(z)
        self._update_height(y)
        return y

    def _insert(self, node, value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        self._update_height(node)
        balance = self._balance_factor(node)

        if balance > 1 and value < node.left.value:
            return self._right_rotate(node)
        if balance < -1 and value > node.right.value:
            return self._left_rotate(node)
        if balance > 1 and value > node.left.value:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and value < node.right.value:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _delete(self, node, value):
        if not node:
            return node
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        self._update_height(node)
        balance = self._balance_factor(node)

        if balance > 1 and self._balance_factor(node.left) >= 0:
            return self._right_rotate(node)
        if balance < -1 and self._balance_factor(node.right) <= 0:
            return self._left_rotate(node)
        if balance > 1 and self._balance_factor(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._balance_factor(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _search(self, node, value):
        if not node or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def search(self, value):
        return self._search(self.root, value)

    def get_height(self):
        return self._height(self.root)

    def is_balanced(self):
        return abs(self._balance_factor(self.root)) <= 1
    
    
avl_tree = AVLTree()
avl_tree.insert(10)
avl_tree.insert(20)
avl_tree.insert(30)

print("Is tree balanced?", avl_tree.is_balanced())  # Output: True
print("Tree height:", avl_tree.get_height())        # Output: 2

avl_tree.delete(20)
print("Is tree balanced after deletion?", avl_tree.is_balanced())  # Output: True
print("Tree height after deletion:", avl_tree.get_height())        # Output: 2

node = avl_tree.search(30)
print("Node found?" if node else "Node not found")  # Output: Node found
