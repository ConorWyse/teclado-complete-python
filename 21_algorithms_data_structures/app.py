from node import Node
from binary_tree import BinaryTree

# tree = BinaryTree(Node(9))
# tree.add(Node(5))
# tree.add(Node(8))
# tree.add(Node(11))
# tree.add(Node(17))

# print('\nIn order:')
# tree.inorder()
# print('\nPre-order:')
# tree.preorder()

tree = BinaryTree(Node(60))

nodes = [50, 30, 90, 70, 80, 75, 120, 110]

for n in nodes:
    tree.add(Node(n))

tree.inorder()
tree.delete(90)
print('\nremoved 90')
tree.inorder()
