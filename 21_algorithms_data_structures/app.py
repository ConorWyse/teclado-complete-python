from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(8))
tree.add(Node(11))
tree.add(Node(17))

print('\nIn order:')
tree.inorder()
print('\nPre-order:')
tree.preorder()
