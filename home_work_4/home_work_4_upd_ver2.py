'''
 Щоб перевірити програми, необхідно почерзі розкоментовувати.
 '''
from audioop import reverse
from sqlite3 import connect

# # task 1 ver .01
# list_for_task = [1,2,3,4,5,6,7,8,9,10, 10 ,4]
# for i in range(1, 10):
#     list_for_task.append(i)
# # sum of list elements(b)
# result = sum(list_for_task)
# print(f'sum of list elements: {result}')
# # list of even index(a), - виправлено, тепер показує як у завдані вимагається
# for i in range(len(list_for_task)):
#     if i % 2 == 0:
#         print(f'even index:{i} his value: {list_for_task[i]}')
# # sum of even and not even elements(c)
# result_not_even_sum = 0
# result_even_sum = 0
# for i in list_for_task:
#     if i % 2 == 0:
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


# # task 2 ver .01
# list_for_example = []
# for i in open('/home/hectpumhui/ALEVEL/projectLesson1/12.txt', 'r'):
#     list_for_example.append(i[:-1])
# for i in list_for_example:
#     a = i.split()
#     fizz = int(a[0])
#     buzz = int(a[1])
#     secret_number = int(a[2])
#     for i in range(1, secret_number + 1):
#         if i % fizz == 0 and i % buzz == 0:
#             print('FB', end=' ')
#         elif i % fizz == 0:
#             print('F', end=' ')
#         elif i % buzz == 0:
#             print('B', end=' ')
#         else:
#             print(i, end=' ')
#     print()

# task3 ver 1.02
list_for_3 = [32, 43, 1, 3, 4, 5, 34, 5, 1, 7, 10, 34, 17, 11, 4, 3, 2, 6, 14, 1412424, 232, 223, 32, 1, 1, 1, 0, 2, 1,
              12, 2131, 11, 3441, 551, 113, 2, 1, 4, 5, 6, 22, 6]

num = []
num2 = []
k = 1

for i in range(len(list_for_3)):
    if i % 5 == 0:
        if k % 2 == 0:
            num = sorted(list_for_3[i:i + 5], reverse=True)
            num2.extend(num)
        else:
            num = sorted(list_for_3[i:i + 5], reverse=False)
            num2.extend(num)
        k += 1
print(num2)
