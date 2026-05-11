class InvalidNumber(Exception):
    pass

try:
    num = int(input("enter ur age: "))
    
    if(num>0):
        print("Your age is positive")
    else:
        raise InvalidNumber("Your age is Negative")
    
except(InvalidNumber) as e:
    print(e)