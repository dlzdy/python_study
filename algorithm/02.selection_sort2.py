# coding=utf-8


def find_max_index(arr):
    max_index = 0
    max_item = arr[0]
    for i in range(1,len(arr), 1):
        if arr[i] > max_item:
            max_item = arr[i]
            max_index = i
    return max_index


def selection_sort(arr):
    dest_arr = []
    while len(arr) > 0:
        max_index = find_max_index(arr)
        dest_arr.append(arr.pop(max_index))
    return dest_arr

print selection_sort([5, 3, 89, 4, 6, 66])