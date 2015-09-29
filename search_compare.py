#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A module for searching & sorting algorithm comparisons."""

#__author__ = 'Erica Liz'

import time
import random


def sequential_search(a_list, item):
    """A sequential search.
    Args:
        a_list(list): a list with data to be searched.
        item(various): a selected item/value to be searched from the given list.
    Returns:
        (Tuple): A tuple with the processed time in seconds, & boolean value of
        whether the item exists in the list.
    Examples:
        >>> sequential_search(test_list, 42)
        (True, 2.2172927856445312e-05)
    """
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    return end-start, found


def ordered_sequential_search(a_list, item):
    """"An ordered sequential search.
    Args:
        a_list(list): a list with data to be searched.
        item(various): an item or value to be searched for in the given list.
    Returns:
        (Tuple): A tuple with the processed time in seconds, & boolean value of
        whether the item exists in the list.
    Examples:
        >>> ordered_sequential_search(test_list, 9)
        (False, 2.9802322387695312e-05)
    """
    start = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()
    return end-start, found


def binary_search_iterative(a_list, item):
    """An interative binary search.
    Args:
        a_list(list): a list with data to be searched.
        item(various): an item or value to be searched for in the given list.
    Returns:
        (Tuple): A tuple with the processed time in seconds, & boolean value of
        whether the item exists in the list.
    Examples:
        >>> binary_search_iterative(test_list, 5)
        (False, 1.71661376953125e-05)
    """
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    return end-start, found


def binary_search_recursive(a_list, item):
    """A recursive binary search.
    Args:
        a_list(list): a list with data to be searched.
        item(various): an item or value to be searched for in the given list.
    Returns:
        (Tuple): A tuple with the processed time in seconds, & boolean value of
        whether the item exists in the list.
    Examples:
        >>> binary_search_recursive(test_list, 2)
        (True, 6.9141387939453125e-06)
    """
    start = time.time()
    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)
    end = time.time()
    return end-start, found


def random_list(avg_time):
    """A list generator for algorithm searches."""
    my_list = []
    for item in range(avg_time):
        my_list.append(random.randint(1, avg_time))
    return my_list
   

def main():
    """The main function of the program."""
    test_num = [500, 1000, 10000]
    
    for i in test_num:
        counter = 100
        results = [0, 0, 0, 0]
        while counter > 0:
            my_list = random_list(i)
            results[0] += sequential_search(my_list, -1)[0]
            results[1] += ordered_sequential_search(my_list, -1)[0]
            results[2] += binary_search_iterative(my_list, -1)[0]
            results[3] += binary_search_recursive(my_list, -1)[0]
            counter -= 1
        print 'For the list of {}... '.format(i)
        print ('The sequential search took %10.7f seconds to run, '
                'on average.') % (results[0] / 100)
        print ('The ordered sequential search ' + 'took %10.7f seconds to run, '
                'on average.') % (results[1] / 100)
        print ('The iterative binary search ' + 'took %10.7f seconds to run, '
                'on average.') % (results[2] / 100)
        print ('The recursive binary search ' + 'took %10.7f seconds to run, '
                'on average.') % (results[3] / 100)

if __name__ == "__main__":
    main()
