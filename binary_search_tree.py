class BinarySearchTree:
    class __Node:
        def __init__(self, value): 
            self.value = value
            self.right = None
            self.left = None
    
    def __init__(self, value: int = None, /):
        
        self.root = None
        self.__number_of_nodes = 0
        if value:
            self.__value_check(value)
            self.root = BinarySearchTree.__Node(value)
            self.__number_of_nodes += 1
    
    def __value_check(self, value: int):
        """Check if a value is of type int"""
        if not isinstance(value, int):
            raise ValueError(f'integers can be entered, not {type(value)}')
            
    def insert(self, value: int, /):
        """Add value"""
        self.__value_check(value)
        if self.root:
            current = self.root
            while current:
                if value < current.value: 
                    if current.left:
                        current = current.left
                    else:
                        current.left = BinarySearchTree.__Node(value)
                        self.__number_of_nodes += 1
                        return None
                elif value > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = BinarySearchTree.__Node(value)
                        self.__number_of_nodes += 1
                        return None
                else:
                    raise ValueError(f'The value {value} is predefined.')
        self.root = BinarySearchTree.__Node(value)
        self.__number_of_nodes += 1
        
    def search(self, value: int, /) -> bool:
        """Check if a value exists"""
        self.__value_check(value)
        if self.root:
            current = self.root
            while current:
                if current.value == value:
                    return True
                if value < current.value:
                    current = current.left
                else:
                    current = current.right
            return False
        raise Exception('Empty Binary Search Tree')
    
    def __min_value_node(self, node) -> '__Node':
        """Find node with the smallest value"""
        current = node
        while current.left:
            current = current.left
        return current        
    
    def __remove_node(self, node: '__Node', value: int) -> '__Node':
        if not node:
            raise ValueError('value not defined in tree')
        if value < node.value:
            node.left = self.__remove_node(node.left, value)
        elif value > node.value:
            node.right = self.__remove_node(node.right, value)
        else:
            if not node.left and not node.right:
                self.__number_of_nodes -= 1
                return None
            elif node.left and not node.right:
                self.__number_of_nodes -= 1
                return node.left
            elif not node.left and node.right:
                self.__number_of_nodes -= 1
                return node.right
            else:
                left_leaf = self.__min_value_node(node.right)
                node.value = left_leaf.value
                node.right = self.__remove_node(node.right, left_leaf.value)
        return node
    
    def remove(self, value: int, /):
        """Delete value from tree"""
        self.__value_check(value)
        self.__check_for_emptiness()
        self.root = self.__remove_node(self.root, value)    
    def find_min(self) -> int:
        """Return the smallest value"""
        current = self.root
        while current:
            if current.left:
                current = current.left
            else:
                return current.value
        raise Exception('Empty Binary Search Tree')
    
    def find_max(self) -> int:
        """Return the largest value"""
        current = self.root
        while current:
            if current.right:
                current =  current.right
            else:
                return current.value
        raise Exception('Empty Binary Search Tree')
    
    def height(self, node: '__Node'=None) -> int:
        """Tree height (longest path root -> leaf)"""
        if not self.root:
            return 0
        if node is None:
            node = self.root
        left_h = self.height(node.left) if node.left else 0
        right_h = self.height(node.right) if node.right else 0
        return 1 + max(left_h, right_h)

    def count_nodes(self) -> int:
        """Count how many nodes there are"""
        return self.__number_of_nodes
    
    def extend(self, binary_search_tree: 'BinarySearchTree', /):
        """Merge binary search trees"""
        if not isinstance(binary_search_tree, BinarySearchTree):
            raise TypeError('Incorrect type of information entered')
        current = binary_search_tree.in_order()
        for i in current:
            self.insert(i)
                    
    def __check_for_emptiness(self):
        """Gives an error if the tree is empty"""
        if not self.root:
            raise Exception('Empty Binary Search Tree')
            
    def in_order(self, node = None, /) -> list[int]:
        """Return in the form left -> root -> right"""
        if not node:
            self.__check_for_emptiness()
            node = self.root
        array = []
        if node:
            if node.left:
                array.extend(self.in_order(node.left))
            array.append(node.value)
            if node.right:
                array.extend(self.in_order(node.right))
        return array
    
    def pre_order(self, node = None, /) -> list[int]:
        """Is returned root -> left -> right format"""
        if not node:
            self.__check_for_emptiness()
            node = self.root
        array = []
        if node:
            array.append(node.value)
            if node.left:
                array.extend(self.pre_order(node.left))
            if node.right:
                array.extend(self.pre_order(node.right))
        return array
    
    def post_order(self, node = None, /) -> list[int]:
        """Returns in left -> right -> root form"""
        if not node:
            self.__check_for_emptiness()
            node = self.root
        array = []
        if node:
            if node.left:
                array.extend(self.post_order(node.left))
            if node.right:
                array.extend(self.post_order(node.right))
            array.append(node.value)
        return array
    
    def level_order(self) -> list[int]:
        """To traverse the tree from the root to the children row by row"""
        self.__check_for_emptiness()
        current = [self.root]
        array = []
        while current:
            array.append(current[0].value)
            if current[0].left:
                current.append(current[0].left)
            if current[0].right:
                current.append(current[0].right)
            del current[0]
        return array
                
    def clear(self):
        """Clean the tree completely"""
        self.root = None
        self.__number_of_nodes = 0