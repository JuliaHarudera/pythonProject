def log_arguments_results(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функций {func.__name__} с аргуменом: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат вызова {func.__name__}: {result}")
        return result
    return wrapper


@log_arguments_results
def add_numbers(a, b):
    return a + b


add_numbers(3, 4)