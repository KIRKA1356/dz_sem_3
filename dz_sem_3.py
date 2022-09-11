
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

# def convert():
#     num = int(input("Введите число в десятичной системе: "))
#     result =  []
#     while (num>0):
        
#         if num % 2 == 0:
#             result.insert(0,"0")
#         else: 
#             result.insert(0,"1")
#         num //= 2
    
#     a = (f"Ваше число в двоичной системе: ")   
#     b = ("".join(result))
#     word = a + b
#     print (word)
# convert()




# Задача 5

# list = [0, 1]
# num = int(input("Введите число ряда фибоначи: "))
# def fibon(num, list):
#     sum = 0
#     sum_2 = 0
#     for i in range(2,num+1):
#         sum = list[i-2] + list[i-1]
#         list.append(sum)
#     for i in range(0,num):
#         sum_2 = list[1] - list[0]
#         list.insert(0, sum_2)
#     print(list)
# fibon(num,list)