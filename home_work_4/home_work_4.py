'''
 Щоб перевірити програми, необхідно почерзі розкоментовувати.
 '''


# # task 1
# list_for_task = []
# for i in range(1, 10):
#     list_for_task.append(i)
# # sum of list elements(b)
# result = sum(list_for_task)
# print(f'sum of list elements: {result}')
# # list of even index(a), sum of even and not even elements(c)
# result_not_even_sum = 0
# result_even_sum = 0
# for i in list_for_task:
#     if i % 2 == 0:
#         print(f'even index:{i} his value: {list_for_task[i]}')
#         result_even_sum += i
#     else:
#         result_not_even_sum += i
# print(f'sum of EVEN elements: {result_even_sum}')
# print(f'sum of NOT EVEN elements: {result_not_even_sum}')
# # value of max element (d)
# max_elem = max(list_for_task)
# print(f'max elements: {max_elem}')
# for i in list_for_task:
#     if i >= max_elem:
#         print(f'max element: {i} and index: {list_for_task.index(max_elem)}')


# # task 2
# num = []
# list_for_example = []
# for i in open('file_1.txt', 'r'):
#     list_for_example.append(i[:-1])
# print(list_for_example)
# for i in list_for_example:
#     num.append(i.split(" "))
#
# print(num[0][1])
# lend = len(list_for_example)
#
# while lend > 0:
#     k = 0
#     fizz = int(i[k])
#     k += 1
#     buzz = int(i[k])
#     k += 1
#     secret_number = int(i[k])
#
#     for k in range(1, secret_number + 1):
#         if k % fizz == 0 and k % buzz == 0:
#             print('FB', end=' ')
#         elif k % fizz == 0:
#             print('F', end=' ')
#         elif k % buzz == 0:
#             print('B', end=' ')
#         else:
#             print(i, end=' ')
#     lend -= 1


# task 3
# ver 1.0
# listex = [32, 43, 1, 3, 4, 5, 34, 5, 1, 7, 10, 34, 17, 11, 15, 16, 17, 11, 4, 812]
# print(listex)
# res = sorted(listex[:5])
# res_2 = sorted(listex[5:10], reverse=True)
# res.extend(res_2)
# res_3 = sorted(listex[10:15])
# res.extend(res_3)
# res_4 = sorted(listex[15:20], reverse=True)
# res.extend(res_4)
# print(res)

# ver 1.01
