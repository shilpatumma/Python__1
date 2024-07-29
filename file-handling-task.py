# (1). Counting Words in a File

# num_of_words = 0
# with open("file-handling-task.txt", "r") as f:
#     for line in f:
#         words = line.split()
#         num_of_words += len(words)
# print("Number of words is : ")
# print(num_of_words)


# (2). search for a specific word in a file

with open("file-handling-task.txt", "r") as f:
    for line in f:
        for word in line.split():
            print(word)

    

