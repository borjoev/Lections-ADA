"=================словари========================="
# dict -  изменяемый итерируемый неупорядоченный неиндексируемый


# uszstan'}er = {'name': 'isa',
#         'city': 'bishkek',
#         'contry': 'Kyrgyzstan' }
# print(user['name'])
# print(user['city'])

# dict1 = {'a': 1, 'b': 2, 'c': 3, 'a': 4}
# print(dict1['a'])
# print(dict1['b'])

# dict1 = {'a': 1, 'b': 2}
# dict2 = dict([('a', 1), ('b', 2)])
# print(dict2)

# dict3 = dict(['ab', 'cd', 'ef'])
# print(dict3)

# dict4 = {}
# dict4['name'] = 'isa'
# dict4['city'] = 'bishkek'
# print(dict4)


"====================методы словарей================"
# print(dir(dict4))
# get() - метод который возвращает значение по ключу если такого ключа нет то возвращает none 
# pop() - метод который удаляет пару по ключу и возвращает значение
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# popped = dict_.pop("a")
# print(dict_)
# print(popped)

# # dict_.pop('a')



# # .popitem() - метод который удаляет последнюю пару и возвращает ее
# dict5 = {'a': 1, 'b': 2, 'c': 3}
# popped = dict5.popitem()
# print(dict5)
# print(popped)

# dict0 = ()
# print(dict0.popitem())

# .update() - расширяет словарь парами из второго словаря

# dict1 = {1: 'a', 2: 'b'}







# # .clear() - удаляет все пары в словаре
# dict1.clear()
# print(dict1)

# # .fromkeys() - метод для использоания словаря список ключей
# dict1 = dict.fromkeys('hi')
# print(dict1)

# dict2 = dict.fromkeys([1, 2, 3])
# print(dict2)

# dict3 = dict.fromkeys([1, 2, 3], 'hello')
# print(dict3)


# "==============================================="
# # keys, values, items
# # keys - метод который возвращает ключи
# # values - метод который возвращает значения
# # items - метод который возвращает пары ключ - значение в виде tuple

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {}


for key, value in dict2.items(): 
    dict2[value] = key
print(dict2)

    
