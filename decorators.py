







# def decorator(num):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 func(*args, **kwargs)
#         return wrapper
#     return inner_decorator


# @decorator(5)
# def hello():
#     print('hello world')
# hello()

"===================================================================================="


import requests
from time import time

def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time()
        func()
        end = time()
        time_exec = end - start
        print(f"время выполнения:  {time_exec} секунд")
    return wrapper

@benchmark
def fetch_webpage() -> None:
    webpage = requests.get('https://google.com')

fetch_webpage()


