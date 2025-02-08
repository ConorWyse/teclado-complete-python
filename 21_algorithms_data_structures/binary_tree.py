from node import Node


class BinaryTree:
    def __init__(self, head: Node):
        self.head = head
    
    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError('A node with that value already exists.')
            if new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
 
    def find(self, value: int) -> Node:
        current_node = self.head
        while current_node:
            if value == current_node.value:
                return current_node
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        raise LookupError(f'A node with value {value} was not found.')
 
    def inorder(self):
        """prints out all the values stored in the tree in numerical order."""
        self._inorder_recursive(self.head)
    
    def _inorder_recursive(self, current_node):
        if not current_node:
            return
        self._inorder_recursive(current_node.left)
        print(current_node)
        self._inorder_recursive(current_node.right)

    
    def preorder(self):
        """prints out all the values stored in the tree in 'preorder' order."""
        self._preorder_recursive(self.head)
    
    def _preorder_recursive(self, current_node):
        if not current_node:
            return
        print(current_node)
        self._preorder_recursive(current_node.left)
        self._preorder_recursive(current_node.right)

