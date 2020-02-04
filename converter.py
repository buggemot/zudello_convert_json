import os
import sys
import io
import pdb
import logging
from json import loads, dumps


def write_to_file(out_file, content, mode="w", encoding='utf-8'):
    err = None
    try:
        with io.open(out_file, mode, encoding=encoding) as f:
            f.write(content)
    except Exception as err:
        return False, err
    return True, err


def read_file(in_file, mode="r", encoding='utf-8'):
    content, err = None, None
    try:
        with io.open(in_file, mode, encoding=encoding) as f:
            content = f.read()
    except Exception as err:
        return False, err
    return True, content


def is_exists_dir(name_of_dir, create=False):
    if os.path.isdir(name_of_dir):
        return True
    else:
        if create:
            try:
                os.mkdir(name_of_dir)
                return True
            except Exception as err:
                print("Error of creating dirrectory {} : {}".format(
                        name_of_dir, err
                ))
                sys.exit(1)
    return False


def load_json(content):
    try:
        content_json = loads(content)
    except ValueError as err:
        return False, err
    return True, content_json


def get_json_from_file(in_file, logger):
    ok, result = read_file(in_file)
    if ok:
        content = result
        ok, result = load_json(content)
        if ok:
            json_content = result
        else:
            print(result)
            logger.error("Error of loading json from file {}: {}".format(
                in_file, result
            ))
            return False
    else:
        print(result)
        logger.error("Error of reading file {}: {}".format(
            in_file, result
        ))
        return False
    return json_content


def convert_to_interface(json_content, logger,
    rule_of_determine_group_parameter, rule_of_determine_single_parameter):
    out_interface = []
    first_level_key = [k for k in json_content.keys()][0]

    for i in json_content[first_level_key]:
        for key in i:
            d_out = {}
            stack_keys = [key]
            while stack_keys:
                key = stack_keys.pop()
                if isinstance(i[key], dict):
                    d_out = {
                        "name": key,
                        "label": key,
                        "type": determine_type_of_parameter(i[key],
                                rule_of_determine_group_parameter),
                        "spec": []
                    }
                    temp_d = i[key]
                    stack_keys.extend([k for k in temp_d])
                    key = stack_keys.pop()
                elif isinstance(i[key], str):
                    if d_out:
                        spec_out = {
                            "name": key,
                            "label": key,
                            "type": determine_type_of_parameter(i[key],
                                    rule_of_determine_single_parameter),
                        }
                        d_out['spec'].append(spec_out)
            out_interface.append(d_out)
            pdb.set_trace()
            print('ok')

def determine_type_of_parameter(paramater, rule_of_determine_single_parameter):
    return "test"


def main():

    in_dir = "in"
    is_exists_dir(in_dir, True)

    out_dir = "out"
    is_exists_dir(out_dir, True)

    log_dir = 'log'
    is_exists_dir(log_dir, True)

    prefix_out_file = "zudello_intrfc"
    extension_for_in_files = 'json'

    log_filename = os.path.join(log_dir, 'error.log')
    logging.basicConfig(filename=log_filename,
                        filemode='a',
                        format='%(asctime)s - %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logger = logging.getLogger()

    #parameter, regex for parameter, regex for value
    rule_of_determine_group_parameter = [
        ('array'), # Array of items of the same type
        ('​collection'), #An object
        ]
    rule_of_determine_single_parameter = [
        ('uuid', None, '[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[0-9A-F]{4}-[0-9A-F]{12}'), #UUID
        ('​email', '(?:e ?\-? ?(?:mail)?)', '[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}'), # Allows only a valid email address to be filled in
        ('​url', None, '[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'), #URL address
        ('text', 'string', '[\w\d ]+'),
        ('date', 'date', '(?:(?:date)|[\d\-\:]+)'), #Date or date with time
        ('​uinteger', None, '\b(?:(?:\d{1,3}(?:,\d{1,4})?)+'), #Positive whole number
        ('​integer', None, '([^\d]{,2}?(?:\d{1,3}(?:,\d{1,4})?)+'), #Whole number
        ('​boolean', None, None), # true or false value
        ('​buffer', None, None), # Binary buffer
        ('​cert'), #Certifcate in PEM format
        ('​color'), #Hexadecimal color input
        ('file'), #File selection
        ('filename'), #File name
        ('filter'), #An advanced parameter used for filtering
        ('folder'), #Folder selection
        ('hidden'), #Parameter of this type is hidden from the user
        ('json'), #Allows only a json valid against JSON Schema
        ('number'), #A number
        ('path'), #A path to a file or a folder
        ('pkey'), #Private key in PEM format
        ('port'), #A whole number in range from 1 to 65535
        ('select'), #A selection from predefined values
        ('time'), #Time in hh:mm or hh:mm:ss or hh:mm:ss.nnn format
        ('timestamp'), #Unix timestamp
        ('​timezone'), #Time zone name (e.g. Europe/Prague)
    ]

    in_files = [file for file in os.listdir(in_dir) if file.endswith(extension_for_in_files)]
    for in_file in in_files:
        json_content = get_json_from_file(os.path.join(in_dir, in_file), logger)
        if json_content:
            convert_to_interface(json_content, logger,
                rule_of_determine_group_parameter,
                rule_of_determine_single_parameter
            )


if __name__ == "__main__":
    main()
