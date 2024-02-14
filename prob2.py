input = ['a', 'b', 'c', 'aa', 'bb', 'ccc']

func1 = sorted(input, key = lambda x: (len(x), x[0]) )

print(func1)