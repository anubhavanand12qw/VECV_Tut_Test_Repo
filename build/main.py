# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 10:35:09 2021

@author: aanand2
"""

def split_name(name:str) -> list:
    """
    This functions splits character from a string and return it as a list

    Parameters
    ----------
    name : str
        Your name.

    Returns
    -------
    list
        List of characters from your input string.

    """
    result = list(name)

    return result

print(split_name("Anubhav"))