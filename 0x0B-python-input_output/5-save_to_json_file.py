#!/usr/bin/python3
#5-save_to_json_file.py
import json

def save_to_json_file(my_obj, filename):
    """
    Write a Python object to a text file using JSON representation.
    
    Args:
        my_obj (obj): A Python object to be serialized to JSON.
        filename (str): The name of the file to write the JSON representation to.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

