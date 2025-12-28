# BinaryTree Package

A simple **Binary Tree** implementation
in Python (not necessarily a BST).
This package provides a complete binary
tree with basic operations like insertion,
traversal, and utility methods such as
counting leaves or checking height.

## Table of Contents

- [Features](#features)

- [Usage example](#usage-example)
   - [creating a binary tree](#create-a-binary-tree)
   - [insert nodes](#insert-nodes)
   - [get root value](#get-root-value)
   - [check size](#check-size)
   - [traversals](#traversals)
   - [search for a value](#search-for-a-value)
   - [check if tree contains a value](#check-if-tree-contains-a-value)
   - [count leaves](#count-leaves)
   - [tree height](#tree-height)
   - [clear the tree](#clear-the-tree)

- [Notes](#notes)

## Features

- Insert nodes in **level-order** (complete binary tree style)

- Check if a value exists in the tree

- Search for a node by value

- Count leaf nodes

- Get the height of the tree

- Various tree traversals:

   - In-order

   - Pre-order

   - Post-order

   - Level-order (BFS)

- Clear the tree

## Usage Example

```python
from binary_tree import BinaryTree
```

### Create a binary tree

```python
tree = BinaryTree()
```

### Insert nodes

```python
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
```

### Get root value

```python
print("Root:", tree.peek_root())  # Output: 10
```

### Check size

```python
print("Size:", tree.size())  # Output: 4
```

### Traversals

```python
print("In-order:", tree.in_order())      # [40, 20, 10, 30]
print("Pre-order:", tree.pre_order())    # [10, 20, 40, 30]
print("Post-order:", tree.post_order())  # [40, 20, 30, 10]
print("Level-order:", tree.level_order())# [10, 20, 30, 40]
```

### Search for a value

```python
node = tree.search(30)
print("Found node value:", node.value if node else "Not found")
```

### Check if tree contains a value

```python
print("Contains 50?", tree.contains(50))  # False
```

### Count leaves

```python
print("Number of leaves:", tree.count_leaves())  # 2
```

### Tree height

```python
print("Height:", tree.height())  # 2
```

### Clear the tree

```python
tree.clear()
print("Tree cleared. Size:", tree.size())  # 0
```

## Notes

- This implementation does not support node
deletion to maintain proper level-order structure.

- Nodes are inserted according to the level-order position.