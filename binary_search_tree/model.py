from typing import Any
from .node import Node
from .exception import Empty


class BinarySearchTree:
    """Binary Search Tree (BST) implementation supporting duplicate elements via 'count'.

    Attributes:
        root (Node | None): The root node of the BST.
        __size (int): Number of unique nodes in the tree.

    Methods:
        insert(value): Insert a value into the BST. Increments count if value exists.
        search(value): Search for a node with the given value. Returns Node or None.
        delete(value): Delete a node with the given value. Handles duplicates correctly.
        min(): Return the minimum value in the BST.
        max(): Return the maximum value in the BST.
        in_order(): Return list of values in in-order traversal.
        pre_order(): Return list of values in pre-order traversal.
        post_order(): Return list of values in post-order traversal.
        height(): Return the height of the BST.
        is_empty(): Raise Empty exception if the BST is empty.
    """

    def __init__(self):

        self.root = None
        self.__size = 0

    def __autoinc_size(self):

        self.__size += 1

    def __autodec_size(self):

        self.__size -= 1

    def size(self) -> int:
        """Return the number of unique nodes in the BST."""

        return self.__size

    def is_empty(self):
        """Raise Empty exception if the BST has no nodes."""

        if self.__size == 0:
            raise Empty('BinarySearchTree is empty')

    def insert(self, value: Any, /):
        """Insert a value into the BST."""

        if self.__size == 0:
            self.root = Node(value)
            self.__autoinc_size()
            return
        current = self.root
        while current:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    break
        if current.value == value:
            current.count += 1
            return
        if value < current.value:
            current.left = Node(value)
        if current.value < value:
            current.right = Node(value)
        self.__autoinc_size()

    def search(self, value: Any, /) -> Any:
        """Search for a node with the given value and return it. Returns None if not found."""

        self.is_empty()
        current = self.root
        while current:
            if current.value == value:
                break
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return current

    def delete(self, value: Any, /):
        """Delete a node with the given value. Handles duplicates and in-order successor if needed."""

        self.is_empty()
        self.root = self.__delete_helper(self.root, value)

    def __delete_helper(self, node: Node, value: Any, /):
        """Recursive helper for delete(). Returns the updated subtree after deletion."""

        if node is None:
            return
        if node.value == value:
            if node.left and node.right:
                if node.count > 1:
                    node.count -= 1
                    return node
                else:
                    successor = self.__in_order_successor(node.right)
                    node.value = successor.value
                    node.count = successor.count
                    node.right = self.__delete_helper(node.right, node.value)
            elif node.left:
                if node.count > 1:
                    node.count -= 1
                    return node
                else:
                    self.__autodec_size()
                    return node.left
            elif node.right:
                if node.count > 1:
                    node.count -= 1
                    return node
                else:
                    self.__autodec_size()
                    return node.right
            else:
                if node.count > 1:
                    node.count -= 1
                else:
                    self.__autodec_size()
                    return None
        elif value < node.value:
            node.left = self.__delete_helper(node.left, value)
        elif node.value < value:
            node.right = self.__delete_helper(node.right, value)
        return node

    def __in_order_successor(self, node: Node, /) -> Node:
        """Return the in-order successor of the given node (smallest node in right subtree)."""

        while node.left:
            node = node.left
        return node

    def min(self) -> Any:
        """Return the minimum value stored in the BST."""

        self.is_empty()
        current = self.root
        while current.left:
            current = current.left
        return current.value

    def max(self) -> Any:
        """Return the maximum value stored in the BST."""

        self.is_empty()
        current = self.root
        while current.right:
            current = current.right
        return current.value

    def in_order(self) -> list:
        """Return a list of all values in in-order traversal."""

        arr = []
        self.__in_order_helper(self.root, arr)
        return arr

    def __in_order_helper(self, node: Node, arr: list, /):
        """Recursive helper for in_order(). Appends values to arr in in-order."""

        if node is None:
            return
        self.__in_order_helper(node.left, arr)
        arr.append(node.value)
        self.__in_order_helper(node.right, arr)

    def pre_order(self) -> list:
        """Return a list of all values in pre-order traversal."""

        arr = []
        self.__pre_order_helper(self.root, arr)
        return arr

    def __pre_order_helper(self, node: Node, arr: list, /):
        """Recursive helper for pre_order(). Appends values to arr in pre-order."""

        if node is None:
            return
        arr.append(node.value)
        self.__pre_order_helper(node.left, arr)
        self.__pre_order_helper(node.right, arr)

    def post_order(self) -> list:
        """Return a list of all values in post-order traversal."""

        arr = []
        self.__post_order_helper(self.root, arr)
        return arr

    def __post_order_helper(self, node: Node, arr: list, /):
        """Recursive helper for post_order(). Appends values to arr in post-order."""

        if node is None:
            return
        self.__post_order_helper(node.left, arr)
        self.__post_order_helper(node.right, arr)
        arr.append(node.value)

    def height(self) -> int:
        """Return the height of the BST."""

        num = self.__height_helper(self.root)
        return num

    def __height_helper(self, node: Node, /) -> int:
        """Recursive helper for height(). Computes height of subtree rooted at node."""

        if node is None:
            return -1
        if node.left is None and node.right is None:
            return 0
        return max(self.__height_helper(node.left), self.__height_helper(node.right)) + 1