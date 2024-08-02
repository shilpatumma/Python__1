# 1. Write a Python program to read an entire text file.
# Ans...

# f = open("file-handling-prac.txt", "r")
# data = f.read()
# print(data)
# f.close()


# (2). Write a Python program to read first n lines of a file.
# Ans...

# N = int(input("Enter N value: "))
# with open("file-handling-prac.txt", 'r') as f:

#     linesList= f.readlines()
#     print("The following are the first",N,"lines of a text file:")

# for textline in (linesList[:N]):
#     print(textline)

# f.close()



# (3). Write a Python program to append text to a file and display the text
# Ans...

# f = open("file-handling-prac.txt", "a+")
# f.write(" appended text")
# f.close()


# (4). Write a Python program to read last n lines of a file.
# Ans...

# N = int(input("Enter N value: "))
# with open("file-handling-prac.txt", 'r') as f:

#     linesList= f.readlines()
#     print("The following are the first",N,"lines of a text file:")

# for textline in (linesList[N:]):
#     print(textline)

# f.close()

    

# (5). Write a Python program to read a file line by line and store it into a list.
# Ans...

# with open("file-handling-prac.txt", 'r') as f:
#     l = f.readlines()
#     print(l)
#     f.close()



# (6). Write a Python program to read a file line by line store it into a variable.
# Ans...


# def read_file_to_variable(file_path):
#     lines = []
#     try:
#         with open("file-handling-prac.txt", 'r') as file:
#             for line in file:
#                 lines.append(line.strip())
#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' was not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     return lines

# file_path = "file-handling-prac.txt"  
# lines = read_file_to_variable(file_path)

# for i, line in enumerate(lines):
#     print(f"Line {i + 1}: {line}")