# f = open("firstfile.txt", "r")
# print(f.read())
# f.close()


# f = open("firstfile.txt", "r")
# print(f.read(11))
# f.close()


# for-in loop :=>
# f = open("firstfile.txt", "r")
# for line in f.readlines():
#     print(line)
# f.close()


# line number and content :=>
# f = open("firstfile.txt", "r")
# for i, line in enumerate(f.readlines()):
#     print(i, line)
# f.close()


# writing files :=>
# f = open("firstfile.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("firstfile.txt", "r")
# print(f.read())


# f = open("firstfile.txt", "w")
# f.write("...HEllo...")
# f.close()





# (17/07/24)
# f = open("demo.txt", "r")
# print(f.read())
# f.close()

# f = open("demo.txt", "w")
# f.write("....Good Morning ALL....")
# f.close()


# fruits = ["Apple\n", "Orange\n", "Grapes\n", "Watermelon"]
# f = open("demo.txt", "w")
# f.writelines(fruits)

# f = open("demo.txt", "a+")
# f.write ("\nStrawberry")
# f.close()

# f = open("demo.txt", "a+")
# f.write ("\nKiwi")
# f.close()





# (18/07/24)
# (1). Read File  :-->
# f = open("demo1.txt", "r")
# print(f.read())
# f.close()


# (2). Create a new empty text file (w)  :-->
# f = open("demo2.txt", "w")
# f.write("HEY...")
# f.close()


# (3). Writing to a File   :-->
# text = ("This is new content")
# f = open("demo2.txt", "w")
# f.write(text)
# print("Done writing")
# f.close()


# (4). Move File Pointer   :-->  (seek() method)
# f = open("demo2.txt", "r")
# f.seek(4)
# print(f.read())
# f.close()


# (5). tell method()   :-->
# f = open("demo2.txt", "r")
# f.readline()
# print(f.tell())


# (6).  Create a new empty text file (x)   :-->
# f = open("demo2.txt", "x")
# f.close()



# (7). create file in a specific directory   :-->
# with open(r"E:\Shilpa\SHILPA\Python__1\demo2.txt", "w") as f:
#     f.write("New content added...")
#     pass


# (8). checking if the file is present or not 
# import os
# print(os.listdir())
# print(os.path.isfile("demo2.txt"))


# (9). checking if the file is present or not 
# import os
# print(os.listdir(r"E:\Shilpa\SHILPA\Python__1"))
# print(os.path.isfile(r"E:\Shilpa\SHILPA\Python__1\demo2.txt"))


# (10). join directory path and file name to create file at the specified location.  :-->
# import os 
# path = r"E:\Shilpa\SHILPA\Python__1"
# file_name = "demo2.txt"
# with open(os.path.join(path, file_name), "w") as f:
#     f.write("...Second new content added...")


# (11). Create a File If Not Exists   :-->
# Example 1: create file if not exists.
# import os
# file_path = r"E:\Shilpa\SHILPA\Python__1\demo3.txt"
# if(os.path.exists(file_path)):
#     print("File already exists...")
# else:
#     with open(file_path, "w") as f:
#         f.write("New content added...")



# (12). Create File with a DateTime
# from datetime import datetime
# x = datetime.now()
# file_name1 = x.strftime("%d-%m-%y.txt") 
# with open(file_name1, "w") as f:
#     print("created", file_name1)



# file_name2 = x.strftime('%d-%m-%Y-%H-%M-%S.txt')
# with open(file_name2, "w") as f:
#     print("created", file_name2)



# file_name3 = r"E:\Shilpa\SHILPA\Python__1" + x.strftime("%d-%m-%Y-%H-%M-%S.txt") 
# with open(file_name3, "w") as f:
#     print("created", file_name3)




# 19/07/24
# open a file in python :

# (1). Opening a File in read mode with absolute path  
# f = open(r"E:\Shilpa\SHILPA\Python__1\demo.txt", "r")
# print(f.read())
# f.close()


# (2). Opening a File in read mode with relative path  
# f = open("demo.txt", "r")
# print(f.read())
# f.close()



# (3). Handling the FileNotFoundError
# try:
#     f = open("demo5.txt", "r")
#     print(f.read())
#     f.close()
# except FileNotFoundError:
#     print("Please check the path...")



# finally will be print either condition is wrong or right...
# try:
#     f = open("demo1.txt", "r")
#     print(f.read())
#     f.close()
# except FileNotFoundError:
#     print("File Not Found, Please check the path")
# finally:
#     print("Exit..")



# (5). Opening a File in Read mode
# try:
#     f = open("demo1.txt", "r")
#     print(f.read())
#     f.close()
# except IOError:
#     print("File Not Found, Please check the path")



# (6). Opening a File in Write Mode
# f = open("demo2.txt", "w")
# f.write("HEYYYYYYYYYY.........")

# f = open("demo2.txt", "r")
# print(f.read())
# f.close()



