#################################################################
# Course: CS 3B Intermediate Software Design in Python
# Name: Kirti Subramanian
# Topic: Recursion, Search, and Sort
# Description: Functions that duplicate items in a list and provide search and sort capabilities.
# Filename: kirtisubramaniana1.py
# Date: 7/18/2023
#################################################################

def linear_recursive_duplicate(lst):
    """
    Returns a new list with every item duplicated using linear recursion.

    Args:
        lst (list): The original list to duplicate items from.

    Returns:
        list: A new list with duplicated items.
    """
    if not lst:
        return []
    else:
        return [lst[0], lst[0]] + linear_recursive_duplicate(lst[1:])


def search_item(lst, target):
    """
    Searches for a target item in the list using Python's built-in search method.

    Args:
        lst (list): The list to search for the target item.
        target: The item to search for.

    Returns:
        bool: True if the target item is found, False otherwise.
    """
    return target in lst


def sort_list(lst):
    """
    Sorts the list using Python's built-in sort method.

    Args:
        lst (list): The list to sort.

    Returns:
        list: The sorted list.
    """
    lst.sort()
    return lst
