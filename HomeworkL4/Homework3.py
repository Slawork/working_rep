import functools
def show_function_name(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Запускается функция: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@show_function_name
def say_hello():
    print("Привет, мир!")

@show_function_name
def add(a, b):
    return a + b

say_hello()
print(add(2, 3))