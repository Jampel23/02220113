# Define color constants
RED = 'RED'
BLACK = 'BLACK'

class Node:
    def __init__(self, value, color=RED):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"{self.value}({self.color})"

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, BLACK)  # Sentinel leaf node
        self.root = self.NIL
    
    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.NIL
        new_node.right = self.NIL
        
        parent = None
        current = self.root
        
        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right
        
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
            
        if new_node.parent is None:
            new_node.color = BLACK
            return
        
        if new_node.parent.parent is None:
            return
            
        self._fix_insert(new_node)
    
    def _fix_insert(self, node):
        while node.parent.color == RED:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    uncle.color = BLACK
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right
                if uncle.color == RED:
                    uncle.color = BLACK
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self._right_rotate(node.parent.parent)
            
            if node == self.root:
                break
        
        self.root.color = BLACK
    
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        
        y.parent = x.parent
        if x.parent is None:
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
        if y.right != self.NIL:
            y.right.parent = x
        
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def delete(self, value):
        node = self._search_node(value)
        if node == self.NIL:
            return
        
        original_color = node.color
        if node.left == self.NIL:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self._transplant(node, node.left)
        else:
            min_node = self._minimum(node.right)
            original_color = min_node.color
            x = min_node.right
            if min_node.parent == node:
                x.parent = min_node
            else:
                self._transplant(min_node, min_node.right)
                min_node.right = node.right
                min_node.right.parent = min_node
            
            self._transplant(node, min_node)
            min_node.left = node.left
            min_node.left.parent = min_node
            min_node.color = node.color
        
        if original_color == BLACK:
            self._fix_delete(x)
    
    def _fix_delete(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == RED:
                    sibling.color = BLACK
                    x.parent.color = RED
                    self._left_rotate(x.parent)
                    sibling = x.parent.right
                
                if sibling.left.color == BLACK and sibling.right.color == BLACK:
                    sibling.color = RED
                    x = x.parent
                else:
                    if sibling.right.color == BLACK:
                        sibling.left.color = BLACK
                        sibling.color = RED
                        self._right_rotate(sibling)
                        sibling = x.parent.right
                    
                    sibling.color = x.parent.color
                    x.parent.color = BLACK
                    sibling.right.color = BLACK
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == RED:
                    sibling.color = BLACK
                    x.parent.color = RED
                    self._right_rotate(x.parent)
                    sibling = x.parent.left
                
                if sibling.right.color == BLACK and sibling.left.color == BLACK:
                    sibling.color = RED
                    x = x.parent
                else:
                    if sibling.left.color == BLACK:
                        sibling.right.color = BLACK
                        sibling.color = RED
                        self._left_rotate(sibling)
                        sibling = x.parent.left
                    
                    sibling.color = x.parent.color
                    x.parent.color = BLACK
                    sibling.left.color = BLACK
                    self._right_rotate(x.parent)
                    x = self.root
        
        x.color = BLACK
    
    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node
    
    def search(self, value):
        return self._search_node(value) != self.NIL
    
    def _search_node(self, value):
        current = self.root
        while current != self.NIL and value != current.value:
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return current
    
    def get_black_height(self):
        if self.root == self.NIL:
            return 0
        
        height = 0
        node = self.root
        while node != self.NIL:
            if node.color == BLACK:
                height += 1
            node = node.left
        return height
    
    def _inorder(self, node, result):
        if node != self.NIL:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)
    
    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

# Example Usage
if __name__ == "__main__":
    rb_tree = RedBlackTree()
    rb_tree.insert(10)
    rb_tree.insert(20)
    rb_tree.insert(30)
    print("Inorder traversal:", rb_tree.inorder_traversal())
    print("Black height:", rb_tree.get_black_height())
    
    print("Search 20:", rb_tree.search(20))
    print("Search 40:", rb_tree.search(40))
    
    rb_tree.delete(20)
    print("After deleting 20, inorder traversal:", rb_tree.inorder_traversal())
    print("Black height after deletion:", rb_tree.get_black_height())