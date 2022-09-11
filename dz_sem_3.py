
# # Задача 1

# list_num = [2, 5, 7, 29, 5, 4]
# def sum_of_num(list):
#     sum = 0
#     for i in range(len(list)):
#         if i % 2 != 0:
#             sum += list[i]
#         else: 
#             continue
#     print(sum)
# sum_of_num(list_num)

# Задача 2

# list_num = [2, 5, 7, 3, 3, 29, 5, 4]
# list_sum = []
# def pairs_of_numbers(list, list2):
#     for i in range(int(len(list)/2)):
#         inter = list[i] * list[len(list)-1-i]
#         list2.append(inter)
#     print (list2)
# pairs_of_numbers(list_num, list_sum)


# Задача 3

# list_num = [1.5, 1.03, 3.16, 5.56, 10.94]
# def multiplication_of_fractions(list):
#     list_2 = [] 
#     for i in list:
#         num_2 = i - int(i)
#         list_2.append(num_2)
#     min = list_2[0]
#     max = list_2[1]
#     for i in list_2:
#         if i < min:
#             min = i
#         elif i > max:
#             max = i
#     res = max - min
#     return res
# print(round(multiplication_of_fractions(list_num), 2))
        

# Задача 4
# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10



# Задача 5
# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи](https://clck.ru/yWbkX.)


