from typing import Any
from collections import deque
from .node import Node
from .exception import Empty


class BinaryTree:
    """
    A simple Binary Tree implementation (not necessarily BST).

    Attributes:
        root (Node): Root node of the tree.
        __size (int): Total number of nodes in the tree.
    """

    def __init__(self):

        self.root = None
        self.__size = 0

    def __autoincrement_size(self):

        self.__size += 1

    def __autodecrement_size(self):

        self.__size -= 1

    def peek_root(self):
        """
        Return the value of the root node.

        Raises:
            Empty: If the tree is empty.

        Returns:
            Any: Value of the root node.
        """

        if self.__size == 0:
            return None
        return self.root.value

    def size(self):
        """
        Return the number of nodes in the tree.

        Returns:
            int: Size of the tree.
        """

        return self.__size

    def clear(self):
        """
        Remove all nodes from the tree, resetting its size to 0.
        """

        self.root = None
        self.__size = 0

    def count_leaves(self) -> int:
        """
        Count the number of leaf nodes in the tree.

        Returns:
            int: Total number of leaves.
        """

        return self.__count_leaves_helper(self.root)

    def __count_leaves_helper(self, node: Node, /) -> int:
        """
        Recursive helper to count leaves starting from a given node.

        Args:
            node (Node): Node to start counting from.

        Returns:
            int: Number of leaves in the subtree.
        """

        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.__count_leaves_helper(node.left) + self.__count_leaves_helper(node.right)

    def contains(self, value: Any, /) -> bool:
        """
        Check whether the given value exists in the tree.

        Args:
            value (Any): Value to search for.

        Raises:
            Empty: If the tree is empty.

        Returns:
            bool: True if the value exists, False otherwise.
        """

        self.is_empty()
        return self.__contains_helper(self.root, value)

    def __contains_helper(self, node: Node, value: Any, /) -> bool:
        """
        Recursive helper for `contains`.

        Args:
            node (Node): Current node to check.
            value (Any): Value to search for.

        Returns:
            bool: True if value found in subtree, False otherwise.
        """

        if node is None:
            return False
        if node.value == value:
            return True
        return self.__contains_helper(node.left, value) or self.__contains_helper(node.right, value)

    def search(self, value: Any, /) -> Node:
        """
        Search and return the node containing the given value.

        Args:
            value (Any): Value to search for.

        Raises:
            Empty: If the tree is empty.

        Returns:
            Node | None: Node with the value if found, else None.
        """

        self.is_empty()
        return self.__search_helper(self.root, value)

    def __search_helper(self, node: Node, value: Any, /) -> Any:
        """
        Recursive helper for `search`.

        Args:
            node (Node): Current node in recursion.
            value (Any): Value to search.

        Returns:
            Node | None: Node if found, None otherwise.
        """

        if node is None:
            return None
        if node.value == value:
            return node
        return self.__search_helper(node.left, value) or self.__search_helper(node.right, value)

    def is_empty(self):
        """
        Check if the tree is empty.

        Raises:
            Empty: If the tree has no nodes.
        """

        if self.__size == 0:
            raise Empty('BinaryTree is empty')

    def insert(self, value: Any, /):
        """
        Insert a new node into the tree following level-order (complete binary tree style).

        Args:
            value (Any): Value to insert.
        """

        if self.__size == 0:
            self.root = Node(value)
            self.__autoincrement_size()
            return
        path = bin(self.__size + 1)[3:]
        current = self.root
        for i in range(len(path) - 1):
            if path[i] == '0':
                current = current.left
            else:
                current = current.right
        if path[-1] == '0':
            current.left = Node(value)
        else:
            current.right = Node(value)
        self.__autoincrement_size()

    def height(self) -> int:
        """
        Calculate the height of the tree.

        Returns:
            int: Height of the tree (-1 if empty).
        """

        height = self.__height_counter(self.root)
        return height

    def __height_counter(self, node: Node, /) -> int:

        if node is None:
            return -1
        if node.left is None and node.right is None:
            return 0
        return max(self.__height_counter(node.left), self.__height_counter(node.right)) + 1

    def in_order(self) -> list:
        """
        Perform in-order traversal.

        Returns:
            list: List of node values in in-order sequence.
        """

        arr = []
        self.__in_order_helper(self.root, arr)
        return arr

    def __in_order_helper(self, node: Node, arr: list, /):

        if node is None:
            return
        self.__in_order_helper(node.left, arr)
        arr.append(node.value)
        self.__in_order_helper(node.right, arr)

    def pre_order(self) -> list:
        """
        Perform pre-order traversal.

        Returns:
            list: List of node values in pre-order sequence.
        """

        arr = []
        self.__pre_order_helper(self.root, arr)
        return arr

    def __pre_order_helper(self, node: Node, arr: list, /):

        if node is None:
            return
        arr.append(node.value)
        self.__pre_order_helper(node.left, arr)
        self.__pre_order_helper(node.right, arr)

    def post_order(self) -> list:
        """
        Perform post-order traversal.

        Returns:
            list: List of node values in post-order sequence.
        """

        arr = []
        self.__post_order_helper(self.root, arr)
        return arr

    def __post_order_helper(self, node: Node, arr: list, /):

        if node is None:
            return
        self.__post_order_helper(node.left, arr)
        self.__post_order_helper(node.right, arr)
        arr.append(node.value)

    def level_order(self):
        """
        Perform level-order traversal (BFS).

        Returns:
            list: List of node values level by level.
        """

        arr = []
        queue = deque()
        if self.__size != 0:
            queue.append(self.root)
        while len(queue) != 0:
            node = queue.popleft()
            arr.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return arr