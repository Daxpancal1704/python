name="hello good morning"
print(name.upper())



def count_vowe(text):
    count=0
    for char in text.lower():
        if char in "aeiou":
            count=count+1
    return count

print(count_vowe("education"))       