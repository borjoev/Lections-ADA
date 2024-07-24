"======================================list============================"

# # списки - это изменяемый индексируемый упорядоченный итерируемый тип данных который предназначен для хранения любых данных в определенном порядке


# list_ = [1, 2, 3, 4, 'hello']

# print(list_[1])
# print(list_[4][2])

# new_list = list()
# print(new_list)


# # range() - задает диапозон чисел принимает 3 аргумента 1 - начало диапозона 2 - конец 3 - шаг
# list2 = list(range(1, 11))
# print(list2)

# list3 = [1] * 10
# print(list3)



"================методы списков=========================="

# #print(dir(list3))

# # .append() - добавляет элемент в конец списка

# # list_ = []
# # list_.append(1)
# # print(list_)
# # list_.append


# # .pop() - удаляет элемент из списка по индексу и результатом метода будет удаленный элемент (метод возвращает удаленный элемент) если не указать индекс - удвлит с конца

# popped_el = list_.pop(0)
# print(popped_el)
# popped_el = list_.pop()
# print(popped_el)


# list2 = [1, 2, 3]
# list.pop(3)

# # .remove() - удаляет элемент из списка по значению

# list2 = [1, 2, 3, 4, True, 'hello']
# list2.remove(2)
# print.remove('hello')
# print(list2)



# # .count() - считает количество принятого элемента в списке

# print(list2.count(1))

# list3 = ['hello', 'hello', 'hello']
# print(list3.count(100))


# # .index - 

# list3 = ['hello', 'hello', 'hello', 1, 4, 100, None]
# print(list3.index(1))


# # .insert() - добавляет элемент в список по индексу


# # list3.insert(0, 'world')
# # print(list3)


# # # .extend() - добавляет элементы принятого списка в первый список изменяя его
# # list4 = [1, 2, 3, 4, {'a': 123}]
# # list3.extend(list4)
# # print(list3 + list4)


# # .reverse() - изменяет список расставляя его элементы в обратном порядке
# list3.reverse()
# print(list3)
# # .sort() - сортирует список состоящий из элементов одного типа данных


# list3.sort()

# print(list3)

# list5 = [1, 2, 3, 100, 1223, 211, 2000, 89343383883]

# list5.sort(reverse=True)

# # list5 = ['a','b', 'c', 'A', 'B', 'hello']
# # list5.sort
# # print(list5)


# # .clear() - очищает список
# list5.clear()
# print(list5)


# len() - считвет количесво элементов в омлндовательности
list1 = [1, 2, 3, 4, 5, 6, 7, 8, [1, 2, 3]]
print(len(list1))
len(list1)


a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

name, age, city = ['isa', 16, 'Bishkek']
print(name)
print(age)
print(city)