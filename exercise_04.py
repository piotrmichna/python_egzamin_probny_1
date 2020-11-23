def div(n, m):
    return [i for i in range(n, m + 1) if i % 2 == 0 and i % 3 != 0]


result = div(0, 100)
print(result)
