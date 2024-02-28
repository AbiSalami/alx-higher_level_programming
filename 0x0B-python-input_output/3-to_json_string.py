#!/usr/bin/python3
#3-to_json_string.py
import json

def to_json_string(my_obj):
    """
    Convert a Python object to its JSON representation as a string.
    
    Args:
        my_obj (obj): A Python object.
        
    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)

