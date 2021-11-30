from typing import List
import random


def swap(array: List[int], a: int, b: int):
    """
    Function swaps elements a and b in array
    :param array: list of int
    :param a: index of element a
    :param b: index of element b
    """
    buf = array[a]
    array[a] = array[b]
    array[b] = buf


def merge(ar1: List[int], ar2: List[int]) -> List[int]:
    """
    Function merges two lists
    :param ar1: list 1
    :param ar2: list 2
    :return: Merged list
    """
    i = 0
    j = 0
    c = []
    while i < len(ar1) or j < len(ar2):
        if i == len(ar1):
            c += ar2[j:]
            break
        elif j == len(ar2):
            c += ar1[i:]
            break
        if ar1[i] <= ar2[j]:
            c.append(ar1[i])
            i += 1
        else:
            c.append(ar2[j])
            j += 1
    return c


def bubble_sort(array: List[int]) -> List[int]:
    """
    Function sorts a list with bubble sort algorithm
    :param array: A list of int to sort
    :return: Sorted list of int
    """
    sorted_array = array.copy()
    for j in range(len(sorted_array), 0, -1):
        for i in range(1, j):
            if sorted_array[i] < sorted_array[i - 1]:
                swap(sorted_array, i, i - 1)
    return sorted_array


def merge_sort(array: List[int]) -> List[int]:
    """
    Function sorts a list with merge sort algorithm
    :param array: A list of int to sort
    :return: Sorted list of int
    """
    if len(array) == 1:
        return array
    a_left = merge_sort(array[:len(array) // 2])
    a_right = merge_sort(array[len(array) // 2:])
    return merge(a_left, a_right)


def quick_sort(array: List[int], start, end):
    """
    Function sorts a list with quick sort algorithm. Function changes the passed list!
    :param array: A list of int to sort
    :param start: Start point
    :param end: End point
    """
    # if start is None:
    #     start = 0
    # if end is None:
    #     end = len(array) - 1
    if start >= end: return
    p = array[random.randint(start, end)]

    i, j = start, end
    while i <= j:
        while array[i] < p: i += 1
        while array[j] > p: j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quick_sort(array, start, j)
    quick_sort(array, i, end)
