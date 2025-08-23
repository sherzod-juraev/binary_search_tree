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
