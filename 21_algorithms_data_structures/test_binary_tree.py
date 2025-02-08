from binary_tree import BinaryTree
from node import Node
from unittest import TestCase
from unittest.mock import patch
from io import StringIO


class TestBinaryTree(TestCase):
    def setUp(self):
        self.tree = BinaryTree(Node(9))
        self.tree.add(Node(5))
        self.tree.add(Node(11))
    
    def test_added(self):
        self.assertIsNotNone(self.tree.find(5))
        self.assertIsNotNone(self.tree.find(9))
        self.assertIsNotNone(self.tree.find(11))

    def test_inorder(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            self.tree.inorder()
            self.assertRegex(fake_out.getvalue(), r'.+ 5>\n.+ 9>\n.+ 11>')

    def test_preorder(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            self.tree.preorder()
            self.assertRegex(fake_out.getvalue(), r'.+ 9>\n.+ 5>\n.+ 11>')
