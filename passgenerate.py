import random;
import array;

# maximum length of password needed
# this can be changed to suit your password length
max_length = 15;

# declare arrays of the character that we need in out password
# Represented as chars to enable easy string concatenation

digits = ['0', '1', '2', '3', '4', 
          '5', '6', '7', '8', '9']

lowcase_Characters = ['a', 'b', 'c', 'd', 'e', 
                      'f', 'g', 'h', 'i', 'j', 
                      'k', 'l', 'm', 'n', 'o',
                      'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y',
                      'z']

upcase_Characters = ['A', 'B', 'C', 'D', 'E', 
                      'F', 'G', 'H', 'I', 'J', 
                      'K', 'L', 'M', 'N', 'O',
                      'P', 'Q', 'R', 'S', 'T',
                      'U', 'V', 'W', 'X', 'Y',
                      'Z']

symbols = ['@', '#', '$', '%', '=', 
          ':', '?', '.', '/', '|', 
          '~', '>','*', '(', ')', 
          '<']

# combines all the character arrays above to form one array
combined_List = digits + lowcase_Characters + upcase_Characters + symbols

# randomly select at least one character from each character set above
random_digit = random.choice(digits)
random_lower = random.choice(lowcase_Characters)
random_upper = random.choice(upcase_Characters)
random_symbols = random.choice(symbols)

# combine the character randomly selected above
# at this stage, the password contains only 4 characters but
# we want a 12-character password
temp_Password = random_digit + random_lower + random_upper + random_symbols

# now that we are sure we have at least one character from each
# set of characters, we fill the rest of
# the password length by selecting randomly from the combined
# list of character above.

for x in range (max_length - 4):
    temp_Password = temp_Password + random.choice(combined_List)
    # convert temporary password into array and shuffle to
    # prevent it from having a consistent pattern
    # where the beginning of the password is predictable
    temp_Password_List = array.array('u', temp_Password)
    random.shuffle(temp_Password_List)

# traverse the temporary password array and append the chars
# to form the password
password = ""
for x in temp_Password_List:
    password = password + x

# print out password
print(password)