# "=======================Comprehssion========================="
# ""''
# # езкльтат  for элемент  in  помледовательность
# # i for i in list1 
# # результат for элемент  in  помледовательность if фильтр - фильтрация
# # i for i in list1 if 1 % 2 == 0
# # тело1 if  условие  else  тело2  for элемент  in  последовательность
# # 'четное'  if i % 2 == 0 else  ' нечетное' for i in range(1, 11)
# # # # ""'

# # comprehession = (i for i in range(1, 6))
# # print(comprehession)

# # print(next(comprehession))

# # #next() - это функция которая запрашивает у генератора текущий элемент


# # "========================  синтаксический сахар=============   "
# # # list_comprehession
# # list_comprehession = list((i**2 for i in range(1, 6)))
# # print(list_comprehession)
# # list_comprehession2 = [i**2 for i in range(1, 6)]

# # list_comp = [i for i in range(1, 11)if i % 2 == 0]
# # print(list_comp)

# # list3 = []
# # for i in range(1, 11):
# #     if i % 2 == 0:
# #         list3.append(i)
# # print(list3)

# # list1 = []
# # for i in range(5):
# #     list1.append('hello')
# # print(list1)


# "==================dict comprehession=============="
# dict_ = dict((i, i**2)for i in range(10))
# print(dict_)
# dict_ = {i: i**2 for i in range(10)}
# print(dict_)

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {value: key for key, value in dict1.items()}
# print(dict2)

# dict_ = {i: i for i in range(1, 11)}
# print(dict_)

# dict2 = {i: str(i) for i in range(1, 11)}
# print(dict2)

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# dict_ = {}
# for ind in range(len(list1)):
#     key = list1[ind]
#     value = list2[ind]
#     dict_[key] = value
# print(dict_)

# dict_ = {list1[ind]: list2[ind] for ind in range(len(list1))}
# print(dict_)

# dict_ = dict(zip(list1, list2))
# print(dict_)

# "================= вложенные  comprehession============="

# dict1 = {}
# for i in range(1, 6):
#     key = 1
#     value = [j for j in range(1, i+1)]
#     dict1[key] = value
#     print(dict1)

#     dict_ = {i: [j for j in range(1, i+1)]for i in range(1, 6)}
#     print(dict_)

#     dict_ = {i: list(range(1, i+1)) for i in range(1, 6)}
#     print(dict_)


# list1 = []
# for i in range(10):
#     inner_list = []
#     for j in range(5):
#         inner_list.append('hello world')
#     list1.append(inner_list)
# print(list1)

# list1 = [['hello world for j in range(5)']for i in range(10)]
# print(list1)

# list1 = [['hello world']*5 for i in range(10)]
# print(list1)

# list1 = [['hello world']*5]*10
# print(list1)



# list1 = [[1, 2, 3, 4, 5] for i in range(1, 11)]
# print(list1)

# dict_ = {}
# for i in range(1, 6):
#     inner_dict = {}
#     for j in range(1, i+1):
#         list_ = []
#         for k in range(1, i+1):
#             list_.append(k)
#             inner_dict[j] = list_
#     dict_[i] = inner_dict
# print(dict_)







