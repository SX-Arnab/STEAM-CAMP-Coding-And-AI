# cube_num = [i**3 for i in range(1, 6)]
# print(cube_num)


even_num = [i for i in range(10,15)if i%2 == 0]
print(even_num)

from functools import reduce

num = [1, 2, 3, 4]

sum = lambda a,b: a+b

print(reduce(sum, num))