#!/usr/bin/python3
"""Load, add, save
"""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []
    
argc = len(sys.argv)
for idx in range(1, argc):
    items.append(sys.argv[idx])
save_to_json_file(items, "add_item.json")
