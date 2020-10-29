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
        return self.__binary_tree_node_sum(root)
    
    def build_binary_tree(self, root_id, json_data):
        self.root = self.__build_binary_tree(self.root, root_id, json_data)
        return self.root
    
    def __build_binary_tree(self, root, node_id, json_data):
        new_node = BinaryTree(value=json_data[node_id]["value"], left=None, right=None)
        if json_data[node_id]["left"] != None:
            new_node.left = self.__build_binary_tree(new_node, json_data[node_id]["left"], json_data)
        if json_data[node_id]["right"] != None:
            new_node.right = self.__build_binary_tree(new_node, json_data[node_id]["right"], json_data)
        return new_node
    
    def __binary_tree_node_sum(self, root, depth=0):
        if root == None:
            return self.node_sum
        self.node_sum += depth
        self.__binary_tree_node_sum(root.left, depth=depth+1)
        self.__binary_tree_node_sum(root.right, depth= depth+1)
        return self.node_sum

