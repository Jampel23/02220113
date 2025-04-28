class Node:
    def __init__(self, value):
        self.value = value      # Value of the node
        self.left = None        # Left child reference
        self.right = None       # Right child reference

class BinaryTree:
    def __init__(self, root_value=None):
        if root_value:
            self.root = Node(root_value)   # Initialize with a root node if value provided
        else:
            self.root = None               # Otherwise, empty tree
        print("Created new Binary Tree")
        print(f"Root: {self.root.value if self.root else None}")

# Example usage
if __name__ == "__main__":
    tree = BinaryTree()  # Creating an empty BinaryTree
