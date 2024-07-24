"==============встроенные функции===================="
#map, filter, zip, reduce, enumerate

#zip - соединяет несолько последовательностей (получаем генератор в котором элементы - tuple)

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c']
# list3 = [10.5, 20.6, 100.54]

# zipped = zip(list1, list2, list3)
# # print(zipped)
# for el in zipped:
#     print(el)

# list1 = [1, 2, 3, 4, 5]



"===========Enumerate=========================="
#enumerate - нумерует последовательность (по дефолту с 0) (так же получаем генератор)

# enumerated = enumerate('hello')
# # print(enumerated)

# for el in enumerated:
#     print(el)


# string = 'hello world'
# print(list(enumerate(string[5:])))

"======================Map========================="
# map - принимает функцию и последовательность (записывает в новую последовательность результат функции в которую передвются элементы последовательности)

# list1 = ['1', '2', '3', '4', '5']
# mapped_list = list(map(int, list1))
# print(mapped_list)

# string = 'hello world'
# res = ''.join(map(lambda x: x.upper(), string))
# print(res)

# list_ = [1, 2, 3, 4, 5]
# list2 = list(map(lambda x: x**2, list_))
# print(list2)
# print(list(map(lambda x: x**2, list_)))

# list_ = [1, 2, 3, 4, 5]
# def to_2_degreed(x):
#     return x ** 2
# print(list(map(to_2_degreed, list_)))

"=======================Filter=========================="
# Filter - возвращает генератор с элементами прошедшими филбьтр(какое-то условие) принимает в себя функцию и последовательность
# list1 = [1, 0, -2, -3, -4, 5, 10]
# filltered = list(filter(lambda x: x > 0, list1))
# print(filltered)


# users = [
#     ('name': 'isa', 'age': 16),
#     ('name'): 'ivan', 'age': 12),
    
# ]


"""
вывести только имена пользовтельец которые млвдше 15

"""

"===============================Reduce============================="
from functools import reduce
# # reduce - принимает функцию и последовательость возвращает 1 результат (передаваемая функция должна принимать 2 аргумента)
# list_ = [1, 2, 3, 4, 5]
# res = reduce(lambda x, y: x*y, list_)
# print(res)

# string = 'hello'
# res = reduce(lambda x, y: x + '$' + y, string)
# print(res)

# string = 'hello world'
# print(reduce(lambda x, y: string.replace(x, y), string))

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 346, 44, 678, 456]
# res = reduce(lambda x, y: x if x<y else y, list_)
# print(res)


# list1 = [1, 17000, 134, 12431, 43542]
# res = reduce(lambda x, y: x+y, list1)
# print(res)

# list1 = [1, 17000, 134, 12431, 43542]
# res = list(map(lambda x: x**2, list1))
# print(res)

# list1 = [1, 17000, 134, 12431, 43542]
# res = list(filter(lambda x: x % 2 == 0, list1))
# print(res)

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 10]
# list2 = len(list(filter(lambda x: x % 2 != 0, list1)))
# list2 = len(list(filter(lambda x: x % 2 == 0, list1)))
# result = F'xtnyst'

# num = int(input('введите число'))
# for i in range(1, 51):
#     if i % 3 == 0:
#         print('fizz')
#     else:
#         print('buzz')
#     break

# res = list(map(lambda x: ))


# list1 = [1, 2, 3, 4, 234, 534, 123, -123, 342, 654]
# res = reduce(lambda x, y: x if x<y else y, list1)
# print(res)
