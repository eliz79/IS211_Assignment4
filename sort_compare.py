#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A module that is used for search & sort algorithms."""

#__author__ = 'Erica Liz'

import time
import random


def insertion_sort(a_list):
    """Insertion list sort function."""
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    end = time.time()
    return end-start, a_list


def gap_insertion_sort(a_list, start, gap):
    """A gap insertion sort function."""

    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


def shell_sort(a_list):
    """A shell list sort function."""
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.time()
    return end-start, a_list


def python_sort(a_list):
    """A list sort function."""
    start = time.time()
    a_list = a_list.sort()
    end = time.time()
    return end-start, a_list


def random_list(avg_time):
    """A random list generator."""
    my_list = []
    for item in range(avg_time):
        my_list.append(random.randint(1,avg_time))
    return my_list


def main():
    """The main function of the program."""
    test_num = [500, 1000, 10000]

    for i in test_num:
        counter = 100
        result = [0, 0, 0]

        while counter > 0:
            my_list = random_list(i)
            result[0] += insertion_sort(my_list)[0]
            result[1] += shell_sort(my_list)[0]
            result[2] += python_sort(my_list)[0]
            counter -= 1
        print 'For the list of {}... '.format(i)
        print ('Insertion Sort took %10.7f seconds to run,'
               'on average.' % (result[0] / 100))
        print ('Shell Sort ' + 'took %10.7f seconds to run,'
               'on average.' % (result[1] / 100))
        print ('Python Sort ' + 'took %10.7f seconds to run,'
               'on average.' % (result[2] / 100))

if __name__ == "__main__":
    main()
