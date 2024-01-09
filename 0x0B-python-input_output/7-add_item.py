#!/usr/bin/python3
import 6-load_from_json_file as ld
import 5-save_to_json_file as sv
import sys
if __name__ == "__main__":
    args = sys.argv[1]
    items = ld.load_from_json_file("add_item.json")
    items_to_sv = items + args
    sv.save_to_json_file(items_to_sv, "add_item.json")
    ld_cn = ld.load_from_json_file("add_item.json")
    print(ld_cn)
