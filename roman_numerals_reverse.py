'''
convert a numerical value up to 3999 into a roman numeral
'''

# set values for each possible numeral {value : numeral}
rev_rom_num_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
                    90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

# loop to request user input until valid number is provided
while True:
    try:
        user_input = int(input("Please enter a number between 1 & 3,999: "))
        # check input is in range 1 to 3999, if not request new input
        if not 1 <= user_input <= 3999:
            print(f"Sorry, {user_input} is not in the valid range of 1 to 3,999.\n")
            continue
        break
    # if user did not enter 'int', provide message and request input again
    except ValueError:
        print("Sorry, please enter whole numbers only.\n")
        continue

# set original input for later output
original = user_input

# loop through user input and break up into thousands,hundreds,tens,ones
split_units = []
while user_input != 0:
    value = user_input % (10 ** len(split_units))
    split_units.append(value)
    user_input -= value
# loop will always create a 0 value in [0] position in the list, so remove
split_units.remove(0)

# lop through split units, further split into units which match equivelant roman numerals
# example1: 3 == 1, 1, 1 == III
# example2: 70 == 50, 10, 10 == LXX
split_units_further = []
for i, value in enumerate(split_units):
    temp_value = int(value / (10 ** i))
    counter = temp_value
    # if value is 1/2/3 then split into 1's, multiply each by its unit
    if 1 <= temp_value <= 3:
        while counter != 0:
            split_units_further.append(1 * (10 ** i))
            counter -= 1
    # if value is 6/7/8 then minus 5 before splitting, split the remainder into 1's
    # multiply the 5 and 1's by the unit
    elif 6 <= temp_value <= 8:
        counter -= 5
        while counter != 0:
            split_units_further.append(1 * (10 ** i))
            counter -= 1
        split_units_further.append(5 * (10 ** i))
    # if value is 0/4/5/9 then multiply by its unit
    else:
        split_units_further.append(temp_value * (10 ** i))

# if user_input is a multiple of 10, list will contain empty values
# loop through list and remove "0" then reverse list
while 0 in split_units_further:
    split_units_further.remove(0)
split_units_further.reverse()

# loop through ordered list of values, look up corresponding numeral and add to string for output
NUMERALS = ""
for i, value in enumerate(split_units_further):
    NUMERAL = str(rev_rom_num_dict.get(value))
    NUMERALS += NUMERAL

# output answer to user
print(f"The numerical value \"{original}\", when converted to roman numerals,\
would read as {NUMERALS}.")
