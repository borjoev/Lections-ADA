"============числа============="
# integers(int) - целые числа (1, 3, 6)


age = 10
# print(type(age)) # <class 'int'>
# type() - возвращает класс\тип данных к которому относится перемнная или значение

b = int('10')
print(type(b)) #<class 'int>




"==========float======="
#float - естественные числа\числа с плавающей точкой\десятичные

price = 105.5
print(type(price)) #<class 'float'>

price2 = float(1)
print(price2)

price3 = float('10.64')
print(price3) # 10.64
print(type(price3)) # <class 'float'>



# import decimal 
# from decimal import Decimal

# a = Decimal('0.1')
# print(a) # 0.1
# print(type(a)) # <class 'decimal.Decimal'>

"======================binary=================================="


a = bin(10)
print(a) # 0b1010
print(int(a, 2)) # 10


"====================================операции над числами======================="
5 + 7 #сложение
7 - 3 #вычитвние
10 * 4 #умножение
10/3 #деление
10//2 #целочислнное деление
5 % 2 #нахождение остатка от деления
2 ** 3 # возведение числа в степень (квадрат/куб и т.д)
25 ** 0.5 #нвхождение квадратрного корня


# модуль числа - из отрицательного числа в положительное |-5| = 5
# abs() - для полуения положительного числа



print(abs(-5))


#round() - округдение числа
print(round(1.3))
print(round(1.6))
print(round(13.49))
print(round(1.5))
print(round(1.51))





"""python3 <название файла"""





#sqrt - функция для нахождения квадратного корня числа. sqrt обзательно нужно импортировать

from math import sqrt
print(sqrt(25))
print(sqrt(49))
print(sqrt(65536))



# pow 
#1) возвлдит число в степень 
#2) находит остатокот делерия на 3 число


print(pow(2, 3, 3))




# divmod() - функция которая возвращает 2 числла где 1 число - целая часть от деления 2 число - остатк от деления 


print(divmod(8, 3))

print('5%2')
 




















