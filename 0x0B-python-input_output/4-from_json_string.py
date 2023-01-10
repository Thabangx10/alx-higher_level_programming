#!/usr/bin/python3
# 6-from_json_string.py
"""From JSON string to Object
"""
import json


def from_json_string(my_str):
    """Return the python representation of the JSON string
    """
    return json.loads(my_str)
