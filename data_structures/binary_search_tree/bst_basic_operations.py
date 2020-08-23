
class Node:

    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        self.parent = None
    

class BinarySearchTree:

    def __init__(self):
        self.__root = None

    def insert(self, data):
        self.__root = self.__insert(self.__root, data)
    
    def search(self, data, print_is_on=True):
        node_found = self.__search(self.__root, data)
        if node_found and print_is_on:
            print("Search result for", data, "= Found")
        elif node_found == None:
            print(data, "is NOT found in BST!")
        return node_found
    
    def in_order_traversal(self):
        if self.__root == None:
            print("BST is empty!")
            return
        print("In order traversal:", end=" ")
        self.__in_order_traversal(root=self.__root)  
        print("\n")
    
    def pre_order_traversal(self):
        if self.__root == None:
            print("BST is empty!")
            return
        print("Pre-order traversal:", end=" ")
        self.__pre_order_traversal(root=self.__root)
        print("\n")
    
    def next_biggest_node(self, data):
        print("Finding next value after " + str(data) + " : ", end=" ")
        node = self.search(data=data, print_is_on=False)
        if node == None:
            print(data, "is not at all present in this BST!! Hence cannot find the next biggest element")
            return
        next_node = self.__next_biggest_node(root=node, data=node.data)
        if next_node == None:
            return

    def delete(self, data):
        print("Deleting " + str(data), end="... ")
        node = self.search(data=data, print_is_on=False)
        if node == None:
            print(data, "is not in this BST!! Hence it cannot be deleted.")
            return
        self.__delete(node)
        
    # Private functions starts here
    def __delete(self, node):
        number_of_children = self.__get_number_of_children(node)
        if number_of_children == 0:
            self.__delete_node_with_0_child(node)
        elif number_of_children == 1:
            self.__delete_node_with_1_child(node)
        else:
            self.__delete_node_with_2_children(node)
    
    def __get_number_of_children(self, node):
        if node.left == None and node.right == None:
            return 0
        if (node.left == None and node.right != None) or (
            node.left != None and node.right == None):
            return 1
        return 2
    
    def __pre_order_traversal(self, root):
        if root == None:
            return
        print(root.data, end=" ")
        self.__pre_order_traversal(root.left)
        self.__pre_order_traversal(root.right)

    def __delete_node_with_0_child(self, node):
        # Case 1: node has 0 child
        self.__assign_parent_to_child_node(node=node, child_node=None)
    
    def __delete_node_with_1_child(self, node):
        # Case 2: node has only 1 child
        child_node = self.__find_single_child_node(node)
        self.__assign_parent_to_child_node(node, child_node)
    
    def __delete_node_with_2_children(self, node):
        # Case 3: node has 2 children
        successor_node = self.__next_biggest_node(node, node.data)
        node.data = successor_node.data
        # Now successor node's values are duplicated.
        # Hence successor_node has to be deleted.
        self.__delete(node=successor_node)
    
    def __find_single_child_node(self, node):
        if node.right != None:
            return node.right
        return node.left
    
    def __assign_parent_to_child_node(self, node, child_node=None):
        if node.parent == None: # Only one node in the BST
            self.__root = child_node
            return
        if node.parent.data == node.data: # this case can happen if this function
            # is visited after case 3
            if node.parent.right == node:
                node.parent.right = child_node
            else:
                node.parent.left = child_node
        elif node.parent.data < node.data: # then node is a right child of parent
            node.parent.right = child_node
        else: # then node is a left child of parent
            node.parent.left = child_node
        if child_node != None:
            child_node.parent = node.parent
        print("done!")


    def __next_biggest_node(self, root, data):
        if root.right != None:
            leftmost = self.__get_leftmost_node(root.right)
            return leftmost
        return self.__find_first_bigger_parent(root.parent, data)
    
    def __find_first_bigger_parent(self, parent_node, data):
        if parent_node == None:
            print("No next element because the given node is the biggest element in this BST!!")
            return None
        if parent_node.data > data:
            return parent_node
        return self.__find_first_bigger_parent(parent_node.parent, data)

    def __get_leftmost_node(self, root):
        if root.left != None:
            return self.__get_leftmost_node(root.left)
        return root

    def __search(self, root, data):
        if root == None:
            return None
        
        if root.data == data:
            return root
        
        if root.data < data:
            return self.__search(root.right, data)
        else:
            return self.__search(root.left, data)

    def __insert(self, root, data, parent=None):
        if root == None:
            node = Node()
            node.data = data
            node.parent = parent
            return node
        if root.data < data:
            root.right = self.__insert(root.right, data, root)
        elif root.data > data:
            root.left = self.__insert(root.left, data, root)
        else:
            print("Can't insert duplicate values!!--", data)
        return root

    def __in_order_traversal(self, root):    
        if root == None:
            return
        self.__in_order_traversal(root.left)
        print(str(root.data), end=" ")
        self.__in_order_traversal(root.right)

if __name__ == "__main__":
    integer_list = [1, 4, 5, -5, -3, 10, 6, 8, 7, 40, 35, 33, 34, 32, 31, 30, 29]
    for index, value in enumerate(integer_list):
        integer_list[index] = value + 10
    bst = BinarySearchTree()
    for number in integer_list:
        bst.insert(number)
    for number in integer_list:
        bst.next_biggest_node(number)
    new_integer_list = integer_list + [20, 3, 4, 5, 21, 40, 7, 8, 37]
    for number in new_integer_list:
        bst.search(number)
    bst.pre_order_traversal()
    for item in integer_list:
        bst.delete(item)
        bst.in_order_traversal()
        bst.pre_order_traversal()
