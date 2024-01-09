#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    json_str = '"' + str(my_obj).replace('"', '\\"') + '"'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json_str)
