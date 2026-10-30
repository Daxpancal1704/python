import string

sentence=input("Enter a sentence: ").lower()

vowles="aeiou"
vowles_count={}
consonants_count={}
total_consonants = 0


for char in sentence:
    if char in string.ascii_lowercase:
        if char in vowles:
            vowles_count[char]=vowles_count.get(char ,0) +1
        else:
            consonants_count[char]=consonants_count.get(char,0)+1
            total_consonants+=1

#.print vowles report

sorted_vowels=sorted(vowles_count.items(),key=lambda x: (-x[1],x[0]))
for vowles ,count in sorted_vowels:
    print(f"{vowles} : {count} ")

#print consonants report

if total_consonants > 0:
    print(f"consonants: {total_consonants}")
    most_comman=sorted(consonants_count.items(),key=lambda x :(-x[1], x[0]) )[0]
    print(f"Most comman {most_comman[0]} ({most_comman[1]})")
else:
    print("Not comman")  