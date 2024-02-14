a = [1,5,8,9]
y = [1,5,6,8]

intersection = list(filter(lambda x: x in y, a))

print(intersection)