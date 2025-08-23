 # Binary Search Tree (BST) in Python

This project is a simple implementation of a Binary Search Tree (BST) in Python.
It provides the basic functionality of a BST such as insertion, search, removal, traversals, and more.
The project is split into two files for better structure:

binary_search_tree.py → contains the BinarySearchTree class implementation

main.py → demonstrates usage of the BinarySearchTree

---

## Features

- Insert new values

- Search for existing values

- Remove nodes (leaf, one-child, two-children cases handled)

- Find minimum and maximum values

- Count total nodes

- Find tree height

- Clear the tree

- Merge two BSTs

- Traversal methods:

  - In-order (Left → Root → Right)

  - Pre-order (Root → Left → Right)

  - Post-order (Left → Right → Root)

  - Level-order (Breadth-First Search)
 
 ---
 
 ## Project Structure
 
📂 binary_search_tree

 ┣ 📜 binary_search_tree.py

 
 ┣ 📜 main.py          

 
 ┗ 📜 README.md          
 
---
 ## Requirements

Python 3.9+ recommended

No external libraries needed

--
## Notes

Duplicate values are not allowed (insertion will raise an error).

This is a basic BST, not self-balancing (e.g., AVL/Red-Black Tree).

---

## Example Usage

main.py
```python

from binary_search_tree import BinarySearchTree

# Create a new BST and insert values
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# Search
print(bst.search(40))   # True
print(bst.search(100))  # False

# Traversals
print("In-order:", bst.in_order())     
print("Pre-order:", bst.pre_order())  
print("Post-order:", bst.post_order())
print("Level-order:", bst.level_order())

# Find min and max
print("Min:", bst.find_min())
print("Max:", bst.find_max())

# Remove a node
bst.remove(30)
print("After removing 30:", bst.in_order())

# Count nodes
print("Total nodes:", bst.count_nodes())

# Height of tree
print("Height:", bst.height())

```
