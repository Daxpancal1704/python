import string

sentence=input("Sentence : ").lower()

vowles="aeiou"
vowle_count={}
total_consonants=0

for char in sentence:
    if char in string.ascii_lowercase:
        if char in vowles:
            vowle_count[char]=vowle_count.get(char,0)
            print(char)