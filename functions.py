# "==========================================функции====================="

# # def my_len(obj):
# #     count = 0
# #     for element in obj:
# #         count += 1
# #     return count

# # res = my_len(['hello', 1, 2, 3, 4, True, False, [1, 2, 3]])
# # print(len(['hello', 1, 2, 3, 4, True, False, [1, 2, 3]]))
# # print(res)



# a = ['hello', 1, 2, 3, 4, True, False, [1, 2, 3]]
# count = 0
# for element in a:
#     count += 1
# print(count)



# "=================аргументы и параметры====================="

# def my_len(obj): # obj - парамтер
#     count = 0
#     for element in obj:
#         count += 1
#     return count

# "=====================виды парамтеров======================="




# "===================виды аргументов======================="




# def add_or_add_10(num1, num2=10):

#     # ''''''
#     # складывает 2 числа
#     # если второе не передать сложит с 10

#     return num1 + num2

# number = 5
# print(add_or_add_10(number, ))


"====================*=========================================================="
# list1 = list(range(1, 11))
# list2 = [*range(1, 11)]
# print(list1)
# print(list2)


# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {**dict1}
# list1 = [*dict1]
# print(dict1)
# print(dict2)
# print(list1)


# def func(a, b=10, *args, **kwargs):
#     print('a -', a)
#     print('b -', b)
#     print('args -', args)
#     print('kwargs -', kwargs)
# func(1, 2, 3, 4, 5, 6, 7, 8, 9, c=10, d=123, v=45)


"=============lambda============================="
# lambda - анонимная функция

lambda_func = lambda x: x**10
print(lambda_func(10))


"=============================================================================="

# calc = {
#     '+': lambda n1, n2: n1 + n2,
#     '-': lambda n1, n2: n1 - n2,
#     '*': lambda n1, n2: n1 * n2,
#     '**': lambda n1, n2: n1 ** n2,
#     '/': lambda n1, n2: n1 / n2,
#     '//': lambda n1, n2: n1 // n2,
#     '%': lambda n1, n2: n1 % n2,
# }



# def main():
#     try:
#         num1 = int(input('введите первое число: '))
#         num2 = int(input('введите второе число: '))
#         oper = input('введите операцию: ')
#         func = calc[oper]
#         res = func(num1, num2)

#         print(num1, oper, num2, '=', res)

#     except ValueError:
#         print('введите число')
#     except KeyError:
#         print('такой операции нет')
#     except ZeroDivisionError:
#         print('на ноль делить нельзя')


# while True:
#     main()
#     if input('завершить yes/no? ').lower() == 'yes':
#         break

# main()

db = [
    {'name': 'isa', 'password': hash('isa123')},
    {'name': 'isa2', 'password': hash('123456789')}
]

def in_database(name):
    for user in db:
        if user['name'] == name:
            return True
    return False

def register(name, password1, password2):
    if in_database(name):
        raise Exception('пользователь с таким именем уже существует: ')     
    if password1 != password2:
        raise Exception('пароли не совпали!  ') 
    user = {'name': name, 'password':hash(password1)}
    db.append(user)
    return 'Вы успешно зарегистрировались!  '


def login(name, password):
    if not in_database(name):
        raise Exception('пользователь не найден')
    for user in db:
        if user['name'] == name:
            if user['password'] != hash(password):
                raise Exception('пароль неверный!  ')
    return 'вы успешно вошли в систему!  '

