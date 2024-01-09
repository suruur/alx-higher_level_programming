#!/usr/bin/python3
def from_json_string(my_str):
    if my_str.startswith('"') and my_str.endswith('"'):
        return my_str[1:-1].replace('\\"', '"')
    else:
        return None
