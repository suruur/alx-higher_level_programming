#!/usr/bin/python3
def load_from_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        json_str = file.read().strip()
    if json_str.startswith('"') and json_str.endswith('"'):
        return json_str[1:-1].replace('\\"', '"')
    else:
        return None
