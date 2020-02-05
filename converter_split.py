import pdb
import logging
import utils
import os
import rules

def convert_to_interface(json_content, logger,
    rules.rule_of_determine_group_parameter, rules.rule_for_single_parameter):
    out_interface = []

    def iterate_group_node(node, group_node):
        pdb.set_trace()
        for key in node:
            if isinstance(node[key], str):
                single_node = {
                    "name": key,
                    "label": key,
                    "type": get_type_of_parameter(node[key],
                            rule_of_determine_single_parameter)
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
                    "type": get_type_of_parameter(node[key],
                            rule_of_determine_single_parameter)
                }
                out_interface.append(single_node)
        utils.dump_json(out_interface)


def get_type_of_parameter(paramater, rules.rule_for_single_parameter):
    return "test"


def main():

    in_dir = "in"
    utils.is_exists_dir(in_dir, True)

    out_dir = "out"
    utils.is_exists_dir(out_dir, True)

    log_dir = 'log'
    utils.is_exists_dir(log_dir, True)

    prefix_out_file = "zudello_intrfc"
    extension_for_in_files = 'json'

    log_filename = os.path.join(log_dir, 'error.log')
    logging.basicConfig(filename=log_filename,
                        filemode='a',
                        format='%(asctime)s - %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logger = logging.getLogger()

    in_files = [file for file in os.listdir(in_dir) if file.endswith(extension_for_in_files)]
    for in_file in in_files:
        json_content = utils.get_json_from_file(os.path.join(in_dir, in_file), logger)
        if json_content:
            convert_to_interface(json_content, logger,
                rules.rule_of_determine_group_parameter,
                rules.rule_for_single_parameter
            )


if __name__ == "__main__":
    main()
