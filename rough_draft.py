# # sortfunc
#
# nums = [45, 1, 35, 442, 2, 4, 5, 10, -1]
#
#
# def bubble_sort(ls):
#     flag = True
#     while flag:
#         flag = False
#         for i in range(len(ls) - 1):
#             if ls[i] > ls[i + 1]:
#                 ls[i], ls[i + 1] = ls[i + 1], ls[i]
#                 flag = True
#
#
# # bubble_sort(nums)
# print(nums)
#
#
# def selection_sort(ls):
#     for i in range(len(ls)):
#         lowest = i
#         for j in range(i + 1, len(ls)):
#             if ls[j] < ls[lowest]:
#                 lowest = j
#         ls[i], ls[lowest] = ls[lowest], ls[i]
#
#
# selection_sort(nums)
# print(nums)

class Example:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, first, second, third):
        print(first)
        print(second)
        print(third)


ex = Example('data', second=25, third=3.14)