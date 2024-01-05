"""module to check if a given integer is a palindrom without casting to string"""

while True:
    try:
        user_input = input("Please enter a number to see if it is a palindrome : ")
        user_input = int(user_input)
        break
    except ValueError:
        print(f"\nYou have entered \"{user_input}\" which is incorrect.\
Please try again and use whole numbers only.\n")

original = user_input
rev = 0

while user_input > 0:
    rev = rev * 10 + (user_input % 10)
    user_input = user_input // 10

if rev == original:
    print(f"\n{original} is a palindrome!")
else:
    print(f"\n{original} is not a palindrome!")
