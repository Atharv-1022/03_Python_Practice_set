'''Take the string "  i love python programming  " and:

Remove extra spaces from both ends
Convert it to title case
Count how many times "o" appears'''

text="  i love python programming  "

print(text.strip())
print(text.title())

count=0
for i in text:
    if i=="o":
        count+=1
print(count)