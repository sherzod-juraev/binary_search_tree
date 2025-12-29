# AVL Tree

This package provides a clean and fully functional implementation of an
**AVL Tree (Adelson-Velsky and Landis Tree)** in Python.

An AVL Tree is a self-balancing Binary Search Tree (BST) that guarantees
`O(log n)` time complexity for insertion, deletion, and search operations
by maintaining a balance factor at every node.

## Table of Contents

- [Node structure](#-node-structure)
- [AVL Tree class](#-avltree-class)
    - [Core properties](#core-properties)
    - [Supported operations](#-supported-operations)
        - [Insertion](#insertion)
        - [Deletion](#deletion)
        - [Search](#search)
        - [Traversals](#traversals)
        - [Min / Max](#min--max)
        - [Rotations](#-rotations)
- [Complexity](#complexity)
- [Design goals](#design-goals)

## Node Structure

Each node stores:

- `value`   : the key stored in the node
- `left`    : reference to left child
- `right`   : reference to right child
- `height`  : height of the node
- `count`   : number of duplicates of the same value

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.count = 1
```

Duplicates are handled by increasing the count instead of creating
multiple nodes.

## AVLTree Class

### Core Properties

- `root` – root node of the tree

- `size()` – total number of elements (including duplicates)

- `node_count()` – number of distinct nodes (unique values)

### ✨ Supported Operations

#### **Insertion**

```python
tree.insert(value)
```

- Inserts a value following BST rules

- Handles duplicates using `count`

- Automatically rebalances the tree using rotations

#### **Deletion**

```python
tree.delete(value)
```

- Removes a value from the tree

- Decreases `count` if duplicates exist

- Uses in-order successor for nodes with two children

- Restores AVL balance after deletion

#### **Search**

```python
node = tree.search(value)
```

- Standard BST search

- Guaranteed `O(log n)` time complexity due to AVL balancing

- Returns the corresponding `Node` or `None`

#### **Traversals**

```python
tree.in_order()     # Sorted order
tree.pre_order()    # Root → Left → Right
tree.post_order()   # Left → Right → Root
```

#### **Min / Max**

```python
tree.min()
tree.max()
```

Returns the minimum or maximum
value stored in the tree.

#### **Balance Utilities**

```python
tree.get_balance(node)
tree.is_balanced()
```

- `get_balance(node)` returns balance factor:
`height(left) - height(right)`

- `is_balanced()` verifies the AVL property for the entire tree

#### **🔄 Rotations**

| Case |      Method       |
|:-----|:-----------------:|
| LL   | `__rotate_right`  |
| RR   |  `__rotate_left`  |
| LR   |   `__rotate_lr`   |
| RL   |   `__rotate_rl`   |

Rotations are applied automatically during insertion and deletion.

## Complexity

| Operation | 	Time Complexity  |
|:----------|:-----------------:|
| Insert    |     	O(log n)     |
| Delete    |     	O(log n)     |
| Search    |     	O(log n)     |

## Design goals

- Clear separation of concerns

- Recursive and readable logic

- Correct handling of duplicates

- Strict AVL invariants

- Educational and production-ready structure

