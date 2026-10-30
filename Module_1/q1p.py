"""Question 1. Sentence Letter Report
Read a sentence from the user. Only letters count, so ignore spaces, digits, and
punctuation.
 Treat uppercase and lowercase as the same. Store the vowel counts in a
dictionary and print the following:

Each vowel that appears at least once as vowel: count, ordered by count from highest to
lowest. Vowels with equal counts are ordered alphabetically.

The total number of consonants as Consonants: N
The most common consonant as Most common consonant: x (count). If several consonants
tie, pick the alphabetically first. If the sentence has no consonants, print No consonants
instead"""

import string


seantence=input("Enter a Sentence: ").lower()


vowels="aeiou"
vowles_count={}
consonants={}
total_consonants=0


for char in seantence:
    if char in string.ascii_lowercase:
        if char in vowels:
            vowles_count[char]=vowles_count.get(char ,0) +1
        else:
            consonants[char]=consonants.get(char,0)+1
            total_consonants+=1

comman_vowels=sorted(vowles_count.items(),key=lambda  x : (-x[1],x[0]))
for vowels, count in comman_vowels:
    print(f"vowels is : {vowels}: {count}")


if total_consonants > 0:
    print(f"total consonants: {total_consonants}")
    comman_consonants=sorted(consonants.items(),key=lambda x : (-x[1],x[0]))[0]
    print(f"comman_consonants : {comman_consonants[0]} ({comman_consonants[1]})")
else:
    print("Non Comman")





