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


import tkinter
import os
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir='D:/', title='Выберите файл ',
                                          filetypes=(('Текстовый файл', '.txt'),
                                                     ('Все файлы', '*'), ('Музон ебать', '.mp3')))
    text['text'] = text['text'] + '' + filename
    os.startfile(filename)


window = tkinter.Tk()
window.title('Проводник')
window.geometry('500x200')
window.configure(bg='silver')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл: ', height=5, width=72, background='light grey')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=15, height=3,
                               text='Выбрать файл ', background='grey', activebackground='dark grey',
                               command=file_select)
button_select.grid(column=1, row=3, pady=10)
window.mainloop()
