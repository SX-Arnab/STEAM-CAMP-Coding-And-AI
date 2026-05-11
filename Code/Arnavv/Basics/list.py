# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])
# fruits[1]="orange"
# print(fruits)
# print(len(fruits))



list = [i for i in range(1, 11)]
print(list[0:3])
print(list[6:9])

num = [5, 2, 9, 1, 7]
num.sort()
print(num)
num.append(10)
print(num)
num.remove(2)
print(num)


names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")
print(names)   