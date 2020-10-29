import argparse
import json
from os import path

from binary_tree_operation import BinaryTreeSum

class Parser:
    
    def get_json_data(self):
        args = self.__command_line_reader()
        json_data = self.__validate_input_and_get_json(args)
        return self.__json_parser(json_data)

    # Private methods
    def __json_parser(self, json_data):
        if not json_data:
            print("Error: JSON cannot be empty.")
            exit(1)
        root_node = json_data["tree"]["root"]
        node_map = dict()
        for node_info in json_data["tree"]["nodes"]:
            node_map[node_info["id"]] = node_info
        return root_node, node_map
    
    def __command_line_reader(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--file_name', help="Provide the path to a JSON file",
            type=str, required=False
        )
        parser.add_argument('-s', '--string', help="Provide a JSON string",
            type=str, required=False
        )
        args = parser.parse_args()
        return args
    
    def __validate_input_and_get_json(self, args):
        if not args.file_name and not args.string:
            print("Error: One of file name or string is mandatory")
            exit(1)
        json_data = None
        if args.file_name:
            if not path.exists(path.abspath(args.file_name)) or not args.file_name.endswith(".json"):
                print("Error: Please provide valid JSON file")
                exit(1)
            with open(args.file_name, 'r') as fp:
                json_data = json.load(fp)
        elif args.string:
            try:
                json_data = json.loads(args.string)
            except json.decoder.JSONDecodeError:
                print("Error: Please provide valid JSON string.")
                exit(1)
        return json_data

        
def main():
    root_id, node_map = Parser().get_json_data()
    bts = BinaryTreeSum()
    root = bts.build_binary_tree(root_id, node_map)
    output = bts.BinaryTreeNodeDepthSum(root)
    print("output =", output)


if __name__ == "__main__":
    main()