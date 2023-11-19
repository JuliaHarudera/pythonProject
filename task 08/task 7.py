import functools


def cache_results(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            print(f"Зчитано результат з кешу для ключа: {key}")
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result

            print(f"Збережено результат у кеш для ключа: {key}")

            return result
    return wrapper


@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


result1 = fibonacci(10)
result2 = fibonacci(10)

print(f"Результат 1: {result1}")  # Обчислюється та зберігається у кешу
print(f"Результат 2: {result2}")  # Використовується кеш