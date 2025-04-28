class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root = Node(root_value)
        else:
            self.root = None
        print("Created new Binary Tree")
        print("Root:", "None" if self.root is None else self.root.value)

    def height(self):
        return self._height_helper(self.root)

    def _height_helper(self, node):
        if node is None:
            return 0
        left_height = self._height_helper(node.left)
        right_height = self._height_helper(node.right)
        return max(left_height, right_height) + 1

    def size(self):
        return self._size_helper(self.root)

    def _size_helper(self, node):
        if node is None:
            return 0
        return 1 + self._size_helper(node.left) + self._size_helper(node.right)

    def count_leaves(self):
        return self._count_leaves_helper(self.root)

    def _count_leaves_helper(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaves_helper(node.left) + self._count_leaves_helper(node.right)

    def is_full_binary_tree(self):
        return self._is_full_helper(self.root)

    def _is_full_helper(self, node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self._is_full_helper(node.left) and self._is_full_helper(node.right)
        return False

    def is_complete_binary_tree(self):
        if self.root is None:
            return True
        
        queue = [self.root]
        has_empty_child = False
        
        while queue:
            current = queue.pop(0)
            
            if current.left:
                if has_empty_child:
                    return False
                queue.append(current.left)
            else:
                has_empty_child = True
                
            if current.right:
                if has_empty_child:
                    return False
                queue.append(current.right)
            else:
                has_empty_child = True
                
        return True


# Example usage
if __name__ == "__main__":
    # Create a binary tree
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    
    # Test the methods
    print("Tree Height:", tree.height())
    print("Total Nodes:", tree.size())
    print("Leaf Nodes Count:", tree.count_leaves())
    print("Is Full Binary Tree:", tree.is_full_binary_tree())
    print("Is Complete Binary Tree:", tree.is_complete_binary_tree())