# Take a user input string and check if it is a palindrome (same forwards and backwards)

user_input=input("Enter a string to cheak weather it's palindrom:")

if user_input==user_input[::-1]:
    print("Yes it is a Palindrom")
else:
    print("No, it's not a palindrom")