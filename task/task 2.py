def custom_range(start, stop, step=1):
    current = start
    while current < stop if step > 0 else current > stop:
        yield current
        current += step


for i in custom_range(1,10 ,2):
    print(i)


for i in custom_range(0, 10):
    print(i)

    