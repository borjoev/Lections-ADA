"==============================Turple==============="
# кортеж(turple) - неизменяемый индексируемый упорядоченный итерируемый тип данных предназначенный для хранения любых в определенном порядке (в целом не отличвется от списков просто он не изменяемй поэтому занимает меньше памяти)

tuple1 = (1, 2, 3)
print(type(tuple1))
tuple2 = (5)
print(type(tuple2))
turple2 = tuple('hello')
print(turple2)
# ('h' 'e' 'l' 'l' 'o')
tuple3 = 1, 2, 3
print(tuple3)

tuple4 = (1, 2, 3, [1, 2, 3])
tuple4[-1].append('hello')
print(tuple4)



tuple6 = tuple([1, 2, 3, 'hello', 1000, 811900])
print(dir(tuple6))


"===========================методы Tuple==========="
# .count() - cчитвет количество принятого элемента в кортеже (tuple)

tuple_ = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, False, True)
print(tuple_.count(1))

tuple7 = ('hello', 'hello', 'hello')
print(tuple7.count('hello'))

# .index
tuple8 = (1, 2 , 1)