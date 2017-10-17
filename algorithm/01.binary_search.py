# coding=utf-8
def binary_search_1(list, item):
    total_len = len(list)
    # 当前位置
    cur_position = (total_len - 1) / 2
    while cur_position >= 0 or cur_position < total_len:
        # high
        if list[cur_position] > item:
            cur_position = cur_position - cur_position / 2
        elif list[cur_position] < item:  #low
            cur_position = cur_position + (total_len - cur_position) / 2
        elif item == list[cur_position]:
            return cur_position

    return None

# 非递归方式
def binary_search(list, item):
    # 数组长度
    list_len = len(list)
    # 待比较数组的左边坐标
    low = 0
    # 待比较数组的右边坐标
    high = list_len - 1
    while low <= high:
        # 比较部分的，中间索引
        mid = (low + high ) / 2
        if list[mid] == item :
            return mid
        elif list[mid] > item :#[mid]大了
            high = mid - 1
        elif list[mid] < item :#[mid]小了
            low = mid + 1
    return None


def binary_search_recursion(_list, item):
    return binary_search_recursion2(_list, 0, len(_list) - 1, item)


def binary_search_recursion2(_list, low, high, item):
    mid = (low + high) / 2
    print "low=%d, high=%d, mid=%d, list[mid]=%d, item=%d" %(low, high, mid, _list[mid], item)
    if low > high:
        return None
    if _list[mid] == item:
        return mid
    if _list[mid] > item:
        high = mid - 1
        return binary_search_recursion2(_list, low, high, item)
    elif _list[mid] < item:
        low = mid + 1
        return binary_search_recursion2(_list, low, high, item)


my_list = [1, 3, 5, 7, 9, 15, 67, 89, 100]
'''
print binary_search(my_list, 1)
print binary_search(my_list, 5) #2
print binary_search(my_list, 7)#3
print binary_search(my_list, 9)#4
print binary_search(my_list, 89)#7
print binary_search(my_list, 100)#8
print binary_search(my_list, 101) #nonw
'''
print binary_search_recursion(my_list, 0) #none
print binary_search_recursion(my_list, 1) #0
print binary_search_recursion(my_list, 5) #2
print binary_search_recursion(my_list, 7)#3
print binary_search_recursion(my_list, 9)#4
print binary_search_recursion(my_list, 89)#7
print binary_search_recursion(my_list, 100)#8
print binary_search_recursion(my_list, 101)
''' '''