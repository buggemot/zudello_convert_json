"""
Script to Convert JSON object to Zudello interface
"""
#import pdb
import logging
import re
import os
import utils
import rules


def convert_to_interface(json_content):
    """
    Convert to Zudello interface
    """
    out_interface = []

    def iterate_group_node(node, group_node):
        for key in node:
            if isinstance(node[key], str):
                single_node = {
                    "name": key,
                    "label": key,
                    "type": get_type_of_parameter(key, node[key])
                }
                group_node['spec'].append(single_node)
        return group_node

    first_level_key = [k for k in json_content.keys()][0]
    for node in json_content[first_level_key]:
        for key in node:
            if isinstance(node[key], dict):
                group_node = {
                    "name": key,
                    "label": key,
                    "type": "array",
                    "spec": []
                }
                out_node = iterate_group_node(node[key], group_node)
                out_interface.append(out_node)
            elif isinstance(node[key], list):
                for item in node[key]:
                    group_node = {
                        "name": key,
                        "label": key,
                        "type": "collection",
                        "spec": []
                    }
                    out_node = iterate_group_node(item, group_node)
                    out_interface.append(out_node)
            else:
                single_node = {
                    "name": key,
                    "label": key,
                    "type": get_type_of_parameter(key, node[key])
                }
                out_interface.append(single_node)
        return out_interface


def get_type_of_parameter(key, value):
    """
    Return type of value using rules
    """
    for rule in rules.rule_for_single_parameter:
        parameter, rule_for_key, rule_for_parameter = rule
        if rule_for_key:
            is_search_key = re.search(rule_for_key, key, re.IGNORECASE) or False
        if rule_for_parameter:
            is_match_parameter = re.match(rule_for_parameter, value, re.IGNORECASE) or False
        if is_search_key or is_match_parameter:
            return parameter
    return "unknown"


def main():
    """
    main function
    """
    in_dir = "in"
    utils.is_exists_dir(in_dir, True)

    out_dir = "out"
    utils.is_exists_dir(out_dir, True)

    log_dir = 'log'
    utils.is_exists_dir(log_dir, True)

    prefix_out_file = "zudello_intrfc_"
    #extension_for_in_files = 'json'

    log_filename = os.path.join(log_dir, 'error.log')
    logging.basicConfig(filename=log_filename,
                        filemode='a',
                        format='%(asctime)s - %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logger = logging.getLogger()

    in_files = os.listdir(in_dir)
    for in_file in in_files:
        print("File: {}".format(in_file))
        json_content = utils.get_json_from_file(os.path.join(in_dir, in_file), logger)
        if json_content:
            out_interface = convert_to_interface(json_content)
            out_file_name = os.path.join(out_dir, prefix_out_file + in_file)
            utils.dump_json(out_file_name, out_interface)

if __name__ == "__main__":
    main()
