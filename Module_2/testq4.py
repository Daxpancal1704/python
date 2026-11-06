file_name=input("Enter file name :")
try:
    with open(file_name , "r")as read:
        line=0
        words=0
        lonegest_line=''
        for line in read:
            words+=len(line.split())
        if len(line.strip())>len(lonegest_line):
            lonegest_line=line.strip()
        if line == 0:
            print("File is empty")
        else:
            print("Line: ",line)
            print("words: ",words)
            print("longest_line: ",lonegest_line)
except FileNotFoundError as e:
    print(e)

