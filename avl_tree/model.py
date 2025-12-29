from typing import Any
from .node import Node
from .exception import Empty


class AVLTree:
    """
    AVL Tree (Adelson-Velsky and Landis Tree) class.

    Attributes
    ----------
    root : Node
        Root node of the AVL tree.
    __size : int
        Total number of elements in the tree (including duplicates).
    __node_count : int
        Total number of nodes in the tree (excluding duplicates).
    """

    def __init__(self):

        self.root = None
        self.__size = 0
        self.__node_count = 0

    def node_count(self) -> int:
        """
        Returns the total number of distinct nodes in the AVL tree,
        excluding duplicates.

        Returns
        -------
        int
            Number of unique nodes in the tree.
        """
        
        return self.__node_count

    def size(self) -> int:
        """
        Returns the total number of elements in the AVL tree,
        including duplicates.

        Returns
        -------
        int
            Total count of elements stored in the tree.
        """

        return self.__size

    def __autoinc_size_node_count(self, autoinc_node: bool = False, /):
        """
        Increments the tree's size and optionally node count when a new element is added.

        Parameters
        ----------
        autoinc_node : bool
            If True, node_count is also incremented (used when a new node is added).
        """

        self.__size += 1
        if autoinc_node:
            self.__node_count += 1

    def __autodec_size_node_count(self, autodec_node: bool = False, /):
        """
        Decrements the tree's size and optionally node count when an element is removed.

        Parameters
        ----------
        autodec_node : bool
            If True, node_count is also decremented (used when a node is removed).
        """

        self.__size -= 1
        if autodec_node:
            self.__node_count -= 1

    def is_empty(self):
        """
        Checks if the AVL tree is empty.
        Raises an Empty exception if the tree has no nodes.
        """

        if self.__node_count == 0:
            raise Empty('AVLTree is empty')

    def insert(self, value: Any, /):
        """
        Inserts a new value into the AVL tree.
        If the value already exists, increments its count.
        After insertion, checks balance and performs rotations if necessary.
        """

        if self.__node_count == 0:
            self.root = Node(value)
            self.__autoinc_size_node_count(True)
            return
        self.root = self.__insert_helper(self.root, value)

    def __insert_helper(self, node: Node, value: Any, /) -> Node:
        """
        Helper function for insertion. Works recursively.
        Adds the value, updates count, checks balance, and applies rotations if needed.

        Returns
        -------
        Node
            The updated node (may be the new root after rotation).
        """

        if value < node.value:
            if node.left:
                node.left = self.__insert_helper(node.left, value)
            else:
                node.left = Node(value)
                self.__autoinc_size_node_count(True)
        elif node.value < value:
            if node.right:
                node.right = self.__insert_helper(node.right, value)
            else:
                node.right = Node(value)
                self.__autoinc_size_node_count(True)
        else:
            node.count += 1
            self.__autoinc_size_node_count()

        bf = self.get_balance(node)
        if bf < -1:
            if node.right.value < value: # right-right
                return self.__rotate_left(node)
            else: # right-left
                return self.__rotate_rl(node)
        elif 1 < bf:
            if value < node.left.value: # left-left
                return self.__rotate_right(node)
            else: # left-right
                return self.__rotate_lr(node)
        node.height = self.get_height(node)
        return node

    def delete(self, value: Any, /):
        """
        Deletes a value from the AVL tree.
        Currently not implemented.
        """

        self.is_empty()
        self.root = self.__delete_helper(self.root, value)

    def __delete_helper(self, node: Node, value: Any, /) -> Node:

        if node is None:
            return None
        if value < node.value:
            if node.left:
                node.left = self.__delete_helper(node.left, value)
        elif node.value < value:
            if node.right:
                node.right = self.__delete_helper(node.right, value)
        if value == node.value:
            if node.count > 1:
                node.count -= 1
                self.__autodec_size_node_count()
            else:
                if node.left and node.right:
                    successor = self.__successor(node.right)
                    node.value, node.count = successor.value, successor.count
                    successor.count = 1
                    node.right = self.__delete_helper(node.right, node.value)
                elif node.left:
                    self.__autodec_size_node_count(True)
                    return node.left
                elif node.right:
                    self.__autodec_size_node_count(True)
                    return node.right
                else:
                    self.__autodec_size_node_count(True)
                    return None
        bf = self.get_balance(node)
        if bf < -1:
            if node.right.value < value: # right-right
                return self.__rotate_left(node)
            else: # right-left
                return self.__rotate_rl(node)
        elif 1 < bf:
            if value < node.left.value: # left-left
                return self.__rotate_right(node)
            else: # left-right
                return self.__rotate_lr(node)
        node.height = self.get_height(node)
        return node

    def __successor(self, node: Node, /) -> Node:

        current = node
        while current.left:
            current = current.left
        return current

    def search(self, value: Any, /) -> Node:
        """
        Searches for a value in the AVL tree.

        Returns
        -------
        Node | None
            Returns the node containing the value, or None if not found.
        """

        self.is_balanced()
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif current.value < value:
                current = current.right
            else:
                break
        return current

    def __rotate_lr(self, x: Node, /) -> Node:
        """
        Performs a Left-Right (LR) rotation.

        Returns
        -------
        Node
            The new root of the rotated subtree.
        """

        x.left = self.__rotate_left(x.left)
        return self.__rotate_right(x)

    def __rotate_left(self, x: Node, /) -> Node:
        """
        Performs a Left rotation (RR case).

        Returns
        -------
        Node
            The new root of the rotated subtree.
        """

        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = self.get_height(x)
        y.height = self.get_height(y)
        return y

    def __rotate_rl(self, x: Node) -> Node:
        """
        Performs a Right-Left (RL) rotation.

        Returns
        -------
        Node
            The new root of the rotated subtree.
        """

        x.right = self.__rotate_right(x.right)
        return self.__rotate_left(x)

    def __rotate_right(self,x: Node, /) -> Node:
        """
        Performs a Right rotation (LL case).

        Returns
        -------
        Node
            The new root of the rotated subtree.
        """

        y = x.left
        T3 = y.right
        y.right = x
        x.left = T3
        x.height = self.get_height(x)
        y.height = self.get_height(y)
        return y

    def get_height(self, node: Node, /) -> int:
        """
        Calculates the height of a node.

        Parameters
        ----------
        node : Node
            The node to measure.

        Returns
        -------
        int
            Height of the node.
        """

        h = 1 + max(self.__node_height(node.left), self.__node_height(node.right))
        return h

    def __node_height(self, node: Node | None, /) -> int:
        """
        Returns the height of a node. Returns 0 if node is None.
        """

        if node is None:
            return 0
        return node.height

    def get_balance(self, node: Node, /):
        """
        Calculates the balance factor (BF) of a node.

        Returns
        -------
        int
            BF = height(left) - height(right)
        """

        if node is None:
            return 0
        return self.__node_height(node.left) - self.__node_height(node.right)

    def is_balanced(self, node: Node | None = None, /) -> bool:
        """
        Checks if the AVL tree is fully balanced.

        Returns
        -------
        bool
            True if the tree is balanced, False otherwise.
        """

        if node is None:
            node = self.root
        return self.__is_balanced_helper(node)


    def __is_balanced_helper(self, node: Node, /) -> bool:
        """
        Helper function to recursively check balance for each node.
        """

        if node is None:
            return True
        bf = self.get_balance(node)
        if bf < -1 or 1 < bf:
            return False
        return self.__is_balanced_helper(node.left) and self.__is_balanced_helper(node.right)

    def min(self):
        """
        Returns the minimum value in the AVL tree.

        Returns
        -------
        Any
            The minimum value.
        """

        self.is_empty()
        current = self.root
        while current.left:
            current = current.left
        return current.value

    def max(self):
        """
        Returns the maximum value in the AVL tree.

        Returns
        -------
        Any
            The maximum value.
        """

        self.is_empty()
        current = self.root
        while current.right:
            current = current.right
        return current.value

    def in_order(self) -> list:
        """
        Returns values of the tree in in-order traversal.
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
        Returns values of the tree in pre-order traversal.
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
        Returns values of the tree in post-order traversal.
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