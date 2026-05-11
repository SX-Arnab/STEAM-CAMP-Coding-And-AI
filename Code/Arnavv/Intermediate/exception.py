try:
    x= int(input("Enter the num: "))
    y= int(input("Enter the num: "))
    print(x/y)
except ZeroDivisionError:
    print("Cannot divide by zero")


# Questions (1)

# try:
#     num1 = int(input("Enter the number: "))
#     num2 = int(input("Enter the number: "))
#     print(num1/num2)

# except(ZeroDivisionError, ValueError) as e:
#     print(f"The code gave error: {e}")

# # Questions (2)


# class ValueError(Exception):
#     pass

# try:
#     age = int(input("Enter the age: "))
#     if
#     print(age)


# except:
#     raise ValueError("Age is negative")
