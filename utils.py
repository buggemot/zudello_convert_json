import os
import sys
import io
from json import loads, dumps, dump

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


def dump_json(content):
    try:
        with open('test.json', 'w') as f:
            dump(content, f, indent = 4)
    except Exception as err:
        print(err)


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
