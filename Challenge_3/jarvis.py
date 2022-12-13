import json


def get_dict_value(str_keys, str_dictionary):
    dictionary = json.loads(str_dictionary)
    keys = str_keys.split('/')
    for key in keys:
        dictionary = get_value(dictionary, key)
    print(dictionary)


def get_value(temp_dict, key):
    return temp_dict.get(key)


get_dict_value('a/b/c/d', '{"a":{"b":{"c":{"d":"e"}}}}')
