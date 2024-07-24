"============================Set========================"
# set(множество) - изменяемый неупорядоченный итерруемый неиндексируемый

# set_ = {1, 2, 3, 4}
# set2 = {1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3}
# print(set2)

# set_ = {(1, 2, 3), 3, (4, 5, 6), (1, 2, 3)}
# print(set_)

# "==========Методы set============="
# print(dir(set_))


# # .add() - добавляет элементы в set
# set1 = {1, 2, 3, 4, 5}
# set1.add(6)
# set1.add(7)
# set1.add(True)
# print(set1)

# # .pop() - удаляет случайный элемент из  set (но есть принцип FIFO)
# set2 = {1, 2, 3}
# popped = set2.pop()
# set2.pop()
# set2.pop()
# # set2.pop()
# print(set2, popped)


# .remove() - удвляет элемент из set
# set_ = {1, 2, 3}
# set_.remove(3)
# print(set_)
# set1 = {}
# set1.remove()
# print(set1)

# .difference() (-)
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1 - set2)
# print(set2 - set1)


# .symmetric_difference() - 


# .intersection() (&)
# set1 = {1, 2, 3, 4, 5, 6, 7, 8}
# set2 = {4, 5, 6, 7, 8, 9, 10}
# print(set1.intersection(set2))
# print(set1 & set2)


# .clear()
# set1 = {1, 2, 3, 4}
# set1.clear()
# print(set1)

# # .union() - возвразает множество которое солердит все элементы из всех


# set1 = {1, 2, 3}
# set2 = {True, False, (1, 2, 3)}
# set3 = {4, 5, 6, 7}

# result = set1.union(set2, set3)
# print(result)

# .issubset() - проверяет является ли одно множество подмножеством
# set1 = {1, 2}
# set2 = {1, 2, 3, 4, 5}
# print(set1.issubset(set2))

# # .issuperset() - проверята являтся ли мнодество
 
# set1 = {1, 2, 3, 6, 5}
# set2 = {1, 2, 3, 4, 5}
# print(set1.issuperset(set2))
# print(set2.issuperset(set1))


# .isdisjoint() - 
# set1 = {1, 2, 3, 4, 5}
# set2 = {6, 7, 8, 9, 10}
# print(set2.isdisjoint(set1))

# # .discard() - удвляет элемент по указанному значению
# set1 = {1, 2, 3, 4}
# set1.discard(3)
# print(set1)
"==============================================================="


# person = {'name': 'kelly', 'age': 25, 'city': 'new york'}
# print(person['age'])


# sample_set = {'yellow', 'orange', 'black'}
# sample_list = ['blue', 'green', 'red']
# sample_set.add('blue')
# sample_set.add('green')
# sample_set.add('red')
# print(sample_set)


# set1 = {6, 4, 2, 5, 7, 8, 10, 9}
# set1.discard(7)
# print(set1)

# set2 = {'python', 'it', 'c++', 'java', 'dart', 'programming'}
# set3 = {'html', 'css', 'c++', 'java', 'dart', 'programming'}
# print(set2 & set3)
# print(set3 - set2)


# set5 = {1, 2, 3, 4, 5}
# set5.add(6)
# set5.pop()
# print(set5)

# menu = {'manty': 200, 'plov': 150, 'lagman': 130, 'borsh': 100}
# menu2 = {'besh_barmak': 130, 'lagman': 135}
# menu.update(menu2)
# popped = menu.pop('borsh')
# print(menu)

# menu = {}
# dict1 = {'drinks': ['coca-cola', 'sprite', 'fanta']}
# menu.update(dict1)
# print(menu)

suitcase = []
suitcase.insert(0, 'шляпа')
suitcase.insert(1, 'носки')
suitcase.insert(2, 'кофта')
suitcase.insert(3, 'футболка')
suitcase.insert(4, 'штаны')
a = suitcase.pop()
print(suitcase)






