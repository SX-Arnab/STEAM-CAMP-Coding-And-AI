'''
Q.1Print Twinkle, Twinkle, little start, How I wonder what you are! 
using single print statement
Q.2 Store your name, age, height, and whether u r studet or not 
in a variable
Q.3 Typecaste num = '45' to integer
Q.4 Use a while loop to reverse a given number
'''

print("Twinkle, Twinkle, little start,\n How I wonder what you are!")

name = "Arnav"
age= 14
height = 4.5
student =True
print(name, age, height, student)

num = '45'
num_int= int(num)
print(num, num_int)


integer = int(input("Enter the number: "))
int_square = integer**2
int_cube = integer**3

print(int_square, int_cube)



num = int(input("Enter the number: "))
number = num
reversed_num = 0

while num > 0:
    r = num%10
    num //= 10
    reversed_num = reversed_num *10 + r

print(reversed_num)

if reversed_num == number:
    print("Number is same")
else:
    print("Numbers are different")    
