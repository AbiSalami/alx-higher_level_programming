#!/usr/bin/python3
# 101-locked_class.py
"""Defines a locked class."""

class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]

     def __setattr__(self, name, value):
         """Prevents dynamic creation of new attributes except 'first_name'."""
         if name != 'first_name':
             raise AttributeError("'LockedClass' object has no attribute '{}'"
                                .format(name))
         super().__setattr__(name, value)
