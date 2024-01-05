'''
convert roman numeral into numeric value (guarantee to work from 1-3999)
further improvements would be additional notes on invalid inputs and suggestions for correct input
'''
print("Welcome! This program will take any valid roman numeral and return the numerical value.\n")

# set values for each possible numeral
rom_num_dict = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XX": 20,
    "XXX": 30,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CC": 200,
    "CCC": 300,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
    "MM": 2000,
    "MMM": 3000,
}

# create list of ordered numerals
rom_num_list = []
for keys in rom_num_dict:
    rom_num_list.append(keys)
print(f"List of possible numerals. Order of numerals are important.\
{rom_num_list}")

# loop for user to input a roman numeral and check it is valid
while True:
    user_input = input("Please type a roman numeral: ").upper()

    # restarT variable to start over at user input if input is invalid
    RESTART = False

    # loop through characters in user input to check they are valid
    for char in user_input:
        if not char in rom_num_list:
            print(f"\nError: {char} is an invalid input.")
            RESTART = True
            continue
    # restart if error is returned
    if RESTART:
        print("Please try again.\n")
        continue

    # set original to be printed later
    original = user_input

    # using ordered list of numerals, loop through user input and break
    # it up into fragments and store in a new list
    fragments = []
    for i in rom_num_list:
        if i in user_input:
            char_index = user_input.index(i)
            fragments.append(user_input[char_index:])
            user_input = user_input[:char_index]

    # loop through list of fragments and check in numeral list
    # if not in list then the user input must be incorrect and start again
    # otherwise, sum value of numerals when looked up to dictionary
    TOTAL = 0
    for i in fragments:
        if not i in rom_num_list:
            print(f"\nError: {i} is an invalid input.")
            RESTART = True
            continue
        else:
            TOTAL += rom_num_dict.get(i)

    # restart if error is returned
    if RESTART:
        print("Please try again.\n")
        continue
    break

print(f"\"{original}\" converted to a numerical value is {TOTAL}.")
