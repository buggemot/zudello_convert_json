"""
Script to Convert JSON object to Zudello interface
"""
#import pdb
import logging
import re
import os
import utils
import rules


def generate_out_interface(json_content, node):
    #pdb.set_trace()
    for k, v in json_content.items():
        if isinstance(v, dict):
            if True:
                dict_node = {
                    "name": k,
                    "label": split_camel_case(k),
                    "type": "array",
                    "spec": []
                }
            generate_out_interface(v, dict_node['spec'])
            node.append(dict_node)
        elif isinstance(v, list):
            for i in v:
                if True:
                    list_node = {
                        "name": k,
                        "label": split_camel_case(k),
                        "type": "collections",
                        "spec": []
                    }
                    generate_out_interface(i, list_node['spec'])
                    node.append(list_node)
        else:
            single_node = {
                "name": k,
                "label": split_camel_case(k),
                "type": get_type_of_parameter(k, v)
            }
            node.append(single_node)
    return node


def split_camel_case(text_value):
    split_text_value = ""
    for i, l in enumerate(text_value):
        if str.isupper(l) and i > 0:
            split_text_value += " "
        split_text_value += l
    return split_text_value


def get_type_of_parameter(key, value):
    """
    Return type of value using rules
    """
    for rule in rules.rule_for_single_parameter:
        parameter, rule_for_key, rule_for_parameter = rule
        if rule_for_key:
            is_search_key = re.search(rule_for_key, key, re.IGNORECASE) or False
        if rule_for_parameter:
            if isinstance(value, str) and len(value) == 0:
                return "text"
            if not (isinstance(value, str) or isinstance(value, bytes)):
                value = str(value)
            is_match_parameter = re.match(rule_for_parameter, value, re.IGNORECASE) or False
            if is_search_key or is_match_parameter:
                return parameter
    return "unknown"


def add_extension(filename, extension):
    if filename.endswith(extension):
        return filename
    else:
        return "{}.{}".format(filename, extension)


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
            out_interface = generate_out_interface(json_content, [])
            # for k, v in generator_node(json_content):
            #     print("{} - {}".format(k, v))
            # out_interface = convert_to_interface(json_content)
            in_file = add_extension(in_file, 'json')
            out_file_name = os.path.join(out_dir, prefix_out_file + in_file)
            utils.dump_json(out_file_name, out_interface)

if __name__ == "__main__":
    main()
