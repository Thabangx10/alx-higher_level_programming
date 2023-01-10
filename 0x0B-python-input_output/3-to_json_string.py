#!/usr/bin/python3
"""to_json_string"""

import json


def to_json_string(my_obj):
    """Return the json representation of a str(obj)
    """
    return json.dumps(my_obj)
