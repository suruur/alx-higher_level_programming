#!/usr/bin/python3
def to_json_string(my_obj):
    if isinstance(my_obj, str):
        return '"' + my_obj.replace('"', '\\"') + '"'
    else:
        return None
