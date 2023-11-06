def geometric_progression(a, r):
    current_term = a

    while True:
        yield current_term
        current_term *= r


a = 2
r = 3


gen = geometric_progression(a, r)

for _ in range(5):
    print(next(gen))