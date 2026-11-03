
# file_name = input("Enter file name: ")

# try:
#     with open(file_name, "r") as file:
#         lines = 0
#         words = 0
#         longest_line = ""

#         for line in file:
#             lines += 1
#             words += len(line.split())

#             if len(line.strip()) > len(longest_line):
#                 longest_line = line.strip()

#         if lines == 0:
#             print("The file is empty.")
#         else:
#             print("Lines:", lines)
#             print("Words:", words)
#             print("Longest line:", longest_line)

# except FileNotFoundError:
#     print(f"File not found: {file_name}")



user_file=input("Enter a file name : ")
try:
    with open(user_file, "r")as r:
        lines=0
        words=0
        longest_line=''

        for line in r:
            lines+=1
            words +=len(line.split())
        if len(line.strip()) > len(longest_line):
            longest_line=line.strip()
        if lines== 0:
            print("The file is empty")
        else:
            print("Lines :",lines)
            print("words :",words)
            print("longest_line :",longest_line)
except FileNotFoundError as e:
    print(e)

