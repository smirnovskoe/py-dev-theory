x = [_ for _ in range(10)]

z, *y = ( 'a' for _ in range(10))

print(type(z), y)


