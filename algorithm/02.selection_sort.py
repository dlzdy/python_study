# coding=utf-8
# O(n*n)
def selection_sort(array):
    dest_array = []
    dest_array_len = len(array)
    for m in range(dest_array_len): #
        dest_array.append(array[0]) # 把原数组最大的赋值给目标数组
        for i in range(len(array)):
            if array[i] > dest_array[m]:
                dest_array[m] = array[i]
        array.remove(dest_array[m]) # 删除原数组最大的元素
    return dest_array

array = [2,4,5,67,6,3,7,9,0,12,2,4,56,7,98] # 0 - 14
#array = [2,7,98] # 0 - 14
print selection_sort(array)
