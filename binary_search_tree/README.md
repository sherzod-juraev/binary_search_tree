# Binary Search Tree Package

A simple Python package implementing a **Binary Search Tree (BST)** with support for duplicate elements.

## Table of Contents

- [Files description](#files-description)
- [Features](#features)
- [Usage example](#use-in-your-python-scripts)
   - [Create a BST instance](#create-a-bst-instance)
   - [Insert values](#insert-values)
   - [Search for a value](#search-for-a-value)
   - [Traversals](#traversals)
   - [Min, Max and Height](#min-max-and-height)
   - [Delete values](#delete-values)

## 
### Files Description

- **model.py**: Implements the `BinarySearchTree` class with standard BST operations: insert, search, delete, traversals (in-order, pre-order, post-order), min, max, and height calculation.  
- **node.py**: Defines the `Node` class used internally by the BST, with attributes for `value`, `count`, `left`, and `right`.  
- **exception.py**: Defines a minimal `Empty` exception class, used to indicate that the BST is empty when performing certain operations.  
- **__init__.py**: Imports the `BinarySearchTree` class to simplify package usage.

## Features

- Supports **duplicate values** via a `count` attribute in each node.  
- Implements standard BST operations:
  - `insert(value)` — insert a value or increment count if it exists
  - `search(value)` — return the node containing the value
  - `delete(value)` — delete a node or decrement count if duplicates exist
  - `min()` / `max()` — find the minimum or maximum value
  - `in_order()`, `pre_order()`, `post_order()` — tree traversal methods
  - `height()` — compute the height of the tree
  - `size()` — return the number of unique nodes
- Raises `Empty` exception when operations are performed on an empty tree.

## Use in your Python scripts

### Create a BST instance
```python
from binary_search_tree import BinarySearchTree
bst = BinarySearchTree()
```

### Insert values
```python
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(10)  # Duplicate, count increases
```

### Search for a value
```python
node = bst.search(10)
print(node.value, node.count)  # Output: 10 2
```

### Traversals
```python
print(bst.in_order())   # Output: [5, 10, 15]
print(bst.pre_order())  # Output: [10, 5, 15]
print(bst.post_order()) # Output: [5, 15, 10]
```

### Min, Max and Height
```python
print(bst.min())     # Output: 5
print(bst.max())     # Output: 15
print(bst.height())  # Output: 1
```

### Delete values
```python
bst.delete(10)  # Decrements count if > 1
```