"get the sentence from user side and after get sentances is lowecase,remove spaceing "
import string

sentence=input("Enter  a Sentence: ")

#Storing value in this 
vowels="aeiou"
vowels_count={}
consonant={}
total_consonant=0


#start the looping 

for char in sentence:
    if char in string.ascii_lowercase:
        if char in vowels:
            vowels_count[char] = vowels_count.get(char,0) + 1
        else:
            consonant[char]=consonant.get(char,0) + 1
            total_consonant +=1

#Counting the vowles
comman_vowles=sorted(vowels_count.items(),key=lambda x : (-x[1],x[0]))
for vowels , count in comman_vowles:
    print(f"{vowels}:{count}")

if total_consonant > 0:
    print(f"Consonants : {total_consonant}")    
    comman_consonant=sorted(consonant.items(),key=lambda x : (-x[1],x[0]))[0]
    print(f"Most comman consonant {comman_consonant[0]}({comman_consonant[1]})")
else:
    print("Non")