class Node:
    def _init_(self, value):
        self.value = value  # Value of the node
        self.left = None    # Left child reference
        self.right = None   # Right child reference

class BinaryTree:
    def _init_(self, root=None):
        self.root = root  # Root node reference

    def _repr_(self):
        return f"Created new Binary Tree Root: {self.root.value if self.root else None}"

    # Task 2 - Tree Information Methods

    def height(self, node):
        """Calculate the maximum depth of the tree"""
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

    def size(self, node):
        """Count the total number of nodes"""
        if node is None:
            return 0
        left_size = self.size(node.left)
        right_size = self.size(node.right)
        return left_size + right_size + 1

    def count_leaves(self, node):
        """Count number of leaf nodes"""
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    def is_full_binary_tree(self, node):
        """Check if the tree is a full binary tree"""
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right)
        return False

    def is_complete_binary_tree(self, node, index, total_nodes):
        """Check if the tree is a complete binary tree"""
        if node is None:
            return True
        if index >= total_nodes:
            return False
        return (self.is_complete_binary_tree(node.left, 2 * index + 1, total_nodes) and
                self.is_complete_binary_tree(node.right, 2 * index + 2, total_nodes))

    def is_complete(self):
        """Check if the tree is a complete binary tree (public method)"""
        total_nodes = self.size(self.root)
        return self.is_complete_binary_tree(self.root, 0, total_nodes)


# Test the Binary Tree Implementation
if __name__ == "_main_":
    # Create some nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    # Manually link the nodes
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    # Create a BinaryTree with the root node
    tree = BinaryTree(node1)

    # Print tree structure
    print(tree)

    # Tree Information Methods
    print(f"Tree Height: {tree.height(tree.root)}")
    print(f"Total Nodes: {tree.size(tree.root)}")
    print(f"Leaf Nodes Count: {tree.count_leaves(tree.root)}")
    print(f"Is Full Binary Tree: {tree.is_full_binary_tree(tree.root)}")
    print(f"Is Complete Binary Tree: {tree.is_complete()}")