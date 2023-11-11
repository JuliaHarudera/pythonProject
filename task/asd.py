def steptn(a, b):
    if b == 0:
        return 1
    else:
        return a * steptn(a, b - 1)

a = 2
b = 3


resulit = steptn(a, b)
print(f"{a}в степени {b} равно {resulit}")