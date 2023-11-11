def decorator(func):
    def wrapper(*args, **kwargs):
        print("Действие перед началом фунций ")
        result = func(*args, **kwargs)
        print("Действие в конце  фунций")
        return result
    return wrapper


@decorator
def example_function():
    print()


example_function()