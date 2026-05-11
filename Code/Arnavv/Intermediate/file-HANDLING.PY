# def read_file(filename):
#     try:
#         with open(filename,'r') as f:   
#             content = f.read()
#             print('\n',content, '\n')
#     except(FileNotFoundError) as e:
#         print(e)
        

# read_file('file.txt')


# with open('notes.txt', 'w') as f:
#     f.write('Learning Python is fun !!')



# with open('tasks.txt', 'w') as f:
#     f.write('''HI
# hiii
# hiiiii''')


# with open('tasks.txt', 'a') as f:
#     f.write("\nTask Completed!")

with open('tasks.txt') as f:
    lists_line = f.readlines()
    print(lists_line)