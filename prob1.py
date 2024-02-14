num = 123

func1 = lambda x: list(str(x))
func2 = lambda x: sum(list(map(lambda x: int(x), x)))


print(func2(func1(num)))

