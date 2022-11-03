'''
 Щоб перевірити програми, необхідно почерзі розкоментовувати.
 '''

# # task 1 ver 1.1
# str_1 = input(f'Please enter some symbols for first string: ')
# str_2 = input(f'Please enter some symbols for second string: ')
# str_3 = input(f'Please enter some symbols for third string: ')
#
# list_for_srts = [str_1, str_2, str_3]
#
# for strs in list_for_srts:
#     if len(strs) % 2 == 0:
#         result = len(strs) // 2
#         result_2 = len(strs) - result
#         print(strs[result-1]+strs[result])
#     else:
#         result = len(strs) // 2
#         result_2 = len(strs) - result
#         print(strs[result::result_2])

# # task 2
# while True:
#     str_1 = input(f'Please enter some string from 5 to 15 symbols: ')
#     if len(str_1) >= 5 and len(str_1) <= 15:
#         break
# result = len(str_1) // 2
# stat = str_1[result::]
# stat_2 = str_1[:result:]
# stat_3 = stat + stat_2
# temp = stat_3[:-3]
# temp_for_three_symbols = stat_3[-3:]
# fiinish = temp + temp_for_three_symbols.upper()
# print(fiinish)


# # task 3 ver 1.1
# while True:
#     str_1 = input(f'Please enter some character set !> 10: ')
#     if len(str_1) <= 10:
#         break
# lenght_of_input = len(str_1)
# if len(str_1) <= 3:
#     print(str_1[-lenght_of_input:].lower())
# else:
#     total = str_1[:-3] + str_1[-3:].lower()
#     midle = len(str_1) // 2
#     first_half = total[:midle]
#     secon_half = total[midle:]
#     temp = secon_half[-3:]
#     third_half = secon_half[:-3]
#     glue_together = first_half+ temp + third_half
#     print(f'result: {glue_together}')

#
# # task 4 ver 1.1
# width_of_sqaruk = int(input('Please enter size of your sqaruk: '))
# temp = width_of_sqaruk - 2
# while True:
#     for i in range(width_of_sqaruk):
#         print("#", end=" ")
#     print('')
#     break
#
#
# while temp > 0:
#     print("#", end=" ")
#     for i in range(width_of_sqaruk - 2 ):
#         print(" ", end=" ")
#     print('#', end=" ")
#     print('')
#     temp -= 1
#
#
# while True:
#     for i in range(width_of_sqaruk):
#         print("#", end=" ")
#     print('')
#     break