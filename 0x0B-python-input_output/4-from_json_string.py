#!/usr/bin/python3
#4-from_json_string.py
import json

def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.
    
    Args:
        my_str (str): A JSON string.
        
    Returns:
        obj: A Python data structure represented by the JSON string.
    """
    return json.loads(my_str)

