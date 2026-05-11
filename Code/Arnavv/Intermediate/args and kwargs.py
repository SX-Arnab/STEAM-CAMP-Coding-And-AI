# def sum_all(*nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     return(sum)


# print(sum_all(1,3,45,6,7))



def print_details(**abc):
    for key, value in abc.items():
        print(f"{key} : {value}")
        

print_details(name = "alice", age =25, city = "delhi")