# 1. Write a Python program to read an entire text file.
# Ans...

# f = open("file-handling-prac.txt", "r")
# data = f.read()
# print(data)
# f.close()


# (2). Write a Python program to read first n lines of a file.
# Ans..


# f = open("file-handling-prac.txt", "r")
# print(f.readline())
# f.close()

# N = int(input("Enter N value: "))
# with open("file-handling-prac.txt", 'r') as f:

#     linesList= f.readlines()
#     print("The following are the first",N,"lines of a text file:")

# for textline in (linesList[:N]):
#     print(textline)



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
    

# (5). Write a Python program to read a file line by line and store it into a list.
# Ans...

# with open("file-handling-prac.txt", 'r') as f:
#     l = f.readlines()
#     print(l)


# (6). Write a Python program to read a file line by line store it into a variable.
# Ans...



# (7). Write a Python program to read a file line by line store it into a array.
# Ans...

# with open("file-handling-prac.txt", 'r') as f:
#     l = f.readlines()
#     print(l)



# (8). Write a python program to find the longest words.
# Ans...


# (9). Write a Python program to count the frequency of words in a file.
# Ans...

# from collections import Counter
# def word_count(freq):
#     with open("file-handling-prac.txt") as f:
#         return Counter(f.read().split())

# print("Number of words in the file :",word_count("file-handling-prac.txt"))


# (10). Write a Python program to count the number of lines in a text file.
# Ans...

# with open(r"file-handling-prac.txt", 'r') as f:
# 	num_of_lines = len(f.readlines())
# 	print('Total Number of lines:', num_of_lines)



# (11). Write a Python program to get the file size of a plain file.
# Ans...

# import os
# file = open("file-handling-prac.txt")
# file.seek(0, os.SEEK_END)
# print("Size of file is :", file.tell(), "bytes")


# (12). Write a Python program to write a list to a file
# Ans...

# fruits = ['Orange', 'Apple', 'Guava', 'Berry', 'Papaya', 'Kiwi']
# with open("file-handling-prac.txt", "w") as myfile:
#         for c in fruits:
#                 myfile.write("%s\n" % c)

# content = open("file-handling-prac.txt")
# print(content.read())



# (13). Write a Python program to copy the contents of a file to another file .
# Ans...

# import shutil 
# shutil.copyfile("file-handling-prac.txt",'second.txt')



# (14). Write a Python program to combine each line 
# from first file with the corresponding line in second file.
# Ans...

# with open("file-handling-prac.txt") as f1, open('second.txt') as f2:
#     for line1, line2 in zip(f1, f2):
        
#         print(line1 + line2)
		


# (15). Write a Python program to read a random line from a file.
# Ans...

# import random
# def random_line(rdm):
#     lines = open(rdm).read().splitlines()
#     return random.choice(lines)
# print(random_line('second.txt'))


# (16). Write a Python program to assess if a file is closed or not.
# Ans...

# f = open('second.txt', 'r')
# print(f.closed)
# f.close()
# print(f.closed)



# (17). Write a Python program to remove newline characters from a file.
# Ans...

# inputFile = "second.txt"
# with open(inputFile, 'r') as f:
#     linesList= f.readlines()
#     print([k.rstrip('\n') for k in linesList])
# f.close()


# (18). Write a Python program that takes a text file as input 
# and returns the number of words of a given text file.
# Note: Some words can be separated by a comma with no space.
# Ans...

# def count_words(textfile):
#     with open(textfile) as f:
#         data = f.read()
#         data.replace(",", " ")
#         return len(data.split(" "))
# print(count_words("third.txt"))



# (19). Write a Python program to extract characters 
# from various text files and puts them into a list.
# Ans...

# import glob
# char_list = []
# files_list = glob.glob("*.txt")
# for file_elem in files_list:
#     with open(file_elem, "r") as f:
#         char_list.append(f.read())
# print(char_list)



# (20). Write a Python program to generate 
# 26 text files named A.txt, B.txt, and so on up to Z.txt.
# Ans...

# import string, os
# if not os.path.exists("letters"):
#     os.makedirs("letters")
# for letter in string.ascii_uppercase:
#     with open(letter + ".txt", "w") as f:
#         f.writelines(letter)



# (21). Write a Python program to create a file 
# where all letters of English alphabet are listed by specified number of letters on each line.
# Ans...

# import string
# def letters_file_line(n):
#     with open("fourth.txt", "w") as f:
#         alphabet = string.ascii_uppercase
#         letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
#         f.writelines(letters)
# letters_file_line(3)