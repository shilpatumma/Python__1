# 1. Write a Python program to read an entire text file.
# Ans...

# f = open("file-handling-prac.txt", "r")
# data = f.read()
# print(data)
# f.close()


# (2). Write a Python program to read first n lines of a file.
# Ans...

f = open("file-handling-prac.txt", "r")
print(f.readline())
f.close()
