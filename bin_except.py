# Author:  Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 10/23/2023
# Description: a binary search algorithm for a sorted list that returns the index of the target.
# If not found, raises a TargetNotFound exception


class TargetNotFound(Exception):
    """user-defined exception for when binary search does not find target"""
    pass


def bin_except(a_list, target):
    """
  Searches a_list for an occurrence of target
  list should be sorted
  If found, returns the index of its position in the list
  If not found, raises a TargetNotFound exception, indicating the target value isn't in the list
  """
    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    raise TargetNotFound
