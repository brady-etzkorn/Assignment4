# simple_sorts.py
# bubble sort, selection sort, insertion sort
# Strongly suggest you turn off LLMs like
# GitHub Copilot, TabNine, etc. when working on this file.
# Writing a sorting algorithm yourself is the best
# way to learn how it works.
# Modified by: 

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1 == lst[j + 1], lst[j]

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        mid_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[mid_index]:
                mid_index = j
        lst[i], lst[mid_index] == lst[mid_index], lst[i]
            

def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] == key
    
