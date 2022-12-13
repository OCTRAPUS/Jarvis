import json
import logging

logging.basicConfig(level=logging.INFO)


def get_dict_value(str_keys, str_dictionary):
    dictionary = json.loads(str_dictionary)
    try:
        keys = str_keys.split('/')
        for key in keys:
            dictionary = get_value(dictionary, key)
    except KeyError:
        logging.error("Error with the Key")
    except Exception as ex:
        logging.error(f"Hit the Exception {ex}")

    print(dictionary)


def get_value(temp_dict, key):
    return temp_dict.get(key)


get_dict_value('a/b/c/d', '{"a":{"b":{"c":{"d":"e"}}}}')