# (7). Opening a File in Append Mode
# f = open("demo2.txt", "a")
# f.write("\nHELLO......(in append mode)")

# f = open("demo2.txt", "r")
# print(f.read())
# f.close()



# (8). Closing a File
# f = open("demo2.txt", "r")
# print(f.read())
# f.close()



# (9). Opening file using with statement :
# (Consider there are two files ‘sample.txt’ and ‘sample2.txt’ and we want to copy the contents of the first file to the second.)

# with open("demo.txt", "r", encoding = "utf-8") as infile, open("demo1.txt", "w") as outfile:
#     for i in infile:
#         outfile.write(i)
# f = open("demo1.txt", "r")
# print(f.read())
# f.close()



# (10). Creating a new file : (the x mode)
# try:
#     with open("demo3.txt", "x") as f:
#         f.write("New file created.....")
#     f = open("demo3.txt", "r")
#     print(f.read())
# except:
#     print("The file already exists......")



# (11). Opening a File for multiple operations : ("+" operator)
# with open("demo3.txt", "r+") as f:
#     print(f.read())
#     f.write("\nOpening a File for multiple operations using + operator")



# (12). Opening a Binary file : (read the contents)
# with open("example.bin", "rb") as f:
#     x = f.read()
# print(x)




# 23/7/24
# read file in python : (read(), readline(), and readlines())

# (1). Read a Text File
# try:
#     f = open("demo.txt", "r")
#     print(f.read())
#     f.close()
# except FileNotFoundError:
#     print("File Not Found")



# (2). Reading a File Using the with Statement
# with open("demo.txt", "r") as f:
#     print(f.read())



# (3). readline(): Read a File Line by Line
# with open("demo.txt", "r") as f:
#     line = f.readline()
#     print(line)



# (4). Reading First N lines From a File Using readline()
# (using loop and strip function)

# with open("demo.txt", "r") as f:
#     for i in range(4):
#         print(f.readline())

# with open("demo.txt", "r") as f:
#     for i in range(4):
#         print(f.readline().strip())



# (5). Reading Entire File Using readline()
# # (end= "")
# with open("demo.txt", "r") as f:
#     line = f.readline()
#     # while line != "":
#         print(line, end= "")
#         line = f.readline()



# (6). Reading First and the Last line using readline()
# with open("demo.txt", "r") as f:
#     first_line = f.readline()
#     print(first_line)
#     for last_line in f:
#         pass
#     print(last_line)



# (7). readlines(): Reading File into List
# with open("demo.txt", "r") as f:
#     lines = f.readlines()
#     print(lines)


# (8). Reading first N lines from a file
# n = 3
# with open("demo.txt", "r") as f:
#     line = [next(f) for x in range (n)]
#     print(line)


# (9). Reading the last N lines in a file
# n = 3
# with open("demo.txt", "r") as f:
#     line = f.readlines()[n:]
#     print(line)


# (10). Reading N Bytes From The File
# try:
#     f = open("demo.txt", "r")
#     print(f.read(10))
#     f.close()
# except FileNotFoundError:
#     print("Please check the path")


# (11). Reading and Writing to the same file
# with open("demo.txt", "r") as f:
#     print(f.read)
#     f.write("Reading fresh")

# with open("demo.txt", "r+") as f:
#     print(f.read)
#     f.write("Reading fresh")


# with open("demo.txt", "r+") as f:
#     print(f.read())
#     f.write("\nsixth line")
#     print(f.read())
#     f.write("\nseventh line")
#     print(f.read())



# (12). Reading File in Reverse Order
# with open("demo.txt", "r") as f:
#     lines = f.readlines()
#     for line in reversed(lines):
#         print(line)



# (13) Reading a Binary file
# with open("flower.jpg", "rb") as f:
#     byte_content = f.read(1)
#     while byte_content:
#         print(byte_content)



# 26/07/24
# PDF EXAMPLE :

# (1). Reading a specific line from a File
# linenumber = 4
# f = open("demo.txt", "r")
# currentline = 3
# for line in f:
#     if (currentline == linenumber):
#         print(line)
#         break
#     currentline = currentline + 1


# (2). Reading the entire file at once
# f = open("demo.txt", "r")
# print(f.readlines())
# f.close()

# f = open("demo.txt", "r")
# result = f.read()
# print(result)


# (3). Write to a Python File
# (a). – write(string)
# f = open("demo1.txt", "w")
# f.write("Hello...")
# f.close()

# (b). – writelines(list)
# f = open("demo1.txt", "w")
# f.write("Python...\n")
# f.write("JAva...")
# f.close()

# color = ["red\n", "yellow\n", "black\n", "white\n", "blue"]
# f = open("demo1.txt", "w")
# f.writelines(color)
# f.close()


# (4). Append in a Python File
# f = open("demo1.txt", "a+")
# f.write("\nskyblye")
# f.close()