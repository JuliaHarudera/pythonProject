import functools
import json

results_cache = {}


def save_result_to_file(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = hash((args, frozenset(kwargs.items())))
        if key in results_cache:
            print(f"Зчитано результат з кешу для ключа {key}")
            return results_cache[key]
        else:
            result = func(*args, **kwargs)
            results_cache[key] = result

            print(f"Збережено результат у кеш для ключа {key}")

            return result

    return wrapper


@save_result_to_file
def add_numbers(a, b):
    print("выконеня функций")
    return a + b


result1 = add_numbers(2, 3)
result2 = add_numbers(3, 4)

print(f"Результат 1: {result1}")
print(f"Результат 2: {result2}")