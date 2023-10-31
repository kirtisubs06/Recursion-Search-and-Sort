#################################################################
# Course: CS 3B Intermediate Software Design in Python
# Name: Kirti Subramanian
# Topic: Recursion, Search, and Sort
# Description: Test that demonstrates linear recursion, search, and sort functionalities on a user-provided list.
# Filename: kirtisubramaniana1.py
# Date: 7/18/2023
#################################################################

from kirtisubramaniana1 import linear_recursive_duplicate, search_item, sort_list


def get_user_list():
    """
    Asks the user to input a list of items and returns the list.

    Returns:
        list: The list of items entered by the user.
    """
    while True:
        try:
            user_input = input("Enter a list of items separated by spaces (e.g., item1 item2 item3): ")
            user_list = user_input.split()
            break
        except:
            print("Invalid input. Try again.")
    return user_list


def test_linear_recursive_duplicate(lst):
    """
    Demonstrates the linear_recursive_duplicate function with different test cases.

    Args:
        lst (list): The list to test the function with.
    """
    print("Test 1:")
    print(linear_recursive_duplicate([]))
    print("Test 2:")
    print(linear_recursive_duplicate(lst))
    print("Test 3:")
    print(linear_recursive_duplicate(lst))
    print("Test 4:")
    print(linear_recursive_duplicate(lst))
    print("Test 5:")
    print(linear_recursive_duplicate(lst))


def test_search_item(lst):
    """
    Demonstrates the search_item function by searching for a target item in the list.

    Args:
        lst (list): The list to search for the target item.
    """
    target = input("Enter an item to search: ")
    if search_item(lst, target):
        print(f"{target} is in the list.")
    else:
        print(f"{target} is not in the list.")


def test_sort_list(lst):
    """
    Demonstrates the sort_list function by sorting the list.

    Args:
        lst (list): The list to sort.
    """
    sorted_lst = sort_list(lst)
    print(f"Sorted list: {sorted_lst}")


if __name__ == "__main__":
    # Get user input for the list of items
    user_list = get_user_list()
    print("Original list:", user_list)

    # Test linear recursion and print duplicates
    test_linear_recursive_duplicate(user_list)

    # Test search capability
    test_search_item(user_list)

    # Test sort capability
    test_sort_list(user_list)
