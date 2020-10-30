class BinaryTree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class BinaryTreeSum:

    def __init__(self):
        self.node_sum = 0
        self.root = None
    
    def BinaryTreeNodeDepthSum(self, root):
        """Method that calculates sum of depths of all nodes of the given tree.
        @root: Start node of the Binary tree."""
        return self.__binary_tree_node_sum(root)
    
    def build_binary_tree(self, root_id, json_data):
        """Method that builds the tree with the given JSON.
        @root_id: ID of the start node.
        @json_data: Dictionary of nodes."""
        self.root = self.__build_binary_tree(self.root, root_id, json_data)
        return self.root
    
    def __build_binary_tree(self, root, node_id, json_data):
        """Private methods that internally builds the Binary tree with given JSON.
        @root: Object of BinaryTree class, means any node in the Binary Tree.
        @node_id: ID of the root.
        @json_data: Dictionary of nodes."""
        new_node = BinaryTree(value=json_data[node_id]["value"], left=None, right=None)
        if json_data[node_id]["left"] != None:
            new_node.left = self.__build_binary_tree(new_node, json_data[node_id]["left"], json_data)
        if json_data[node_id]["right"] != None:
            new_node.right = self.__build_binary_tree(new_node, json_data[node_id]["right"], json_data)
        return new_node
    
    def __binary_tree_node_sum(self, root, depth=0):
        """Private method that internally calculates the sum of depths of all nodes.
        @root: Start node of the Binary Tree.
        @depth: Depth of the current node. For start node, depth will be 0."""
        if root == None:
            return self.node_sum
        self.node_sum += depth
        self.__binary_tree_node_sum(root.left, depth=depth+1)
        self.__binary_tree_node_sum(root.right, depth= depth+1)
        return self.node_sum

