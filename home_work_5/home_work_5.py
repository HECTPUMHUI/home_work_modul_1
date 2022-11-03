'''
 Щоб перевірити програми, необхідно почерзі розкоментовувати.
 '''

# # task 1
# list_sort = [1, 10, 9, 4, 5, 7, 2, 0]
#
#
# def sortex(list, a, b):
#     """
#     Сортує відрізок списку за вказівкою коричтувача
#
#     :param list: список який необхідно відсортувати
#     :param a: індекс початку сортування
#     :param b: індекс кінця сортування
#     :return: повертає список з відсортованим відрізком а,б
#     """
#     num = []
#     print(f"list before: {list}")
#     num = sorted(list[a:b])
#     list_sort_1 = []
#     list_sort_1.extend(list[0:a])
#     list_sort_1.extend(num)
#     list_sort_2 = []
#     list_sort_2.extend(list[b:])
#     list_sort_1.extend(list_sort_2)
#     print(list_sort_1)
#
#
# sortex(list_sort, 2, 6)

# # task 2

# fl = open('/home/hectpumhui/ALEVEL/projectLesson1/file_1.txt', 'r')
# for i in fl.readlines():
#     try:
#         res = eval(i)
#         fl.close()
#         with open('/home/hectpumhui/ALEVEL/projectLesson1/file_2.txt', 'a') as fl2:
#             fl2.write(f'{i[:-1]} = {res}')
#             fl2.write("\n")
#     except ZeroDivisionError:
#         fl.close()
#         with open('/home/hectpumhui/ALEVEL/projectLesson1/file_2.txt', 'a') as fl3:
#             fl3.write(f'{i[:-1]} = ділити на нуль не можна')
#             fl3.write("\n")
#
# fl = open('/home/hectpumhui/ALEVEL/projectLesson1/file_2.txt', 'r')
# print(fl.read())


# # task 3
#
# def papidrom(string):
#     """
#     Функція приймає рядок та повертає значення паліндром рядок чи ні.
#     :param strings: стрічка для перевірки
#     :return: повертає паліндром чи ні
#     """
#     str_2 = []
#     str_1 = string.lower()
#     for i in str_1:
#         if i.isalnum():
#             str_2.append(i)
#     if str_2 == str_2[::-1]:
#         print("Паліндром")
#     else:
#         print("Не паліндром")
