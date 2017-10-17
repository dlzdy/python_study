# coding=utf-8


# 阶乘，递归调用
def fact(i):
    # 基线条件
    if i == 1:
        return 1
    # 递归条件
    else:
        return i * fact(i - 1)

#2
print fact(2)
# 3!=6
print fact(3)
# 5! = 120
print fact(5)
# 8! = 120 * 6 * 7 = 40320
print fact(8)




