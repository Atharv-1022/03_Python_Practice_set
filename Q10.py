# Write a program that counts how many vowels are in a given string

text=input("Enter your full name:")
count=0
vowels=["a","i","o","e","u"]
for i in text.lower():
    if i in vowels:
        count+=1
print(count)